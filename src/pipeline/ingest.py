from pathlib import Path
import pandas as pd
import logging

logger = logging.getLogger(__name__)


def load_csv(file_path: Path) -> pd.DataFrame:
    if not file_path.exists():
        raise FileNotFoundError(f"Requested File Not Found: {file_path}")

    df = pd.read_csv(file_path)
    logger.info("%s records loaded from %s",df.shape[0],file_path)
    return df


