# # from collections import * 
# # import pandas as pd
# # import numpy as np
# # import time
# # import os
# # from sklearn.model_selection import train_test_split
# # from sklearn.metrics import confusion_matrix


# name = 'Jishnu Srivastava'
# print(f'\n Nice to meet you {name}. \n')
# print(' - '*(19))
# print('\n')

# rows = 10
# k = 0
# for i in range(1, rows+1):
#     for space in range(1, (rows-i)+1):
#         print(end="  ")
   
#     while k!=(2*i-1):
#         print("* ", end="")
#         k += 1
#     k = 0
#     print('')
# print('\n')
# print(' - '*(rows*2 - 1))
# print('\n')

# rows1 = 10
# var1 = ord('A')
# for i in range(rows1):
#     for j in range(rows1-i-1):
#         print(end=' ')
#     for k in range(i+1):
#         print(chr(var1),end=" ")
#         var1+=1
#     print(" ")
# print('\n')
# print(' - '*(rows*2 - 1))
# print('\n')

# rows1 = 5
# # print(id(rows1))
# var1 = ord('A')
# for i in range(rows1):
#     for j in range(rows1-i-1):
#         print(end=' ')
#     for k in range(i+1):
#         print(hex(var1),end=" ")
#         var1+=1
#     print(" ")
# print('\n')
# print(' - '*(rows*2 - 1))
# print('\n')

# s = 'Sample string'
# s=s.replace('Sam','Dam')
# print(s)
# print(s[::-1])
# print(s[:3:-1])
# print('\n')
# print(' - '*(rows*2 - 1))
# print('\n')

# s1 = 'One more sample string '
# print(s1.split())
# print(s1.find('s',10,len(s1)))

l = ['I','am']
s1=' '.join(l) + ' MORE JOIN'
print(s1)