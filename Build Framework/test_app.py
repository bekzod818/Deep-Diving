import pytest


def test_basic_route_adding(app):
    @app.route("/home")
    def home(req, resp):
        resp.text = "Hello World"


def test_duplicate_route_adding(app):
    @app.route("/home")
    def home(req, resp):
        resp.text = "Hello World"

    with pytest.raises(AssertionError):

        @app.route("/home")
        def home2(req, resp):
            resp.text = "Hello World"


def test_requests_can_be_sent_by_test_client(app, test_client):
    @app.route("/home")
    def home(req, resp):
        resp.text = "Hello World"

    response = test_client.get("http://testserver/home")

    assert response.text == "Hello World"


def test_parameterized_routing(app, test_client):
    @app.route("/home/{name}")
    def home(req, resp, name):
        resp.text = f"Hello {name}"

    assert test_client.get("http://testserver/home/Bekzod").text == "Hello Bekzod"
    assert test_client.get("http://testserver/home/John").text == "Hello John"


def test_default_response(test_client):
    response = test_client.get("http://testserver/nonexistent")

    assert response.status_code == 404
    assert response.text == "Not Found"


def test_class_based_get(app, test_client):
    @app.route("/books")
    class Books:
        def get(self, req, resp):
            resp.text = "Books page"

    assert test_client.get("http://testserver/books").text == "Books page"


def test_class_based_post(app, test_client):
    @app.route("/books")
    class Books:
        def post(self, req, resp):
            resp.text = "Endpoint to create a book"

    assert (
        test_client.post("http://testserver/books").text == "Endpoint to create a book"
    )


def test_class_based_method_not_allowed(app, test_client):
    @app.route("/books")
    class Books:
        def post(self, req, resp):
            resp.text = "Endpoint to create a book"

    response = test_client.get("http://testserver/books")

    assert response.status_code == 405
    assert response.text == "Method Not Allowed"
