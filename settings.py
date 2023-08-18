from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'py29_orm',
    user='rodion',
    password='1',
    host='localhost',
    port=5432
)
