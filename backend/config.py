import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ENV_PATH = os.path.join(BASE_DIR, "..", ".env")
if os.path.exists(ENV_PATH):
    load_dotenv(ENV_PATH)

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "app.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MIKROTIK_HOST = os.getenv("MIKROTIK_HOST")
    MIKROTIK_PORT = int(os.getenv("MIKROTIK_PORT", "8728"))
    MIKROTIK_USER = os.getenv("MIKROTIK_USER")
    MIKROTIK_PASSWORD = os.getenv("MIKROTIK_PASSWORD")
