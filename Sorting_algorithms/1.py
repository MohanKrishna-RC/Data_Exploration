# # from _typeshed import ReadOnlyBuffer


# def fun():
#     i = 0
#     sum = 0
#     while(i<100):
#         sum = sum + i
#         sum = i + sum
#         i +=1
#     print("kdhfkhd")
#     print(sum)

# fun()

# def fun(A,B):
#     if (B==0):
#         return A
#     else:
#         return fun(B,A%B)

# ans = fun(100,2000)
# print(ans)


# string = "djfjdhfihhd dkfjgskjf"

# count = 0
# for i in string:
#     count = count + 1
# print(count)

# count = 0
# a = []
# dict = {}

# a = [i for i in string]
# for i in a:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1

# print(dict)

# for i in string:
#     dict[i] = dict.get(i,0)+1

# print(dict)

# print(set(string))

# res = {i:string.count(i) for i in set(string)}
# print(res)

def raw_input():
    return input("Enter numbers: ")

nums = map(int, raw_input().split())
print(list(nums))
# val = list(nums)
# res = avg(*nums)


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def findSubstring(s, k):
    sub = []
    dict = {}
    # Write your code here
    for i in range(len(s)):
        a = s[i:i+k]
        if len(a)==k:
            sub.append(a)
    sub.pop()
    for i in range(len(sub)):
        count = 0
        for j in sub[i]:
            if j in 'aeiou':
                print(j)
                count = count+1
        dict[sub[i]]=count
    print(dict)
    itemMaxValue = max(dict.items(), key=lambda x: x[1])
    di = []
    for key,value in dict.items():
        if value==itemMaxValue[1] and value>0:
            di.append(key)
        elif value==itemMaxValue[1] and value==0:
            di.append('Not found!')
    
    return str(di[0])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    k = int(input().strip())

    result = findSubstring(s, k)

    fptr.write(result + '\n')

    fptr.close()
