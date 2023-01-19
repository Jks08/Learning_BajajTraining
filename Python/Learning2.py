# from Learning1 import *
import testImportFile as tif
class Emp:
    def __init__(self,eid='xxxxx',ename='Jon Doe',esal=29000):    #self refers to current object. A name other than self can be given, 
        self.__eid = eid                          # but the same must be referred throughout.
        self.__ename=ename
        self.__esal=esal
    
    def display(self):
        print(f"Employee name, ID and salary has been made private. Hehe! 🤣🤣🤣🤣🤣🤣")

    def disp2(self):
        print(f"Employee name is {self.__ename} bearing ID {self.__eid} and earning {self.__esal} Rs monthly.")

if __name__=='__main__':
    obj1 = Emp()  #obj is a pointer to the actual object, which is Emp(..). First, allocation of memory happens, 
    obj1.display()                # then init function is called. init stand for initialize
    print()                
    obj1.disp2()                  
    print()
    dept = tif.dept().display()

# class trialOfRenaming_self_Ininit:
#     def __init__(archisman,name):
#         archisman.name=name 

#     def display(archisman):
#         print(archisman.name)

# obj2 = trialOfRenaming_self_Ininit('Bhattacharya')
# obj2.display()