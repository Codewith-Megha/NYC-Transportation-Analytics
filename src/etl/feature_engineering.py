"""
Feature engineering for NYC Transportation Analytics.
"""

import numpy as np
import pandas as pd

from src.logger import logger


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create analytical features.
    """

    logger.info("Creating features...")

    # -------------------------------
    # Date & Time Features
    # -------------------------------

    df["pickup_hour"] = df["pickup_datetime"].dt.hour

    df["pickup_day"] = df["pickup_datetime"].dt.day

    df["pickup_month"] = df["pickup_datetime"].dt.month

    df["pickup_weekday"] = df["pickup_datetime"].dt.day_name()

    df["is_weekend"] = (
        df["pickup_datetime"].dt.weekday >= 5
    )

    # -------------------------------
    # Rush Hour
    # -------------------------------

    df["rush_hour"] = df["pickup_hour"].between(7, 10) | \
                      df["pickup_hour"].between(16, 19)

    # -------------------------------
    # Speed
    # -------------------------------

    if "trip_distance" in df.columns:

        hours = df["trip_duration_minutes"] / 60

        hours = (df["trip_duration_minutes"] / 60).replace(0, pd.NA)

        df["average_speed_mph"] = (
        df["trip_distance"] / hours
        ).fillna(0)

        df["average_speed_mph"] = (
            df["average_speed_mph"]
            .replace([float("inf"), -float("inf")], 0)
        )

    # -------------------------------
    # Trip Category
    # -------------------------------

    if "trip_distance" in df.columns:

        distance = df["trip_distance"]

        # Zero-distance trips get their own label instead of a silent null;
        # negative or missing distances are marked Unknown.
        df["trip_category"] = np.select(
            [
                distance == 0,
                (distance > 0) & (distance <= 2),
                (distance > 2) & (distance <= 10),
                distance > 10,
            ],
            ["Zero distance", "Short", "Medium", "Long"],
            default="Unknown",
        )

    logger.info("Feature engineering completed")

    return df