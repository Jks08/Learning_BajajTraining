# from Learning1 import *
import testImportFile as tif
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


# class trialOfRenaming_self_Ininit:
#     def __init__(archisman,name):
#         archisman.name=name 

#     def display(archisman):
#         print(archisman.name)

# obj2 = trialOfRenaming_self_Ininit('Bhattacharya')
# obj2.display()