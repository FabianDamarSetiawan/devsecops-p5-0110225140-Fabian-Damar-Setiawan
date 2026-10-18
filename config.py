import os

class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "default-insecure-key")
    DATABASE_URI = "sqlite:///app.db"