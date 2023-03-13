from django.shortcuts import render
from django_unicorn.components import UnicornView
from django.core.mail import send_mail

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

def timestamp(request):
    # embed UnicornView in the template
    # automatically check if the python files in the Sources folder have been updated and get its time stamps
    # if the python files have been updated, then update the database
    # if the python files have not been updated, then do not update the database
    if os.getcwd() != "C:\\Users\\haoch\\OneDrive\\Documents\\UCL\\COMPSI-Yr4\\Final_Year_Project\\OFFICIAL-REPO\\ML-Integration-OFFICIAL\\mysite\\workflow\\templates\Sources":

        # display the current working directory
        print("Current working directory: {0}".format(os.getcwd()))

        # change the current working directory to the templates folder
        os.chdir("workflow")

        os.chdir("templates")

        os.chdir("Sources")

    # display the files in the Sources folder
    print("Files in Sources folder: ", os.listdir())

    # initialise the time when the website loaded up to compare with the last modified time of the python files
    application_time = datetime.datetime.now()

    # iterate through the files in the Sources folder
    for file in os.listdir():

        # check their last modified time
        # print("Last modified time: ", datetime.datetime.fromtimestamp(os.path.getmtime(file)))

        timestamp_time = datetime.datetime.fromtimestamp(os.path.getmtime(file))

        # check if the year of the last modified time is greater than the year of the time when the website loaded up
        if timestamp_time.year >= application_time.year:

            if timestamp_time.month >= application_time.month:

                # print("Test")

                if timestamp_time.day >= application_time.day:

                    if timestamp_time.hour >= application_time.hour:

                        print("File: ", file)

                        print("Last modified time: ", timestamp_time.time())  

                        os.system("python " + file)      

        # if timestamp_time > application_time:

        #     print("File: ", file)

        #     print("Last modified time: ", timestamp_time.time())

    return render(request, 'workflow/workflow.html', {'unicorn_view': UnicornView})
    
def testbutton(request):
    if request.method == 'POST':
        
        username = request.POST.get('git_link')

        python_file_name = request.POST.get('python_file')

        user_email = request.POST.get('user_email')

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
        print("Start time: ", start_time)

        os.system("python " + python_file_name)
        
        # get the time after the python file has been executed
        end_time = datetime.datetime.now()
        print("End time: ", end_time)

        table_model = WorkFlowData(task_name=python_file_name, start_time=start_time, end_time=end_time, completed="True")
        
        # insert the row "table_model" into the table "WorkFlowData"
        print("table_model: ", table_model.task_name)

        table_model.save()

        workflows = WorkFlowData.objects.all().values()

        output['workflows'] = workflows
        
        # print("password: ", password)

        send_mail(
            'Your workflow has been completed',
            'Here is the message.',
            'haochenglin789@gmail.com',
            [user_email],
            fail_silently=False,
        )

        return render(request, 'workflow/workflow.html', output)

    # return the HTTPResponse object as the workflow.html template after update
    return render(request, 'workflow/workflow.html')

    # return render(request, 'workflow/testfolder/workflow_temp.html', output)