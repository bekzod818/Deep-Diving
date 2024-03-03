class HTMXMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        htmx_header = "HX-Request"
        header = request.headers.get(htmx_header) or None

        if header:
            request.htmx = header == "true"
        else:
            request.htmx = False

        response = self.get_response(request)
        return response
