import peewee
from datetime import datetime
from settings import db


class Category(peewee.Model):
    id = peewee.PrimaryKeyField(null=False)
    name = peewee.CharField(max_length=100, unique=True)
    created_at = peewee.DateTimeField(default=datetime.now())
    
    class Meta:
        database = db
        db_table = 'category'
        order_by = ('created_at', )


class Product(peewee.Model):
    id = peewee.PrimaryKeyField(null=False)
    title = peewee.CharField(max_length=100)
    price = peewee.DecimalField(max_digits=10, decimal_places=2, default=None)
    category = peewee.ForeignKeyField(Category, related_name='categories',to_field='id', on_delete='cascade')
    created_at = peewee.DateTimeField(default=datetime.now())
    
    class Meta:
        database = db
        db_table = 'product'
        order_by = ('created_at',)

