from django.http import JsonResponse

from .models import Course


def all_courses(request):
    queryset = Course.objects.select_related("author").all()

    courses = []

    for course in queryset:
        courses.append({"title": course.title, "author": course.author.name})

    return JsonResponse(courses, safe=False)
