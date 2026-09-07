import pandas as pd
import pytest

from pipeline.validate import validate_columns
from pipeline.validate import validate_unique_ids
from pipeline.validate import validate_not_null
from pipeline.validate import validate_range

def test_validate_columns_accepts_valid_dataframe() -> None:
    df = pd.DataFrame(
        {
            "incident_id": [1, 2, 3],
            "district": ["San Antonio", "Austin", "Dallas"],
            "incident_type": ["Vehicle", "Injury", "Vehicle"],
            "severity": [2, 4, 1],
        }
    )

    required_columns = {
        "incident_id",
        "district",
        "incident_type",
        "severity",
    }

    validate_columns(df, required_columns)

def test_validate_columns_rejects_missing_column() -> None:
    df = pd.DataFrame(
        {
            "incident_id": [1, 2, 3],
            "district": ["San Antonio", "Austin", "Dallas"],
        }
    )

    required_columns = {
        "incident_id",
        "district",
        "severity",
    }

    with pytest.raises(ValueError):
        validate_columns(df, required_columns)

def test_validate_unique_ids_accept_unique_ids() -> None:
    df = pd.DataFrame(
        {'incident_id' : [1,2,3]}
    )

    validate_unique_ids(df, "incident_id")

def test_validate_unique_ids_rejects_duplicate_ids() -> None:
    df = pd.DataFrame(
        {'incident_id' : [1,2,2]}
    )

    with pytest.raises(ValueError):
        validate_unique_ids(df, "incident_id")

def test_validate_not_null_accepts_complete_data() -> None:
    df = pd.DataFrame(
        {
         'incident_id' : [1,2,3,4],
         'district' : ['San Antonio' ,'Austin' ,'Dallas' ,'El Paso']
         }
    )

    validate_not_null(df,{'incident_id','district'})




def test_validate_not_null_rejects_null_data() -> None:
    df = pd.DataFrame(
        {
            'incident_id' : [1,2,3,4],
            'district' : ['San Antonio' ,None ,'Dallas' ,'El Paso']
        }
    )

    with pytest.raises(ValueError):
        validate_not_null(df,{'incident_id','district'})


def test_validate_range_accepts_valid_values() -> None:
    df = pd.DataFrame(
        {
            'severity' : [1 ,2 ,3 ,4]
        }
    )

    validate_range(df,'severity',0,5)




def test_validate_range_rejects_invalid_values() -> None:
    df = pd.DataFrame(
        {
            'severity' : [1 ,-2 ,3 ,7]
        }
    )

    with pytest.raises(ValueError):
        validate_range(df,'severity',0,5)
        