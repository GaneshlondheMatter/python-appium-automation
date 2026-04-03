import psycopg2
from db_config_prod import DBConfig   # 👈 changed to prod config

class DBConnection:

    @staticmethod
    def get_connection():
        try:
            connection = psycopg2.connect(
                host=DBConfig.HOST,
                port=DBConfig.PORT,
                database=DBConfig.DATABASE,
                user=DBConfig.USER,
                password=DBConfig.PASSWORD,
                sslmode=DBConfig.SSLMODE,   # 👈 enabled for prod (Azure required)
                connect_timeout=10,
            )

            print("✅ PROD DB Connected Successfully")
            return connection

        except Exception as e:
            print(f"❌ PROD Database connection failed: {e}")
            raise