import logging

from pipeline.config import INPUT_PATH, OUTPUT_PATH
from pipeline.ingest import load_csv
from pipeline.load import save_parquet
from pipeline.transform import transform_incidents
from pipeline.validate import (
    validate_columns,
    validate_not_null,
    validate_range,
    validate_unique_ids,
)

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def main() -> None:
    required_columns = {
        "incident_id",
        "district",
        "incident_type",
        "severity",
    }

    try:
        logger.info("Pipeline started")
        df = load_csv(INPUT_PATH)

        validate_columns(df, required_columns)
        validate_unique_ids(df, "incident_id")
        validate_not_null(
            df,
            {"incident_id", "district", "incident_type", "severity"},
        )
        validate_range(df, "severity", 0, 5)

        logger.info("Validation completed successfully")

        df = transform_incidents(df)

        save_parquet(df, OUTPUT_PATH)
        logger.info("Pipeline completed successfully")
    except Exception:
        logger.exception("Pipeline has failed")
        raise


if __name__ == "__main__":
    main()
