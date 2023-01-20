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

class Animal:
    def __init__(self,animal):
        self.animal=animal
        print(f"{self.animal} is an animal")

class Mammal(Animal):
    def __init__(self, mname):
        print(f"{mname} is warm blooded")
        super().__init__(mname)

class NonWingedMammal(Mammal):
    def __init__(self, nwmammal):
        print(f"{nwmammal} cant swim")
        super().__init__(nwmammal)

class NonMarineAnimal(Mammal):
    def __init__(self, nwmammal):
        print(f"{nwmammal} cant swim")
        super().__init__(nwmammal)

class Dog(NonMarineAnimal,NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs')
        super().__init__('Dog')

obj1 = NonWingedMammal('Platypus')
print(Dog.mro())         
