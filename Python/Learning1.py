# from collections import * 
# import pandas as pd
# import numpy as np
# import time
# import os
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import confusion_matrix

fixedLength = 10
def hello_message():
    name = 'Jishnu Srivastava'
    print("Hello {}".format(name)) #normal basic format example
    print(f'\n Nice to meet you {name}. \n') #f string print example
    print(' - '*(19))
    print('\n')

def star_triangle():
    rows = 10
    k = 0
    for i in range(1, rows+1):
        for space in range(1, (rows-i)+1):
            print(end="  ")
   
        while k!=(2*i-1):
            print("* ", end="")
            k += 1
        k = 0
        print('')

    print('\n')
    print(' - '*(fixedLength*2 - 1))
    print('\n')

def letters_triangle():
    rows1 = 10
    var1 = ord('A')
    for i in range(rows1):
        for j in range(rows1-i-1):
            print(end=' ')
        for k in range(i+1):
            print(chr(var1),end=" ")
            var1+=1
        print(" ")
    print('\n')
    print(' - '*(fixedLength*2 - 1))
    print('\n')

def hex_triangle():
    rows1 = 5
    # print(id(rows1))
    var1 = ord('A')
    for i in range(rows1):
        for j in range(rows1-i-1):
            print(end=' ')
        for k in range(i+1):
            print(hex(var1),end=" ")
            var1+=1
        print(" ")
    print('\n')
    print(' - '*(fixedLength*2 - 1))
    print('\n')

def string_ops1():
    s = 'Sample string'
    s=s.replace('Sam','Dam')
    print(s)
    print(s[::-1])
    print(s[:3:-1])
    print('\n')
    print(' - '*(fixedLength*2 - 1))
    print('\n')

    s1 = 'One more sample string '
    print(s1.split())
    print(s1.find('s',10,len(s1)))

    l = ['I','am']
    s1=' '.join(l) + ' MORE JOIN'
    print(s1)

    s2 = "             Strip example                "
    print(s2.strip())

def some_formatting():
    print("{:5d}".format(12))
    print("{:2d}".format(1234))
    print("{:8.3f}".format(12.23456))
    print("{:05d}".format(12))
    print("{:08.3f}".format(12.23456))
    print("{:^10.3f}".format(12.23456))
    print("{:<05d}".format(12))
    print("{:08.3f}".format(12.23456))
    print("{:=8.3f}".format(-12.23456))

def no_of_occurences_of_char():
    s3 = "I am learning python"
    dic = {}
    for i in s3:
        if(i in dic):
            dic[i]+=1
        else:
            dic[i]=1
    print(dic)

def list_ops1():
    s = [3,4,5]
    s1 = [6,7,8]
    s+=s1
    print(*s)

    print(s.reverse())
    print(s.pop())
    print(s.index(6))
    s.remove(7)
    print(s)
    print(s.count(8))
    print(len(s))

def dict_ops1():
    dic = {}
    l1 = [1,2]
    l2 = [3,4]
    for i in range(len(l1)):
        dic[l1[i]]=l2[i]
    print(f"Keys - {dic.keys()}; type - {type(dic.keys())}")
    print(f"Values - {dic.values()}; type - {type(dic.values())}")
    print(f"Items - {dic.items()}; type - {type(dic.items())}")

    l11 = ['India','Lanks','Chin']
    l22 = ['pune','colombo']
    dic2 = dict(list(zip(l11,l22)))  #If length of the 2 lists are mismatched, then the extra value of any list are ignored.
    print(dic2)
    print(sorted(dic2))
    print(sorted(dic2.keys()))
      

def set_ops1(): #only reads unique elements
    s1 = {1,2,3}
    s2 = set()
    s2.add(9)
    s2.add(1)
    s2.add(2)
    s2.add(3)
    s1.remove(3)
    print(s1,s2)

    print(f"Union: {s1.union(s2)}")
    print(f"Difference: {s1.difference(s2)}")
    print(f"Symmetric Difference: {s1.symmetric_difference(s2)}")
    print(f"Intersection: {s1.intersection(s2)}")

def func_ops1(aList):
    aList.append(100)

def recur_fact(a):
    if(a==1):
        return a
    else:
        return a*recur_fact(a-1)

def rev_str_recur(st):
    if(len(st)==0):
        return st
    else:
        return rev_str_recur(st[1:])+st[0]


# hello_message()
# star_triangle()
# hex_triangle()
# letters_triangle()
# string_ops1()
# some_formatting()
# no_of_occurences_of_char()
# list_ops1()
# dict_ops1()
# set_ops1()

'''
l = [1,2,3]
print(func_ops1(l))
print(l)
'''

# print(recur_fact(5))
# print(rev_str_recur("Jishnu is alive"))

#Lambda function are oneliners, anonymous and we are referring it here with the variable lambdaFunc.
'''
lambdaFunc = lambda x,y:x+y 
print(lambdaFunc(10,20))
'''
'''
lis1 = list(map(int,input().split()))
lambdaFunc2 = list(map(lambda x:x**3, lis1)) #This lambda function takes in input and print the cubes of all elements.
print(lambdaFunc2)
'''
'''
from functools import reduce  #reduce function
lis1 = [1,2,3,4,5]
lis1.reverse()
L = reduce(lambda x,y:x**y,lis1)
print(L)
'''