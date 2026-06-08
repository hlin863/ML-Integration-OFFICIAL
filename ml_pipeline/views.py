from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .models import TrainingRun
from .services.version_control import current_git_sha
from .tasks import train_model_task


def training_runs(request):
    runs = TrainingRun.objects.all()[:20]
    return render(
        request,
        "ml_pipeline/training_runs.html",
        {
            "runs": runs,
            "default_dataset_path": settings.ML_DATASET_PATH,
        },
    )


@require_POST
def enqueue_training_run(request):
    dataset_path = request.POST.get("dataset_path") or settings.ML_DATASET_PATH
    run = TrainingRun.objects.create(
        dataset_path=dataset_path,
        git_sha=current_git_sha(),
    )
    async_result = train_model_task.delay(run.pk)
    run.celery_task_id = async_result.id or ""
    run.save(update_fields=["celery_task_id", "updated_at"])
    messages.success(request, f"Queued training run #{run.pk}.")
    return redirect("ml_pipeline:training_runs")
