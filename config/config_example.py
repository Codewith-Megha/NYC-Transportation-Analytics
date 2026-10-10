"""
Project configuration.

Local use:   cp config/config_example.py config/config.py   (then edit if needed)
Docker / CI: values are read from environment variables, so no secrets are
             committed. The defaults below match a local PostgreSQL install.
"""
import os
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Data folders
RAW_DATA = BASE_DIR / "data" / "raw"
CLEAN_DATA = BASE_DIR / "data" / "cleaned"
PROCESSED_DATA = BASE_DIR / "data" / "processed"
EXPORT_DATA = BASE_DIR / "data" / "exports"

# PostgreSQL (override with environment variables)
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "transportation_analytics")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "YOUR_PASSWORD")
