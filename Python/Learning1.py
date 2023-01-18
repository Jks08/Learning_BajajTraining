# # from collections import * 
# # import pandas as pd
# # import numpy as np
# # import time
# # import os
# # from sklearn.model_selection import train_test_split
# # from sklearn.metrics import confusion_matrix

fixedLength = 10
def hello_message():
    name = 'Jishnu Srivastava'
    print(f'\n Nice to meet you {name}. \n')
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

hello_message()
star_triangle()
hex_triangle()
letters_triangle()
string_ops1()