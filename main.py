# # ORM (OBject  Reational mapping - объекто релеационное представление ) -
# # технология программирования , которая связывает базы данных с концепциями 
# # объектно - оренитрованных языков программирования Т.Е. ОРМ это прслойка между Бд
# # и кодом который пишет программист , которая позволяет созданные в программе объекты складывать / получать в/ их БД

# # КЛассы - Табуляция

# # Атрибуты класса - Поле

# # Объекты - строки в таблице БД  

# # from datetime import datetime
# # import peewee



# # db = peewee.PostgresqlDatabase(
# #     'py29_orm',
# #     user = 'rodion',
# #     password = '1',
# #     host = 'localhost',
# #     port=5432
# # )


# # class Category(peewee.Model):
# #     id = peewee.PrimaryKeyField(null=False)
# #     name = peewee.CharField(max_length=100, unique = True)
# #     created_at = peewee.DateTimeField(default= datetime.now())

# #     class Meta:
# #         database = db
# #         db_table = 'catigory'
# #         order_by = ('reated_ad',)


# # class Product (peewee.Model):
# #     id = peewee.PrimaryKeyField(null = False)
# #     title = peewee.CharField(max_length=100)
# #     price = peewee.DecimalField(max_digits=10 , decimal_places=2 , default = None)
# #     category = peewee.ForeignKeyField(
        
# #         Category, related_name= ' categories', to_field=id ,
# #         on_delete='cascade'
        
# #     )
# #     created_at = peewee.DateTimeField(default = datetime.now())

# #     class Meta:
# #         database = db
# #         db_table = 'product'
# #         order_by = ('created_at' , )

# # db.connect()
# # # Category.create_table()
# # # Product.create_table()

# # # obj = Category(name = 'sport')
# # # # obj.save()
# # # print(Category.select()[1].name)

# # def get_categories():
# #     for i in Category.select():
# #         print(f'{i.id} ----- {i.name} ----- {i.created_at}')


# # def get_products():
# #     for i in Product.select():
# #         print (f'{i.id} ----- {i.title} ----- {i.price} --- ---- {i.created_at}')
# # def post_category(name):
# #     Category(name= name).save()
# #     return 'created!'

# # def post_product(title , price , category):
# #     category = Category.select().where(Category.name == category)
# #     Product(title = title , price = price , category = category  ).save()
# #     return 'created!'


# # post_product('Product' , 101 , 'game')
# # # post_category('test')
# # get_products()
# # get_categories()



# from datetime import datetime
# import peewee


# db = peewee.PostgresqlDatabase(
#     'py30_orm',                      
#     user = 'rodion',
#     password = 1,
#     host = 'localhost',
#     port = 5432                                            
# )

# ORM (Object Reational mapping - обьектно реляционное представления) - технология программирования, которая связывает базы данных с концепциями обьектно-ориентированных языков прогаммирования. Т.е. ORM это прослойка между БД и кодом который пишет программист, которая позволяет созданные в программе обьекты складывать/получучать в/их БД 
# Классы - Таблица 
# Атрибуты класса - Поле
# Обьекты - Строки в таблице БД



##################################################

# from settings import db
# from models import Product , Category
# from views import *

# db.connect()
# # Category.create_table()
# # Product.create_table()

# for category in get_categories():
#     print(category.name)

# for product in get_products():
#     print(f'{product.title} ------- {product.category.name}')



# inser categories
# list_of_categories = ['game' , 'home' , 'sport' , 'school']
# for category in list_of_categories:
#     post_category(category)


# insert product 

# post_product('p1' , 100 , 'game' )
# post_product('p2' , 101 , 'home' )
# post_product('p3' , 102 , 'game' )
# post_product('p4' , 103 , 'sport')
# post_product('p5' , 104 , 'sport')


# obj = Category.get(name = 'game')
# for product in obj.categories:
#     print(product.title , product.category.name)



# for prodcut in get_product_by_category_name('game'):
#     print(f'{prodcut.title} ------- {prodcut.price}')



# delete_product(1)
# update_product(2, title= 'tesssssts')


class Makers:
    student_count = 0
    
    def __init__(self , name , language , kpi):
        self.name = name
        self.language = language
        self.kpi = kpi
    


    @classmethod
    def new_student(cls, name , language , kpi ):
        cls.student_count += 1
        return cls(name , language , kpi)
        

    
    def get_info(self):
        return f'Student name: {self.name}, Language: {self.language}'
    

    def set_kpi(self, kpi):
        self.kpi = kpi
        return kpi


student1 = Makers.new_student("Marat", "JS", '89')
student2 = Makers.new_student("Oleg", "Python", '55')

print(student1.set_kpi(89))
print(student1.get_info())
print(student2.set_kpi(89))
print(student2.get_info())
print(Makers.student_count)