import pandas as pd

from pipeline.transform import transform_incidents


def test_transform_incidents_strips_whitespace() -> None:
    df = pd.DataFrame(
        {
            "incident_id": [1],
            "district": ["  San Antonio  "],
            "incident_type": ["  Vehicle  "],
            "severity": [2],
        }
    )

    result = transform_incidents(df)
    assert result.loc[0, "district"] == "San Antonio"
    assert result.loc[0, "incident_type"] == "Vehicle"


def test_transform_incidents_severity() -> None:
    df = pd.DataFrame(
        {
            "incident_id": [1, 2, 3, 4, 5, 6],
            "district": [
                "San Antonio",
                "Dallas",
                "Austin",
                "Houston",
                "Paris",
                "Atlanta",
            ],
            "incident_type": [
                "Vehicle",
                "Work Comp",
                "Liability",
                "Tort",
                "Vehicle",
                "Work Comp",
            ],
            "severity": [0, 1, 2, 3, 4, 5],
        }
    )

    result = transform_incidents(df)
    assert result["severity_label"].astype(str).tolist() == [
        "Low",
        "Low",
        "Medium",
        "Medium",
        "High",
        "High",
    ]


def test_transform_incidents_does_not_modify_input() -> None:
    df = pd.DataFrame(
        {
            "incident_id": [1],
            "district": ["  San Antonio  "],
            "incident_type": ["  Vehicle  "],
            "severity": [2],
        }
    )

    result = transform_incidents(df)
    assert df.loc[0, "district"] == "  San Antonio  "
    assert result.loc[0, "district"] == "San Antonio"
