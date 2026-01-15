import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

password = quote_plus(DB_PASSWORD)   # converts @ to %40

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{password}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)