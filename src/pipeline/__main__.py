from pathlib import Path

from pipeline.ingest import load_csv
from pipeline.validate import validate_columns
from pipeline.validate import validate_unique_ids
from pipeline.validate import validate_not_null
from pipeline.validate import validate_range
from pipeline.transform import transform_incidents
from pipeline.load import save_parquet


def main() -> None:
    required_columns = {
    "incident_id",
    "district",
    "incident_type",
    "severity",
}

    df = load_csv(Path("data/raw/incidents.csv"))

    validate_columns(df, required_columns)
    validate_unique_ids(df, "incident_id")
    validate_not_null(
        df,
        {"incident_id", "district", "incident_type", "severity"},
    )
    validate_range(df, 'severity', 0, 5)

    df = transform_incidents(df)

    save_parquet(df, Path("data/processed/cleaned.parquet"))

if __name__ == "__main__":
    main()