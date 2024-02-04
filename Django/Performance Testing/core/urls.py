from django.urls import path

from .views import all_courses

urlpatterns = [
    path("courses/", all_courses, name="all_courses"),
]
