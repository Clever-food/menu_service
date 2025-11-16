from playhouse.sqlite_ext import PostgresqlDatabase
from src.config.config import settings

db = PostgresqlDatabase(
    database=settings.POSTGRES_DB_NAME,
    user=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_HOST,
    port=settings.POSTGRES_PORT,
)

