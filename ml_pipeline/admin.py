from django.contrib import admin

from .models import TrainingRun


@admin.register(TrainingRun)
class TrainingRunAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "status",
        "dataset_path",
        "git_sha",
        "created_at",
        "finished_at",
    )
    list_filter = ("status", "created_at")
    search_fields = ("dataset_path", "git_sha", "celery_task_id")
    readonly_fields = ("created_at", "updated_at", "started_at", "finished_at")
