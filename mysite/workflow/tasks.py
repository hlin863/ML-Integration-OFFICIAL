from __future__ import absolute_import, unicode_literals

from celery import Celery
from celery import task
from celery.utils.log import get_task_logger

from django.core.mail import send_mail, BadHeaderError
from mysite.settings import DEFAULT_FROM_EMAIL

app = Celery('github_tasks',broker='amqp://guest:guest@localhost:5672//')

logger = get_task_logger(__name__)

@task(name="send_email_task")
def send_email_task(subject, message, from_email, recipient_list):
    try:
        send_mail(subject, message, from_email, recipient_list)
    except BadHeaderError:
        return 'Invalid header found.'
    return None