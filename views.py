# import peewee
# from models import Category , Product

# def get_categories():
#     return Category.select()

# def get_products():
#     return Product.select()


# def get_product_by_category_name(category_name):
#     """
#     получит все продукты оторые относяться к определенной 
#     категории
#     """
#     category = Category.get(name = category_name)
#     return category.categories


# def post_category(category_name):
#     try:
#         obj = Category(name=category_name.lower() )
#         obj.save()
#         print('Сохранено!')
#     except peewee.IntegrityError:
#         print('Такая категория существует')

# def post_product(product_name, product_price , category_name):
#     try:
#         category= Category.get(name = category_name)
#         obj = Product(
#         title= product_name , 
#         price= product_price , 
#         category= 1
#         )
#         obj.save()
#         print(category)
#         print('Сохранено')

        
#     except peewee.DoesNotExist:
#         print('Нет такой категории')

# def delete_category():
#     pass

# def delete_product(id_product):
#     try:
#         product = Product.get(id = id_product)
#         product.delete_instance()
#         print('Продукт удален ')
#     except peewee.DoesNotExist:
#         print('Такой продут не найден!')
# def update_category():
#     pass

# def update_product(id_product,**kwargs):
#     product = Product.update(**kwargs).where(Product.id == id_product)
#     product.execute()
#     print('Обновлено!!!!')

    

# class Solution:
#     def sum(self, num1: int, num2: int) -> int: 
#         return num1 + num2
       
# c = Solution()
# print(c.sum(1,2))




# class Solution:
#     def twoSum(self, nums, target: int):
#         dict={}
#         for i,n in enumerate(nums):
#             if n in dict:
#                 return dict[n],i
#             else:
#                 dict[target-n]=i
# s = Solution()
# print(s.twoSum (2,2))


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         for i in s:
#             return len(i)
        
# s = Solution()
# print(s.lengthOfLongestSubstring('sdsd'))


# class Mammal:
#     def move(self):
#         print('Двигается')

# class Hare(Mammal):
#     def move(self):
#         print('Прыгает')

# animal = Mammal()
# animal.move()
# hare = Hare()
# hare.move()

# class Parent():
#     def __init__(self):
#         print('Parent init')

#     def method(self):
#         print('Parent method')

# class Child(Parent):
#     def __init__(self):
#         Parent.__init__(self)

#     def method(self):

#         super(Child, self).method()

# child = Child()
# child.method()

# handle = open("output.txt", "w")
# handle.write("This is a test!")
# handle.close()

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x_str = str(x)
#         if x_str == x_str[::-1]:
#             return True
#         return False


# s = Solution()
# print(s.isPalindrome(12132))



class Solution:
    def romanToInt(self, s: str) -> int:
        I= 1
        V =5
        X=10
        L=50
        C=100
        D=500
        M=1000
        s = 'I'