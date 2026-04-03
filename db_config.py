import os
from dotenv import load_dotenv

load_dotenv()

class DBConfig:
    # ✅ SSH tunnel → always localhost
    # HOST = "localhost"
    HOST = "matter-orbit-postgresql.postgres.database.azure.com"
    PORT = 5432
    # ✅ DB details from .env
    # DATABASE = os.getenv("DB_NAME", "orbit_qa_server")
    DATABASE = os.getenv("DB_NAME", "oribitauthprod")
    #  username 
    # USER = os.getenv("DB_USER", "matmot_bk_user")
    USER = os.getenv("DB_USER", "mmw_read_access")
    # Password 
    PASSWORD = os.getenv("DB_PASSWORD")
    # ✅ Required for Azure PostgreSQL
    # SSLMODE = "require"