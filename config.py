import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    DATABASE_CONFIG = {
        'user': os.environ.get('DB_USER') or 'root',
        'password': os.environ.get('DB_PASSWORD') or 'Ma-294022275',
        'host': os.environ.get('DB_HOST') or 'localhost',
        'database': os.environ.get('DB_NAME') or 'myblog'
    }