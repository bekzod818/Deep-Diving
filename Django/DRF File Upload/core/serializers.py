from rest_framework import serializers

from django.utils import timezone

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")


class CVUploadSerializer(serializers.ModelSerializer):
    uploaded_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ("cv", "uploaded_at")

    def update(self, instance, validated_data):
        instance.uploaded_at = timezone.now()
        return super().update(instance, validated_data)
