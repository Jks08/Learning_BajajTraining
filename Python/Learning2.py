# from Learning1 import *
import testImportFile as tif
import pdb

class Emp:
    org='Some Name'

    def __init__(self,eid='xxxxx',ename='Jon Doe',esal=29000):    
        #self refers to current object. A name other than self can be given, but the same must be referred throughout.
        self.__eid = eid                          
        self.__ename=ename
        self.__esal=esal
    
    def display(self):
        print(f"Employee name, ID and salary has been made private. Hehe! 🤣🤣🤣🤣🤣🤣")

    def disp2(self):
        print(f"Employee name is {self.__ename} bearing ID {self.__eid} and earning {self.__esal} Rs monthly.")

    @classmethod
    def modify(self,n):
        self.org=n

    @staticmethod
    def static_modify(n):
        Emp.org=n

    def my_func(*args,**kwargs):
        print(f"args are of type: {type(args)}; kwargs are of type: {type(kwargs)}")
        print()
        for i in args:
            print(f"{i}",end=" ")
        print()
        # pdb.set_trace()
        for j,k in kwargs.items():
            print(f"{j}:{k}",end=" ")

if __name__=='__main__':
    print()
    obj1 = Emp()  
    print()
    
    print(obj1.org)
    print()
    #obj is a pointer to the actual object, which is Emp(..). 
    # First, allocation of memory happens, then init function is called. init stand for initialize
    
    obj1.display()                
    print()                
    
    obj1.disp2()                  
    print()
    
    obj1.modify('BWAHAHAAHAH')
    print(obj1.org)
    print()
    
    obj1.static_modify('HEhe I want CAKE')
    print(obj1.org)
    print()
    
    dept = tif.dept().display()

    obj1.org = "Parkar"
    print(obj1.org)
    print()

    obj1.static_modify('Naha')
    print(obj1.org)
    print()

    obj1.modify('Dana')
    print(obj1.org)
    print()

    obj1.my_func(1,2,3,4,5,6,x=4,y=6,z=11)
    print('\n')


# class trialOfRenaming_self_Ininit:
#     def __init__(archisman,name):
#         archisman.name=name 

#     def display(archisman):
#         print(archisman.name)

# obj2 = trialOfRenaming_self_Ininit('Bhattacharya')
# obj2.display()

class Person:
    def __init__(self,name,Job=None,pay=0):
        self.name=name
        self.Job=Job
        self.pay=pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self,percent):
        self.pay = int(self.pay + (self.pay*percent/100))

    def __repr__(self):
        return "[Person: %s %s]"

bobo = Person('Bobo Smtith')
sues = Person('Sues me','Developer',100000)
sues.giveRaise(20)
print(sues.lastName(), sues.pay)
print(sues.__repr__())

import datetime
now = datetime.datetime.now()
print(now.__str__())
print(now.__repr__())