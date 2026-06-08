# Generated for the ML pipeline application.

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TrainingRun",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dataset_path", models.CharField(max_length=500)),
                ("git_sha", models.CharField(blank=True, max_length=40)),
                ("celery_task_id", models.CharField(blank=True, max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("running", "Running"),
                            ("success", "Success"),
                            ("failed", "Failed"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("metrics", models.JSONField(blank=True, default=dict)),
                ("artifacts", models.JSONField(blank=True, default=dict)),
                ("error_message", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("started_at", models.DateTimeField(blank=True, null=True)),
                ("finished_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.AddIndex(
            model_name="trainingrun",
            index=models.Index(
                fields=["status", "-created_at"],
                name="ml_pipeline_status_b39b80_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="trainingrun",
            index=models.Index(fields=["git_sha"], name="ml_pipeline_git_sha_c19e4b_idx"),
        ),
    ]
