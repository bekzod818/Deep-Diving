from djangoql.admin import DjangoQLSearchMixin
from import_export.admin import ImportExportActionModelAdmin

from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.urls import reverse
from django.utils.html import format_html

from .forms import TicketAdminForm
from .models import Concert, ConcertCategory, Ticket, Venue


class ConcertInline(admin.TabularInline):
    model = Concert
    fields = ["name", "starts_at", "price", "tickets_left"]

    # optional: make the inline read-only
    readonly_fields = ["name", "starts_at", "price", "tickets_left"]
    can_delete = False
    max_num = 0
    extra = 0
    show_change_link = True


class VenueAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "capacity"]
    inlines = [ConcertInline]


class ConcertCategoryAdmin(admin.ModelAdmin):
    pass


class SoldOutFilter(SimpleListFilter):
    title = "Sold out"
    parameter_name = "sold_out"

    def lookups(self, request, model_admin):
        return [
            ("yes", "Yes"),
            ("no", "No"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "yes":
            return queryset.filter(tickets_left=0)
        else:
            return queryset.exclude(tickets_left=0)


class ConcertAdmin(admin.ModelAdmin):
    """
    Page	URL	                             Description

    List	admin:<app>_<model>_changelist	 Displays the list of objects
    Add	    admin:<app>_<model>_add	         Object add form
    Change	admin:<app>_<model>_change	     Object change form (requires objectId)
    Delete	admin:<app>_<model>_delete	     Object delete form (requires objectId)
    History	admin:<app>_<model>_history	     Displays object's history (requires objectId)

    """

    list_display = ["name", "venue", "starts_at", "price", "tickets_left"]
    list_select_related = ["venue"]
    list_filter = ["venue", SoldOutFilter]
    search_fields = ["name", "venue__name", "venue__address"]
    readonly_fields = ["tickets_left"]

    def display_sold_out(self, obj):
        return obj.tickets_left == 0

    display_sold_out.short_description = "Sold out"
    display_sold_out.boolean = True

    def display_price(self, obj):
        return f"${obj.price}"

    display_price.short_description = "Price"
    display_price.admin_order_field = "price"

    def display_venue(self, obj):
        link = reverse("admin:tickets_venue_change", args=[obj.venue.id])
        return format_html('<a href="{}">{}</a>', link, obj.venue)

    display_venue.short_description = "Venue"


@admin.action(description="Activate selected tickets")
def activate_tickets(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Deactivate selected tickets")
def deactivate_tickets(modeladmin, request, queryset):
    queryset.update(is_active=False)


class TicketAdmin(DjangoQLSearchMixin, ImportExportActionModelAdmin):
    form = TicketAdminForm
    list_display = [
        "customer_full_name",
        "concert",
        "payment_method",
        "paid_at",
        "is_active",
    ]
    list_select_related = ["concert", "concert__venue"]  # to avoid N + 1
    actions = [activate_tickets, deactivate_tickets]


admin.site.register(Venue, VenueAdmin)
admin.site.register(ConcertCategory, ConcertCategoryAdmin)
admin.site.register(Concert, ConcertAdmin)
admin.site.register(Ticket, TicketAdmin)
