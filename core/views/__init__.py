from django.template.response import TemplateResponse

# URL /, name "index"
def index(request):
    """
    Index page.
    If the user is logged out, shows a login link.
    If the user is logged in, shows a page that links to other pages.
    """
    return TemplateResponse(request=request, template="index.html")

# URL /about, name "about"
def about(request):
    """
    About page.
    Has a brief summary of what the website is for.
    """
    return TemplateResponse(request=request, template="about.html")
