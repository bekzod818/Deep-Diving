from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    cv = models.FileField(upload_to="cvs/%Y/%m/%d/", null=True, blank=True)
    uploaded_at = models.DateTimeField(null=True, blank=True)
