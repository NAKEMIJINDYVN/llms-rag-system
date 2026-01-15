from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMP_DIR = BASE_DIR / "temp"

PATH_ETENSION = TEMP_DIR / "extension"

PATH_CHROMIUM = TEMP_DIR / "profile" / "chromium"
PATH_FIREFOX = TEMP_DIR / "profile" / "firefox"
PATH_WEBKIT = TEMP_DIR / "profile" / "webkit"

PATH_EXPORT  = TEMP_DIR / "export_data"
PATH_SCRAPER = TEMP_DIR / "scraper"
