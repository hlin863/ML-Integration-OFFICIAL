from django.db import models
from django.utils import timezone


class TrainingRun(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        RUNNING = "running", "Running"
        SUCCESS = "success", "Success"
        FAILED = "failed", "Failed"

    dataset_path = models.CharField(max_length=500)
    git_sha = models.CharField(max_length=40, blank=True)
    celery_task_id = models.CharField(max_length=255, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    metrics = models.JSONField(default=dict, blank=True)
    artifacts = models.JSONField(default=dict, blank=True)
    error_message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    started_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["status", "-created_at"]),
            models.Index(fields=["git_sha"]),
        ]

    def mark_running(self, task_id=""):
        self.status = self.Status.RUNNING
        self.started_at = timezone.now()
        if task_id:
            self.celery_task_id = task_id
        self.save(update_fields=["status", "started_at", "celery_task_id", "updated_at"])

    def mark_success(self, result):
        self.status = self.Status.SUCCESS
        self.metrics = result.get("metrics", {})
        self.artifacts = result.get("artifacts", {})
        self.error_message = ""
        self.finished_at = timezone.now()
        self.save(
            update_fields=[
                "status",
                "metrics",
                "artifacts",
                "error_message",
                "finished_at",
                "updated_at",
            ]
        )

    def mark_failed(self, error):
        self.status = self.Status.FAILED
        self.error_message = str(error)
        self.finished_at = timezone.now()
        self.save(update_fields=["status", "error_message", "finished_at", "updated_at"])

    def __str__(self):
        return f"TrainingRun #{self.pk} ({self.status})"
