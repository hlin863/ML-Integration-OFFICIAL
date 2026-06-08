from pathlib import Path
from tempfile import TemporaryDirectory

import pandas as pd
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import TrainingRun
from .services.training import train_wine_quality_model
from .tasks import train_model_task


class TrainingServiceTests(TestCase):
    def test_training_outputs_metrics_and_artifacts(self):
        with TemporaryDirectory() as temp_dir:
            dataset_path = Path(temp_dir) / "wine.csv"
            output_dir = Path(temp_dir) / "output"
            _write_dataset(dataset_path)

            result = train_wine_quality_model(dataset_path, output_dir)

            self.assertIn("test_variance_explained", result["metrics"])
            self.assertTrue(Path(result["artifacts"]["metrics"]).exists())
            self.assertTrue(Path(result["artifacts"]["feature_importance"]).exists())
            self.assertTrue(Path(result["artifacts"]["residuals"]).exists())


class TrainingTaskTests(TestCase):
    def test_task_updates_training_run(self):
        with TemporaryDirectory() as temp_dir:
            dataset_path = Path(temp_dir) / "wine.csv"
            artifact_dir = Path(temp_dir) / "artifacts"
            _write_dataset(dataset_path)
            run = TrainingRun.objects.create(dataset_path=str(dataset_path))

            with override_settings(
                ML_DATASET_PATH=str(dataset_path),
                ML_ARTIFACT_DIR=str(artifact_dir),
            ):
                result = train_model_task.apply(args=[run.pk]).get()

            run.refresh_from_db()
            self.assertEqual(run.status, TrainingRun.Status.SUCCESS)
            self.assertIn("training_variance_explained", run.metrics)
            self.assertEqual(run.metrics, result["metrics"])


class TrainingViewTests(TestCase):
    def test_training_runs_page_loads(self):
        response = self.client.get(reverse("ml_pipeline:training_runs"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Model Training Runs")


def _write_dataset(path):
    rows = []
    for index in range(40):
        rows.append(
            {
                "fixed acidity": 6.0 + index * 0.03,
                "volatile acidity": 0.2 + (index % 5) * 0.02,
                "citric acid": 0.1 + (index % 4) * 0.03,
                "residual sugar": 1.0 + (index % 7) * 0.2,
                "chlorides": 0.04 + (index % 3) * 0.01,
                "free sulfur dioxide": 10 + index,
                "total sulfur dioxide": 40 + index * 2,
                "density": 0.99 + index * 0.0001,
                "pH": 3.0 + (index % 6) * 0.02,
                "sulphates": 0.5 + (index % 4) * 0.01,
                "alcohol": 9.5 + (index % 8) * 0.1,
                "quality": 5 + (index % 3),
            }
        )
    pd.DataFrame(rows).to_csv(path, index=False)
