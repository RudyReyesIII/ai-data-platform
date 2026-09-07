from pathlib import Path

import pandas as pd


def load_csv(file_path: Path) -> pd.DataFrame:
    if not file_path.exists():
        raise FileNotFoundError(f"Requested File Not Found: {file_path}")
    return pd.read_csv(file_path)


