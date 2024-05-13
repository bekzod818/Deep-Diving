from webob import Request, Response


class DolphinApp:
    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def handle_request(self, request):
        user_agent = request.environ.get("HTTP_USER_AGENT", "User agent not found")
        response = Response()
        response.text = (
            f"Welcome to Dolphin! Hello my friend with user agent {user_agent}"
        )
        return response


# class DolphinApp:
#     def __call__(self, environ, start_response):
#         status = "200 OK"
#         headers = [("Content-Type", "text/plain")]
#         start_response(status, headers)
#         return [b"Hello Dolphin!"]
