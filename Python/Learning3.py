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

#Overriding is there, not overloading

from math import pi

class Shape:
    def __init__(self,name):
        self.name=name

    def area(self):
        pass

    def fact(self):
        return "2D Shape"

    def __str__(self):
        return self.name

class Square(Shape):
    def __init__(self,length):
        super().__init__('Square')
        self.length=length

    def area(self):
        return self.length**2

    def fact(self):
        return "Each angle is 90"

class Circle(Square):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius=radius
    
    def area(self):
        return pi*(self.radius**2)

obj1 = Square(4)
print(obj1.area())
print(obj1.fact())
obj2 = Circle(4)
print(obj2.area())
print(obj2.fact())