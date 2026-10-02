import logging

from pipeline.config import INPUT_PATH, OUTPUT_PATH

from pipeline.ingest import load_csv
from pipeline.validate import validate_columns
from pipeline.validate import validate_unique_ids
from pipeline.validate import validate_not_null
from pipeline.validate import validate_range
from pipeline.transform import transform_incidents
from pipeline.load import save_parquet

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

def main() -> None:
    required_columns = {
    "incident_id",
    "district",
    "incident_type",
    "severity",
}

    df = load_csv(INPUT_PATH)

    validate_columns(df, required_columns)
    validate_unique_ids(df, "incident_id")
    validate_not_null(
        df,
        {"incident_id", "district", "incident_type", "severity"},
    )
    validate_range(df, 'severity', 0, 5)

    logger.info("Validation completed successfully")

    df = transform_incidents(df)

    save_parquet(df, OUTPUT_PATH)

if __name__ == "__main__":
    main()