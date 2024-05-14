from app import DolphinApp

app = DolphinApp()


@app.route("/home")
def home(request, response):
    response.text = "Hello from the Home page"


@app.route("/about")
def about(request, response):
    response.text = "Hello from the About page"


@app.route("/hello/{name}")
def greeting(request, response, name):
    """
    Simple greeting route
    /hello/Bekzod -> 'Hello Bekzod'
    /hello/John -> 'Hello John'
    """
    response.text = f"Hello {name}"


@app.route("/books")
class Books:
    def get(self, request, response):
        response.text = "Hello from the Books page"

    def post(self, request, response):
        response.text = "Endpoint to create a book"


"""
{
    "/home": home,
    "/about": about,
}
"""
