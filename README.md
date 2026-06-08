# ML CI Django Application

This project is a Django application for continuous integration of a machine
learning workflow. It uses the wine quality dataset as the sample model target,
Celery for asynchronous training jobs, and GitHub Actions to test the Django app
and retrain the model whenever application code, training code, dependencies, or
datasets change.

## Project Structure

- `mysite/` - Django project settings, URLs, WSGI, and Celery application setup.
- `blog/` - Existing educational UI pages for the CI/ML introduction.
- `ml_pipeline/` - ML workflow app with training run models, Celery tasks,
  training services, tests, views, and templates.
- `train.py` - Command-line entry point used by CI to train the model.
- `wine_quality.csv` - Sample dataset used by the model training workflow.
- `.github/workflows/ci.yml` - GitHub Actions pipeline for Django and model tests.

## Local Development

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start Django:

```bash
python manage.py runserver
```

Open the training UI at:

```text
http://127.0.0.1:8000/ml/
```

## Celery Task Queue

Celery uses RabbitMQ by default:

```bash
celery -A mysite worker --loglevel=info
```

The broker can be changed with:

```bash
CELERY_BROKER_URL=amqp://guest:guest@localhost:5672//
```

For local development without manual setup, run the full stack:

```bash
docker compose up --build
```

This starts Django, a Celery worker, and RabbitMQ.

## Model Training

Run the model training workflow directly:

```bash
python train.py --dataset wine_quality.csv --output-dir artifacts/local
```

The command writes:

- `metrics.txt`
- `feature_importance.png`
- `residuals.png`

The Django app stores queued training runs in `ml_pipeline.TrainingRun`,
including status, Git SHA, metrics, errors, and artifact paths.

## Continuous Integration

GitHub Actions runs on pushes and pull requests to `main` when relevant files
change:

- Python source files
- `requirements.txt`
- `wine_quality.csv`
- files under `data/` or `datasets/`
- the CI workflow itself

The CI pipeline runs:

```bash
python manage.py check
python manage.py test
python train.py --dataset wine_quality.csv --output-dir artifacts/ci
```

Model metrics and generated plots are uploaded as workflow artifacts.
