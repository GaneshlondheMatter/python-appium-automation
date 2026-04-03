import os
from dotenv import load_dotenv

load_dotenv(".env.prod")

class DBConfig:
    HOST = os.getenv("DB_HOST")
    PORT = int(os.getenv("DB_PORT", 5432))
    DATABASE = os.getenv("DB_NAME")
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    SSLMODE = os.getenv("DB_SSLMODE", "require")