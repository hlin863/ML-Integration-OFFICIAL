from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


def train_wine_quality_model(dataset_path, output_dir, random_state=42):
    dataset_path = Path(dataset_path).resolve()
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    dataframe = pd.read_csv(dataset_path)
    if "quality" not in dataframe.columns:
        raise ValueError("Dataset must contain a 'quality' target column.")

    features = dataframe.drop(columns=["quality"])
    target = dataframe["quality"]
    x_train, x_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.2,
        random_state=random_state,
    )

    model = RandomForestRegressor(max_depth=2, random_state=random_state)
    model.fit(x_train, y_train)

    train_score = float(model.score(x_train, y_train) * 100)
    test_score = float(model.score(x_test, y_test) * 100)
    metrics = {
        "training_variance_explained": round(train_score, 4),
        "test_variance_explained": round(test_score, 4),
    }

    metrics_path = output_dir / "metrics.txt"
    metrics_path.write_text(
        "Training variance explained: %2.1f%%\n"
        "Test variance explained: %2.1f%%\n" % (train_score, test_score),
        encoding="utf-8",
    )

    feature_importance_path = output_dir / "feature_importance.png"
    _plot_feature_importance(model, features.columns, feature_importance_path)

    residuals_path = output_dir / "residuals.png"
    _plot_residuals(model, x_test, y_test, residuals_path, random_state)

    return {
        "dataset_path": str(dataset_path),
        "output_dir": str(output_dir),
        "metrics": metrics,
        "artifacts": {
            "metrics": str(metrics_path),
            "feature_importance": str(feature_importance_path),
            "residuals": str(residuals_path),
        },
    }


def _plot_feature_importance(model, feature_names, output_path):
    feature_df = pd.DataFrame(
        {
            "feature": feature_names,
            "importance": model.feature_importances_,
        }
    ).sort_values(by="importance", ascending=False)

    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="importance", y="feature", data=feature_df, ax=ax)
    ax.set_xlabel("Importance", fontsize=14)
    ax.set_ylabel("Feature", fontsize=14)
    ax.set_title("Random forest feature importance", fontsize=16)
    fig.tight_layout()
    fig.savefig(output_path, dpi=120)
    plt.close(fig)


def _plot_residuals(model, x_test, y_test, output_path, random_state):
    rng = np.random.default_rng(random_state)
    y_pred = model.predict(x_test) + rng.normal(0, 0.25, len(y_test))
    y_jitter = y_test.to_numpy() + rng.normal(0, 0.25, len(y_test))
    residual_df = pd.DataFrame({"true": y_jitter, "pred": y_pred})

    fig, ax = plt.subplots(figsize=(6, 6))
    sns.scatterplot(x="true", y="pred", data=residual_df, ax=ax)
    ax.set_aspect("equal")
    ax.set_xlabel("True wine quality", fontsize=14)
    ax.set_ylabel("Predicted wine quality", fontsize=14)
    ax.set_title("Residuals", fontsize=16)
    ax.plot([1, 10], [1, 10], "black", linewidth=1)
    ax.set_ylim((2.5, 8.5))
    ax.set_xlim((2.5, 8.5))
    fig.tight_layout()
    fig.savefig(output_path, dpi=120)
    plt.close(fig)
