from django.urls import path

from .views import CVUploadView

urlpatterns = [
    path("upload-cv/", CVUploadView.as_view(), name="upload-cv"),
]
