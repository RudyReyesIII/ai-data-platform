import pandas as pd

def transform_incidents(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result['district'] = result['district'].str.strip()
    result['incident_type'] = result['incident_type'].str.strip()

    result['severity_label'] = (
        pd.cut(
            result['severity'],
            bins=[-1, 1, 3, 5],
            labels=["Low", "Medium", "High"]
        )
    )
    return result