from django.shortcuts import render
from django_unicorn.components import UnicornView

# Create your views here.
from django.http import HttpResponse

from .templates.Sources import *
import os

# from .templates import *

def index(request):
    # embed UnicornView in the template
    return render(request, 'workflow/workflow.html', {'unicorn_view': UnicornView})
    # return render(request, 'workflow/workflow.html')

def testbutton(request):
    if request.method == 'POST':
        
        username = request.POST.get('git_link')

        python_file_name = request.POST.get('python_file')

        password = request.POST.get('pwd')

        output = {'name': username}

        print("username: ", username)

        print("python_file_name: ", python_file_name)

        # display the current working directory
        print("Current working directory: {0}".format(os.getcwd()))

        # change the current working directory to the templates folder
        os.chdir("workflow")

        os.chdir("templates")

        os.chdir("Sources")

        # display the current working directory
        print("Current working directory: {0}".format(os.getcwd()))

        os.system("python " + python_file_name)

        # print("password: ", password)

        return render(request, 'workflow/workflow.html', output)

    # return the HTTPResponse object as the workflow.html template after update
    return render(request, 'workflow/workflow.html')

    # return render(request, 'workflow/testfolder/workflow_temp.html', output)