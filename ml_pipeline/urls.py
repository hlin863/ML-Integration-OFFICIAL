from django.urls import path

from . import views

app_name = "ml_pipeline"

urlpatterns = [
    path("", views.training_runs, name="training_runs"),
    path("repositories/new/", views.repository_selection, name="repository_selection"),
    path("train/", views.enqueue_training_run, name="enqueue_training_run"),
]
