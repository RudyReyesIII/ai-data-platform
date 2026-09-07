from pathlib import Path

from pipeline.ingest import load_csv
from pipeline.validate import validate_columns
from pipeline.validate import validate_unique_ids


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

    print(df)




if __name__ == "__main__":
    main()