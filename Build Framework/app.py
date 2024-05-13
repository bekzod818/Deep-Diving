from webob import Request, Response


class DolphinApp:
    def __call__(self, environ, start_response):
        request = Request(environ)

        response = Response()
        response.text = "Hello Dolphin!"

        return response(environ, start_response)


# class DolphinApp:
#     def __call__(self, environ, start_response):
#         status = "200 OK"
#         headers = [("Content-Type", "text/plain")]
#         start_response(status, headers)
#         return [b"Hello Dolphin!"]
