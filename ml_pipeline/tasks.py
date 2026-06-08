from pathlib import Path

from celery import shared_task
from django.conf import settings

from .models import TrainingRun
from .services.training import train_wine_quality_model


@shared_task(bind=True, name="ml_pipeline.train_model")
def train_model_task(self, training_run_id, dataset_path=None):
    training_run = TrainingRun.objects.get(pk=training_run_id)
    if dataset_path:
        training_run.dataset_path = dataset_path
        training_run.save(update_fields=["dataset_path", "updated_at"])

    training_run.mark_running(task_id=self.request.id or "")
    output_dir = Path(settings.ML_ARTIFACT_DIR) / f"run-{training_run.pk}"

    try:
        result = train_wine_quality_model(
            dataset_path=training_run.dataset_path,
            output_dir=output_dir,
        )
    except Exception as exc:
        training_run.mark_failed(exc)
        raise

    training_run.mark_success(result)
    return result
