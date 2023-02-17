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

    github_url = request.GET.get('git_link')

    output['text'] = github_url

    # return the HTTPResponse object as the workflow.html template after update
    return HttpResponse(output['text'])

    # return render(request, 'workflow/testfolder/workflow_temp.html', output)