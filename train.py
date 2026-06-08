import argparse
from pathlib import Path

from ml_pipeline.services.training import train_wine_quality_model


def main():
    parser = argparse.ArgumentParser(description="Train the wine quality model.")
    parser.add_argument(
        "--dataset",
        default="wine_quality.csv",
        help="Path to the training dataset CSV.",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Directory for metrics and plots.",
    )
    parser.add_argument(
        "--random-state",
        default=42,
        type=int,
        help="Random seed for deterministic train/test split and model training.",
    )
    args = parser.parse_args()

    result = train_wine_quality_model(
        dataset_path=args.dataset,
        output_dir=args.output_dir,
        random_state=args.random_state,
    )

    metrics_path = Path(result["artifacts"]["metrics"])
    print(metrics_path.read_text(encoding="utf-8").strip())
    print(f"Artifacts written to {result['output_dir']}")


if __name__ == "__main__":
    main()
