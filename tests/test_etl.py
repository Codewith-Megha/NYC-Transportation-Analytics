"""Unit tests for the ETL transform steps (no database or parquet files needed)."""
import pandas as pd
import pytest

from src.etl.cleaning import clean_dataset
from src.etl.feature_engineering import engineer_features
from src.etl.standardize import standardize_columns
from src.etl.validation import REQUIRED_COLUMNS, validate_dataframe


def _yellow_rows():
    base = {
        "passenger_count": float("nan"),
        "trip_distance": 5.0,
        "ratecode_id": float("nan"),
        "store_and_fwd_flag": None,
        "congestion_surcharge": float("nan"),
        "airport_fee": float("nan"),
    }
    rows = [
        # valid trip, 30 minutes, with nulls that cleaning should fill
        {**base, "pickup_datetime": "2026-02-03 08:00", "dropoff_datetime": "2026-02-03 08:30"},
        # exact duplicate of the first row
        {**base, "pickup_datetime": "2026-02-03 08:00", "dropoff_datetime": "2026-02-03 08:30"},
        # dropoff before pickup
        {**base, "pickup_datetime": "2026-02-03 09:00", "dropoff_datetime": "2026-02-03 08:00"},
        # outside the 2026-01-01 to 2026-06-01 window
        {**base, "pickup_datetime": "2025-12-31 10:00", "dropoff_datetime": "2025-12-31 10:20"},
        # zero-length trip
        {**base, "pickup_datetime": "2026-03-01 10:00", "dropoff_datetime": "2026-03-01 10:00"},
    ]
    df = pd.DataFrame(rows)
    df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
    df["dropoff_datetime"] = pd.to_datetime(df["dropoff_datetime"])
    return df


def test_yellow_cleaning_drops_bad_rows_and_fills_nulls():
    out = clean_dataset(_yellow_rows(), "yellow")

    assert len(out) == 1
    row = out.iloc[0]
    assert row["trip_duration_minutes"] == pytest.approx(30.0)
    assert row["passenger_count"] == 1
    assert row["ratecode_id"] == 1
    assert row["store_and_fwd_flag"] == "N"
    assert row["congestion_surcharge"] == 0
    assert row["airport_fee"] == 0


def test_fhv_cleaning_requires_one_location_and_fills_base_number():
    df = pd.DataFrame(
        {
            "pickup_datetime": pd.to_datetime(["2026-01-10 10:00"] * 3),
            "dropoff_datetime": pd.to_datetime(["2026-01-10 10:20"] * 3),
            "pulocationid": [float("nan"), 12.0, 40.0],
            "dolocationid": [float("nan"), float("nan"), 41.0],
            "affiliated_base_number": [None, None, "B00001"],
        }
    )

    out = clean_dataset(df, "fhv")

    # first row has both locations missing, so it is removed
    assert len(out) == 2
    assert list(out["affiliated_base_number"]) == ["Unknown", "B00001"]


def test_standardize_renames_yellow_columns():
    df = pd.DataFrame(
        columns=["VendorID", "tpep_pickup_datetime", "PULocationID", "Airport_fee"]
    )

    out = standardize_columns(df, "yellow")

    assert list(out.columns) == [
        "vendor_id",
        "pickup_datetime",
        "pulocationid",
        "airport_fee",
    ]


def test_feature_engineering_time_flags_speed_and_category():
    df = pd.DataFrame(
        {
            # Saturday 08:15 and Wednesday 13:00
            "pickup_datetime": pd.to_datetime(["2026-03-07 08:15", "2026-03-04 13:00"]),
            "trip_duration_minutes": [30.0, 12.0],
            "trip_distance": [5.0, 1.0],
        }
    )

    out = engineer_features(df)

    assert list(out["pickup_hour"]) == [8, 13]
    assert list(out["pickup_day"]) == [7, 4]
    assert list(out["pickup_month"]) == [3, 3]
    assert list(out["pickup_weekday"]) == ["Saturday", "Wednesday"]
    assert list(out["is_weekend"]) == [True, False]
    assert list(out["rush_hour"]) == [True, False]
    assert out["average_speed_mph"].astype(float).tolist() == pytest.approx([10.0, 5.0])
    assert list(out["trip_category"]) == ["Medium", "Short"]


def test_trip_category_labels_zero_negative_and_missing_distance():
    df = pd.DataFrame(
        {
            "pickup_datetime": pd.to_datetime(["2026-03-04 13:00"] * 5),
            "trip_duration_minutes": [10.0] * 5,
            "trip_distance": [0.0, 1.5, 12.0, -1.0, float("nan")],
        }
    )

    out = engineer_features(df)

    assert list(out["trip_category"]) == [
        "Zero distance",
        "Short",
        "Long",
        "Unknown",
        "Unknown",
    ]


def _valid_frame():
    return pd.DataFrame(
        {
            "pickup_datetime": pd.to_datetime(["2026-02-03 08:00"]),
            "dropoff_datetime": pd.to_datetime(["2026-02-03 08:30"]),
            "trip_duration_minutes": [30.0],
            "pickup_hour": [8],
            "pickup_day": [3],
            "pickup_month": [2],
            "pickup_weekday": ["Tuesday"],
            "is_weekend": [False],
            "rush_hour": [True],
        }
    )


def test_validation_accepts_valid_frame():
    validate_dataframe(_valid_frame())


def test_validation_rejects_missing_column():
    df = _valid_frame().drop(columns=[REQUIRED_COLUMNS[-1]])
    with pytest.raises(ValueError, match="Missing required columns"):
        validate_dataframe(df)


def test_validation_rejects_negative_duration():
    df = _valid_frame()
    df["trip_duration_minutes"] = [-1.0]
    with pytest.raises(ValueError, match="Negative trip duration"):
        validate_dataframe(df)


def test_validation_rejects_null_pickup():
    df = _valid_frame()
    df["pickup_datetime"] = pd.to_datetime([None])
    with pytest.raises(ValueError, match="NULL"):
        validate_dataframe(df)
