
from .settings import POSTGRES_PASSWORD
from peewee import PostgresqlDatabase, SqliteDatabase

database = SqliteDatabase("test.sql") 
# PostgresqlDatabase(
#     'postgres', 
#     user='postgres', 
#     password=POSTGRES_PASSWORD,
#     host='localhost', 
#     port=5432  
# )
