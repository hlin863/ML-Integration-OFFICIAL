from django.shortcuts import render
from django_unicorn.components import UnicornView

# Create your views here.
from django.http import HttpResponse

from .templates.Sources import *
import os
# import datetime
import datetime

from .models import WorkFlowData

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

        # resets the os directory to the current working directory
        # check if the current working directory is the same as the templates folder
        if os.getcwd() != "C:\\Users\\haoch\\OneDrive\\Documents\\UCL\\COMPSI-Yr4\\Final_Year_Project\\OFFICIAL-REPO\\ML-Integration-OFFICIAL\\mysite\\workflow\\templates\Sources":

            # display the current working directory
            print("Current working directory: {0}".format(os.getcwd()))

            # change the current working directory to the templates folder
            os.chdir("workflow")

            os.chdir("templates")

            os.chdir("Sources")

        # display the current working directory
        print("Current working directory: {0}".format(os.getcwd()))

        # get the current time
        start_time = datetime.datetime.now()

        # print the current time
        print("Current time: ", start_time)

        os.system("python " + python_file_name)
        
        # get the time after the python file has been executed
        end_time = datetime.datetime.now()
        print("Current time: ", end_time)

        table_model = WorkFlowData(task_name=python_file_name, start_time=start_time, end_time=end_time, completed="True")
        
        # insert the row "table_model" into the table "WorkFlowData"
        print("table_model: ", table_model.task_name)

        table_model.save()

        workflows = WorkFlowData.objects.all().values()

        output['workflows'] = workflows
        
        # print("password: ", password)

        return render(request, 'workflow/workflow.html', output)

    # return the HTTPResponse object as the workflow.html template after update
    return render(request, 'workflow/workflow.html')

    # return render(request, 'workflow/testfolder/workflow_temp.html', output)