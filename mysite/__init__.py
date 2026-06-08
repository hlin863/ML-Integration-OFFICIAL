# This makes sure the Celery app is imported when Django starts so shared_task
# decorators use the project Celery application.
from .celery import app as celery_app

__all__ = ('celery_app',)
