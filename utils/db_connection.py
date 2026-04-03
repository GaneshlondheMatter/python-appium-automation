import psycopg2
from db_config import DBConfig

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
                # sslmode=DBConfig.SSLMODE,
                connect_timeout=10,
            )

            print("✅ DB Connected Successfully")
            return connection

        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            raise