import pandas as pd

class DataValidationError(Exception):
    pass


def validate_users(df: pd.DataFrame):
    required_cols = {
        "user_id", "full_name", "age", "gender",
        "height_cm", "weight_kg", "activity_level"
    }

    if not required_cols.issubset(df.columns):
        raise DataValidationError("Missing columns in users.csv")

    if not df["user_id"].is_unique:
        raise DataValidationError("Duplicate user_id found")

    if not df["age"].between(10, 100).all():
        raise DataValidationError("Invalid age values")

    if not df["weight_kg"].between(30, 300).all():
        raise DataValidationError("Invalid weight values")


def validate_activity(df: pd.DataFrame):
    if (df["steps"] < 0).any():
        raise DataValidationError("Negative steps detected")

    if (df["workout_minutes"] < 0).any():
        raise DataValidationError("Negative workout minutes detected")


def validate_nutrition(df: pd.DataFrame):
    numeric_cols = [
        "calories_consumed", "protein_g", "carbs_g",
        "fats_g", "fiber_g", "water_liters"
    ]

    for col in numeric_cols:
        if (df[col] < 0).any():
            raise DataValidationError(f"Negative values in {col}")