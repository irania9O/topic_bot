
from .settings import POSTGRES_PASSWORD
from peewee import PostgresqlDatabase

database = PostgresqlDatabase(
    'postgres', 
    user='postgres', 
    password=POSTGRES_PASSWORD,
    host='localhost', 
    port=5432  
)
