import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    DATABASE_CONFIG = {
        'user': 'root',
        'password': 'Ma-294022275',
        'host': 'localhost',
        'database': 'myblog'
    }