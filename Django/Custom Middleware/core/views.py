from django.shortcuts import render


def index(request):
    print(request.htmx)
    context = {}
    return render(request, "core/index.html", context=context)
