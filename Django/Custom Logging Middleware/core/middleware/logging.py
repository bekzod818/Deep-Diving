import logging
import time

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s; %(message)s")
handler.formatter = formatter
logger.addHandler(handler)
logger.setLevel(logging.INFO)


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # logic executed before the request is passed to the View (or any other middleware)
        start_time = time.time()

        request_data = {
            "method": request.method,
            "ip_address": request.META.get("REMOTE_ADDR"),
            "path": request.path,
        }
        logger.info(request_data)

        response = self.get_response(request)
        duration = time.time() - start_time

        response_dict = {"status_code": response.status_code, "duration": duration}
        logger.info(response_dict)

        # logic executed after view is called

        return response
