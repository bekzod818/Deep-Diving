def app(environ, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return [b"Hello, World!"]


# server = make_server("localhost", 8000, app)
# server.serve_forever()
