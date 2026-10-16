import os
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / '.env')

class Settings:
    app_name = 'PocketSmart AI'
    secret_key = os.getenv('SECRET_KEY', 'dev-only-change-me')
    database_path = str(ROOT / os.getenv('DATABASE_PATH', 'data/pocketsmart.db'))
    gemini_api_key = os.getenv('GEMINI_API_KEY', '').strip()
    gemini_model = os.getenv('GEMINI_MODEL', 'gemini-3.5-flash').strip()
    max_upload_mb = int(os.getenv('MAX_UPLOAD_MB', '5'))

settings = Settings()
Path(settings.database_path).parent.mkdir(parents=True, exist_ok=True)
