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

def validate_unique_ids(
    df: pd.DataFrame,
    id_column: str,
) -> None:

    duplicates = df[id_column].duplicated(keep=False)
    
    
    if duplicates.any():

        duplicate_ids = (
            df.loc[duplicates, id_column]
            .unique()
            .tolist()
        )
        raise ValueError(f"Duplicates found in {id_column}: {duplicate_ids}")

def validate_not_null(
        df: pd.DataFrame,
        columns: set[str],
) -> None:

    null_counts = (
        df[list(columns)]
        .isna()
        .sum()
    )

    null_counts = null_counts[null_counts > 0]

    if not null_counts.empty:
        raise ValueError(f"Null values found {null_counts.to_dict()}")

    
def validate_range(
    df: pd.DataFrame,
    column: str,
    min_value: float,
    max_value: float,
) -> None:
    invalid = (
        df.loc[
            (df[column] > max_value) | 
            (df[column] < min_value),
            column
        ]
    )

    if not invalid.empty:

        invalid_values = (invalid
                         .unique()
                         .tolist())
        
        raise ValueError(
            f"Values outside of range in {min_value} - {max_value} "
            f"in {column}: {invalid_values}"
            )

