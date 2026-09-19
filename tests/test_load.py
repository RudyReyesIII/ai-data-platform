import pandas as pd
from pipeline.load import save_parquet


def test_save_parquet_creates_file(tmp_path) -> None:
    df = pd.DataFrame(
        {
            "incident_id": [1],
            "district": ["San Antonio"],
            "incident_type": ["Vehicle"],
            "severity": [2],
        }
    )

    output_path = tmp_path / "cleaned.parquet"

    save_parquet(df, output_path)

    assert output_path.exists()

def test_save_parquet_preserves_data(tmp_path) -> None:
    df = pd.DataFrame(
        {
            "incident_id": [1],
            "district": ["San Antonio"],
            "incident_type": ["Vehicle"],
            "severity": [2],            
        }
    )

    output_path = tmp_path / "cleaned.parquet"

    save_parquet(df, output_path)

    loaded_df = pd.read_parquet(output_path)

    assert df.equals(loaded_df)

