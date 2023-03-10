# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def get_stud_details(self):
#         return self.name,self.age
    
#     def set_stud_details(self,name,age):
#         self.name=name
#         self.age=age

# class Science_stud(Student):
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def get_stud(self):
#         return "Science"

# if __name__=='__main__':
#     obj = Science_stud('JKS',21)
#     print(obj.get_stud_details())
#     obj.set_stud_details('AB',21)
#     print(obj.get_stud_details())
#     print(obj.get_stud())

#-------------------------------------------------------------------------------------------
print()

# class Animal:
#     def __init__(self,animal):
#         self.animal=animal
#         print(f"{self.animal} is an animal")

# class Mammal(Animal):
#     def __init__(self, mname):
#         print(f"{mname} is warm blooded")
#         super().__init__(mname)

# class NonWingedMammal(Mammal):
#     def __init__(self, nwmammal):
#         print(f"{nwmammal} cant swim")
#         super().__init__(nwmammal)

# class NonMarineAnimal(Mammal):
#     def __init__(self, nwmammal):
#         print(f"{nwmammal} cant swim")
#         super().__init__(nwmammal)

# class Dog(NonMarineAnimal,NonWingedMammal):
#     def __init__(self):
#         print('Dog has 4 legs')
#         super().__init__('Dog')

# obj1 = NonWingedMammal('Platypus')
# print(Dog.mro())     

#-------------------------------------------------------------------------------------------
print()

#Polymorphism
# class Cat:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def info(self):
#         print(f"The cat is called {self.name} and is {self.age} years old")

#     def speak(self):
#         print("meow")

# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def info(self):
#         print(f"The dog is called {self.name} and is {self.age} years old")

#     def speak(self):
#         print('woof')
# cat1 = Cat('Kitty',3)
# dog1 = Dog('Doggy',4)
# for i in (cat1,dog1):
#     i.info()
#     i.speak()
#     print()

#-------------------------------------------------------------------------------------------

#Overriding is there, not overloading

# from math import pi

# class Shape:
#     def __init__(self,name):
#         self.name=name

#     def area(self):
#         pass

#     def fact(self):
#         return "2D Shape"

#     def __str__(self):
#         return self.name

# class Square(Shape):
#     def __init__(self,length):
#         super().__init__('Square')
#         self.length=length

#     def area(self):
#         return self.length**2

#     def fact(self):
#         return "Each angle is 90"

# class Circle(Square):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius=radius
    
#     def area(self):
#         return pi*(self.radius**2)

# obj1 = Square(4)
# print(obj1.area())
# print(obj1.fact())
# obj2 = Circle(4)
# print(obj2.area())
# print(obj2.fact())

#-------------------------------------------------------------------------------------------

#ABC stands for Abstract Base Class
# from abc import ABC, abstractmethod

# class MyClass(ABC):
#     @abstractmethod
#     def calc(self):
#         pass

# class MyClass(ABC):
#     def connect(self):
#         pass
#     def disconnect(self):
#         pass

# class SubClass(MyClass):
#     def calc(self,x):
#         print(f"{x**2} is the square of {x}")

#     def connect(self):
#         super().connect()
#         print("Connected to DB")

# if __name__ == '__main__':
#     obj = SubClass()
#     obj.calc(13)
#     obj.connect()

#--------------------------------------------------------------------------------------------------------------

#Exception Handling

# try:
#     f = open('test.txt','r')
#     a,b = [int(x) for x in input("Enter two numbers: ").split()]
#     print(a/b)
#     f.write(f"{a} divided by {b} is {a/b}")
# except ZeroDivisionError as e:
#     print("Division by zero is not possible")

# except IOError as e:
#     print("Error: File not found or path is incorrect")


# def avg(l):
#     t=0
#     for i in l:
#         t+=i
#     avg= t/len(l)
#     return t,avg

# if __name__=='__main__':
#     try:
#         t,a=avg([1,2,3,4,5])
#         print(f"Total is {t} and average is {a}")
#     except TypeError as e:
#         print("The list should contain only numbers",e)
#     except ZeroDivisionError as e:
#         print("The list should not be empty",e)

#-------------------------------------------------------------------------------------------

#Logging

# import logging

# logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
# logger = logging.getLogger().setLevel(logging.DEBUG)
# logger.debug("This is a debug message")
# logger.info("This is an info message")
# logger.warning("This is a warning message")
# logger.error("This is an error message")
# logger.critical("This is a critical message")
# logger.exception("This is an exception message")

#-------------------------------------------------------------------------------------------

#Generators
#created using yield keyword. Maintain the return state of the function in the cache memory.

# def countdown(n):
#     i=0
#     while i<=n:
#         yield i
#         i+=1
# y = countdown(20)
# for i in y:
#     print(i)
#     if(i==15):
#         break

#-------------------------------------------------------------------------------------------

#Iterators
#Iterators are objects that can be iterated upon. They are implemented using __iter__() and __next__() methods.

# class MyIterator:
#     def __init__(self,l,h):
#         self.l=l
#         self.h=h

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.l<=self.h:
#             x = self.l
#             self.l+=1
#             return x
#         else:
#             raise StopIteration

# if __name__ == '__main__':
#     obj = MyIterator(1,10)
#     for i in obj:
#         print(i)


#-------------------------------------------------------------------------------------------

#Decorators
#Decorators are used to modify the functionality of a function without changing the function itself. They are implemented using @ symbol. Decorators can be used to implement logging, authentication, etc. Decorators are created using closures (functions returning functions).

def my_decorator(func):
    def wrapper(n1,n2):
        f = func(n1,n2)
        return 1+f
    return wrapper
@my_decorator
def wrapper(n1,n2):
    return n1+n2

def double_val(func):
    def wrapper(n1,n2):
        f = func(n1,n2)
        return f*2
    return wrapper

@double_val
@my_decorator
def myfunc(n1,n2):
    return n1*n2

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print(wrapper(n1,n2))
print(myfunc(n1,n2))

#-------------------------------------------------------------------------------------------