from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Subdirectories
FIGURES_DIR = BASE_DIR / "figures"
DATA_DIR = BASE_DIR / "raw_data"
PROCESSED_DIR = BASE_DIR / "processed_data"
#TEST_DB_PATH = BASE_DIR / "may2025.db"  # if used in tests or dev
