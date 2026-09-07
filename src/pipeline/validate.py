import pandas as pd


def validate_columns(
    df: pd.DataFrame,
    required_columns: set[str],
) -> None:
    missing_cols = required_columns - set(df.columns)


    if missing_cols:
        raise ValueError(
            f"Missing required columns: {sorted(missing_cols)}"
        )