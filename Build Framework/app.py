class DolphinApp:
    def __call__(self, environ, start_response):
        status = "200 OK"
        headers = [("Content-Type", "text/plain")]
        start_response(status, headers)
        return [b"Hello Dolphin!"]
