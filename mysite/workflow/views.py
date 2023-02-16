from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .templates import *

def index(request):
    # return the HTTP response as html code from templates/index.html
    return render(request, 'workflow/workflow.html')
    # return HttpResponse("Hello, world. You're at the polls index.")
