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
    if request.method == 'POST':
        
        username = request.POST.get('git_link')

        password = request.POST.get('pwd')

        output = {'name': username, 'pwd': password}

        print("username: ", username)

        print("password: ", password)

        return render(request, 'workflow/workflow.html', output)

    # return the HTTPResponse object as the workflow.html template after update
    return render(request, 'workflow/workflow.html')

    # return render(request, 'workflow/testfolder/workflow_temp.html', output)