"""

Render the html template index.html with the data in the context variable.

"""
from django.http import HttpResponse

HTML_CODE = """

    <h1>My First Django App</h1>

"""

def home(request):
    """
    
    Render the html template index.html with the data in the context variable.

    Input: request (HttpRequest)

    Output: response (html template)

    """
    return HttpResponse(HTML_CODE)