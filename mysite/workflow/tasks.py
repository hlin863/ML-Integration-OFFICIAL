from __future__ import absolute_import, unicode_literals

from celery import Celery
from celery import task
from celery.utils.log import get_task_logger

from models import ConfigurationForm
from django.core.mail import send_mail, BadHeaderError
from mysite.settings import DEFAULT_FROM_EMAIL
import os
import requests
import datetime
from subprocess import Popen, PIPE

# import the temproary directory
import tempfile
import shutil
import zipfile

# import pandas for data analysis and processing
import pandas as pd

app = Celery('github_tasks', broker='amqp://guest:guest@localhost:5672//')

logger = get_task_logger(__name__)


@task(name="send_email_task")
def send_email_task(subject, message, from_email, recipient_list):
    try:
        send_mail(subject, message, from_email, recipient_list)
    except BadHeaderError:
        return 'Invalid header found.'
    return None


def get_current_results(output_file, temp_dir):
    """

    This function loads the current results from the data output_file and stores them in the temp directory.

    Parameters
    ----------
    output_file : str
        The output file to load the results from.
    temp_dir : str
        The temporary directory to store the results in.
    """

    # parse the file to get the results
    with open(output_file, 'r') as f:
        results = f.read()

    # store the file in the temp directory

    return results


def github_repo_updated(github_repo):
    """
    1. Check if the github repo has been updated in the last 5 minutes.

    Parameters
    ----------
    github_repo : str
        The github repo to check for updates.

    Returns
    -------
    bool
        True if the github repo has been updated in the last 5 minutes, False otherwise.

    """
    # get the current time
    current_time = datetime.datetime.now()
    print("Current time: ", current_time)

    # get the time 5 minutes ago
    time_5_minutes_ago = current_time - datetime.timedelta(minutes=5)
    print("Time 5 minutes ago: ", time_5_minutes_ago)

    # get the time 5 minutes from now
    time_5_minutes_from_now = current_time + datetime.timedelta(minutes=5)
    print("Time 5 minutes from now: ", time_5_minutes_from_now)

    # get the time the github repo was last updated
    github_repo_last_updated = requests.get(github_repo).json()['updated_at']
    print("Github repo last updated: ", github_repo_last_updated)

    # check if the github repo has been updated in the last 5 minutes
    if time_5_minutes_ago < github_repo_last_updated < time_5_minutes_from_now:
        return True
    else:
        return False


def fetch_data_file(data_file, unzip_location):
    """

    This function fetches the data file from the data file url.

    Parameters
    ----------
    data_file : str
        The url of the data file to fetch.
    unzip_location : str
        The location to unzip the data file to.

    Returns
    -------

    """
    # check if the data type is file or from a url
    if data_file.startswith("http") or data_file.startswith("https"):
        print("The data file is from a url.")
        # get the data file from the url
        data_request = requests.get(data_file)

        return data_request.content  # return the data file content

    # otherwise if the data file is a path.
    elif data_file.startswith("C:\\"):
        path = data_file
        print("The data file is a path.")
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(unzip_location)

        # load the data fro the directory after extracting the zip file
        # if the data is a type csv file
        if data_file.endswith(".csv"):
            data = pd.read_csv(data_file)

            return data

    # copy file location to the current working directory
    shutil.copy(data_file, os.getcwd())


def data_files_updated(data_files):
    """
    1. Check if the data files have been updated in the last 5 minutes.

    Parameters
    ----------
    data_files : list
        A list of data files to check for updates.

    Returns
    -------
    bool
        True if the data files have been updated in the last 5 minutes, False otherwise.

    """
    # get the current time
    current_time = datetime.datetime.now()
    print("Current time: ", current_time)

    # get the time 5 minutes ago
    time_5_minutes_ago = current_time - datetime.timedelta(minutes=5)
    print("Time 5 minutes ago: ", time_5_minutes_ago)

    # get the time 5 minutes from now
    time_5_minutes_from_now = current_time + datetime.timedelta(minutes=5)
    print("Time 5 minutes from now: ", time_5_minutes_from_now)

    # check if the data files have been updated in the last 5 minutes
    for data_file in data_files:
        # get the time the data file was last updated
        data_file_last_updated = requests.get(data_file).json()['updated_at']
        print("Data file last updated: ", data_file_last_updated)

        if time_5_minutes_ago < data_file_last_updated < time_5_minutes_from_now:
            return True
        else:
            return False


@task(name="send_updates")
def send_updates(config_db):
    """

    1. Check if the github repo or the data files have been updated in the last 5 minutes.

    Parameters
    ----------
    gconfig_db: database key
        The database key for the config_db database for the row in the database. 

    """
    # allows the user to get the previous results.
    config_dict = ConfigurationForm.get(config_db)

    github_repo = config_dict['github_repo']

    data_files = config_dict['data_files']  # directory of the data files

    training_script = config_dict['training_script']

    output_file = config_dict['output_file']

    unzip_location = config_dict['unzip_location']

    print("Sending updates")
    # check if the github repo or the data files have been updated.
    if github_repo_updated(github_repo) or data_files_updated(data_files):
        print("Checking whether repo or data has been updated.")

        # if os.getcwd() != "C:\\Users\\haoch\\OneDrive\\Documents\\UCL\\COMPSI-Yr4\\Final_Year_Project\\OFFICIAL-REPO\\ML-Integration-OFFICIAL\\mysite\\workflow\\templates\Sources":

        #     # display the current working directory
        #     print("Current working directory: {0}".format(os.getcwd()))

        #     # change the current working directory to the templates folder
        #     os.chdir("workflow")

        #     os.chdir("templates")

        #     os.chdir("Sources")

        # define a temporary working directory
        temp_directory = tempfile.TemporaryDirectory()

        # change the current working directory to the temporary working directory
        os.chdir(temp_directory.name)

        # display the files in the Sources folder
        print("Files in Sources folder: ", os.listdir())

        # fetch the github repo code file and the data files as a zip file.
        github_repo_zip = f'{requests.get(github_repo)}/archive/refs/head/main.zip'

        # use request.get to fetch the zip file from the github repo
        zip_request = requests.get(github_repo_zip)

        # opens the zip file for processing.
        fhOut = open("github_repo.zip", "b")

        # check the status code of the request
        if zip_request.status_code == 200:

            # if the status code is 200, write the content of the request to the zip file
            fhOut.write(zip_request.content)

        # close the zip file
        fhOut.close()

        data_files = fetch_data_file(data_files, unzip_location)

        # run the training script
        if Popen(training_script, shell=True, stdout=PIPE, stderr=PIPE) == 0:

            print("Training script ran successfully.")

            # produce a file that contains the results of the ML training.

            # 1. getting the data from the previous ML training process
            previous_results = config_db.previous_results

            # 2. getting the data from the current ML training process
            current_results = get_current_results(output_file, temp_directory)

            # 3. comparing the results from the previous ML training process and the current ML training process
            if current_results < previous_results:
                # send an email to the user
                send_email_task(
                    "The training results are getting worse.", DEFAULT_FROM_EMAIL, [""])
            elif previous_results - 0.05 <= current_results <= previous_results + 0.05:
                send_email_task(
                    "The training results are the same.", DEFAULT_FROM_EMAIL, [""])
            else:
                # push the new model to the staging server and production server.
                send_email_task(
                    "The training results are getting better.", DEFAULT_FROM_EMAIL, [""])
        else:

            # send an email to the user
            send_email_task(
                "ML Training Failed", "The ML training failed. Please check the training script.", DEFAULT_FROM_EMAIL, [""])

            # destroy the temp directory
            temp_directory.cleanup()
