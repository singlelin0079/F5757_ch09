DATABASE_URL = "sqlite:///tasks.db"
SECRET_KEY = "your-secret-key-here"
API_BASE_URL = "http://localhost:5000"
API_KEY = "sk-1234567890abcdef"
DEBUG = True
DEFAULT_USER = "admin"

class Config:
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = SECRET_KEY