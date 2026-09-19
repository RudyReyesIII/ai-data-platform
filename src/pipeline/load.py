from pathlib import Path

import pandas as pd


def save_parquet(
    df: pd.DataFrame,
    file_path: Path,
) -> None:
    
    file_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(file_path, index=False)