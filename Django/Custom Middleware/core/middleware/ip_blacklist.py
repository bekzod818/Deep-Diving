from django.conf import settings
from django.core.exceptions import PermissionDenied


class IPBlacklistMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if hasattr(settings, "BANNED_IPS") and settings.BANNED_IPS is not None:
            # check incoming request IP address is in the BANNED_IPS
            if request.META.get("REMOTE_ADDR") in settings.BANNED_IPS:
                raise PermissionDenied()

        response = self.get_response(request)
        return response
