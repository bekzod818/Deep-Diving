from app import DolphinApp

app = DolphinApp()


@app.route("/home")
def home(request, response):
    response.text = "Hello from the Home page"


@app.route("/about")
def about(request, response):
    response.text = "Hello from the About page"


"""
{
    "/home": home,
    "/about": about,
}
"""
