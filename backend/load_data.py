import pandas as pd
from backend.db_connection import engine
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent   # Nutri-Fit-Insight folder
DATA_DIR = BASE_DIR / "data"

def load_users():
    df = pd.read_csv(DATA_DIR / "users.csv")
    df.to_sql("user_profile", engine, if_exists="append", index=False)

def load_activity():
    df = pd.read_csv(DATA_DIR / "daily_activity.csv")
    df.to_sql("daily_activity", engine, if_exists="append", index=False)

def load_nutrition():
    df = pd.read_csv(DATA_DIR / "nutrition.csv")
    df.to_sql("nutrition_log", engine, if_exists="append", index=False)

if __name__ == "__main__":
    load_users()
    load_activity()
    load_nutrition()
    print("All data loaded successfully")