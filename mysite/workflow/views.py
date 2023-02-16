from django.shortcuts import render
from django_unicorn.components import UnicornView

# Create your views here.
from django.http import HttpResponse

# from .templates import *

def index(request):
    # embed UnicornView in the template
    return render(request, 'workflow/workflow.html', {'unicorn_view': UnicornView})
    # return render(request, 'workflow/workflow.html')

def testbutton(request):
    output = {}

    output['text'] = "Hello World"

    return render(request, 'workflow/workflow_temp.html', output)