from dotenv import load_dotenv
from playhouse.sqlite_ext import PostgresqlDatabase
import os

load_dotenv()

db = PostgresqlDatabase(
    database=os.getenv('POSTGRES_DB_NAME'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),
    port=os.getenv('POSTGRES_PORT')
)
