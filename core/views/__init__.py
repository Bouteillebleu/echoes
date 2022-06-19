from django.template.response import TemplateResponse

from login_required import login_not_required

# URL /, name "index"
@login_not_required
def index(request):
    """
    Index page.
    If the user is logged out, shows a login link.
    If the user is logged in, shows a page that links to other pages.
    """
    return TemplateResponse(request=request, template="index.html")

# URL /about, name "about"
@login_not_required
def about(request):
    """
    About page.
    Has a brief summary of what the website is for.
    """
    return TemplateResponse(request=request, template="about.html")
