# cook your dish here
# class Account:
#     def __init__(self, balance):
#         self.__balance = balance
        
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#              self.__balance -= amount
#         else:
#             print("Insufficent balance")
    
#     def deposite(self, amount):
#         self.__balance += amount
        
#     def display(self):
#         return self.__balance
        
# acc = Account(100000)
# acc.withdraw(21050)
# acc.deposite(500)
# print("Account current balance is:",acc.display())

# from abc import abstractmethod

# class shape:
#     @abstractmethod
#     def area(self):
#         pass
    
# class Rectangle(shape):
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
        
#     def area(self):
#         return self.width * self.height
        
# class Circle(shape):
#     def __init__(self, radius):
#         self.radius = radius
        
#     def area(self):
#         return 3.14 * (self.radius ** 2)
        
# list = [Rectangle(10, 20), Circle(20)]

# for item in list:
#     print(item.area())

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called")
#         func()
#         print("Something is happening after the function is called")
#     return wrapper
   
# @my_decorator 
# def sayHello():
#     print("Hello!")
    
# sayHello()
    