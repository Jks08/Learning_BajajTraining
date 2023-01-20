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
print('\n')


#Operator Overloading
class Book1:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other_ob):
        return self.pages+other_ob.pages

    def __gt__(self,other_ob):
        if self.pages>other_ob.pages: 
            return "b1 has more than pages" 
        else: 
            "b1 has less pages"

class Book2:
    def __init__(self,pages):
        self.pages=pages

b1 = Book1(100)
b2 = Book2(200)
print(b1+b2)
print('\n')

#Regular Expressions
import re
p = re.compile(r'm\w\w')
s = "cat rat mat sat men watt"
r = p.search(s)
print(r.group())

p1 = re.search(r'w\w\w',s)
print(p1.group())
print()

st = 'This; is the: "Core" Python\'s book'
r1 = re.split(r'\W',st)
print(r1)
print()

st1 = "This is beautiful"
r2 = re.sub(r'beautiful',r'not so beautiful',st1)
print(r2)
print()

st2 = "An apple a day keeps the doctor awaya"
r3 = re.findall(r'[b-z,B-Z]+[\w]*',st2)
for w in r3:
    print(w)

print()

st3 = "one two three four five six seven 8 9 10"
r4 = re.findall(r'\b\w{3,5}\b',st3)
print(r4)
print()
r5 = re.findall(r'\b\d\b',st3)
print(r5)
print()
st4 = "one two three onw two three"
r6 = re.findall(r't[\w]*',st4)
print(r6)
print()

print("ASSIGNMENT OF MAIL OID REGEX *******************************")
print()

f = open('mailIDs.txt','r')
for i in f:
    i = i.strip()
    # emails = re.findall("[0-9a-zA-z]+@[0-9a-zA-z]+\.[0-9a-zA-z]+[.]*\w*", i)
    emails = re.findall(r"\S+@\S+",i)
    if(len(emails)>0):
        print(emails)
print()

st5 = "Today is 19/01/2023. Next class will be from 06/10/2023"
r7 = re.findall(r'\d+/\d+/\d+',st5)
print(r7)
print('\n')


# from urllib.request import urlopen
# urlToRead = "https://raw.githubusercontent.com/Jks08/Exploratory-Data-Analysis/main/IBM_HR.csv"
# import pandas as pd
# def read_data(url):
#     if url.startswith(('http:','https:','ftp:')):
#         # return urlopen(url).read()
#         return pd.read_csv(url)

#     else:
#         print('Not valid URL')

# # s = read_data(urlToRead).decode('utf-8')
# s = pd.DataFrame(pd.read_csv(urlToRead))
# dic = {}
# for i in s.columns:
#     if i in ['Age','Attrition','Department','JobLevel','Gender']:
#         print(f"Header: {i} | Value:{s[i][0]}")
#         dic[i] = s[i][0]

# print(dic)
# newSheet = pd.DataFrame(dic,index=[0])
# newSheet.to_excel('newSheet.xlsx')

# def extract_headers_from_csv_url(urlToRead):
#     try:
#         webUrl = urlopen(url)
#         print("Result code: " + str(webUrl.getcode()))
#         data = webUrl.read()
#         print(data)
#         headers = str(data).split("\\n")[0]
#         print(headers)
#         header_list = headers.split(",")
#         print(header_list)
#     except Exception as e:
#         print("Exception occured: " + str(e))

# def extract_headers_from_csv_url(urlToRead):
#     try:
#         webUrl = urlopen(urlToRead)
#         print("Result code: " + str(webUrl.getcode()))
#         data = webUrl.read()
#         print(data)
#         headers = str(data).split("\\n")[0]
#         print(headers)
#         header_list = headers.split(",")
#         print(header_list)
#     except Exception as e:
#         print("Exception occured: " + str(e))