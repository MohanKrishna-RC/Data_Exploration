#!/bin/python3

import math
import os
import random
import re
import sys

#Return the maximum sum of subsequence and subarray

def finalre(arr):
    # N stores the total number of subsets
    N = int(pow(2, len(arr)))
 
    # generate each subset one by one
    result = []
    for i in range(N):
        s = []
        # check every bit of `i`
        for j in range(len(arr)):
            # if j'th bit of `i` is set, print S[j]
            if (i & (1 << j)) != 0:
                s.append(arr[j])
        result.append(s)
        res = [ele for ele in result if ele != []]

    return res

def subarray(nums):
    # consider all sublists starting from i
    subar = []
    for i in range(len(nums)):
        s = []
        # consider all sublists ending at `j`
        for j in range(i, len(nums)):
            # Function to print a sublist formed by [i, j]
            subar.append(nums[i: j + 1])
        
    return subar
def maxSum(result):
    # traversal in list of lists
    # res = max([ele for sub in result for ele in sub])
    s = max(result, key=sum)
    maxi = sum(s)
    return maxi
from collections import defaultdict

def mssl(lst, return_sublist=False):
    d = defaultdict(list)
    for i in range(len(lst)+1):
        for j in range(len(lst)+1):
            d[sum(lst[i:j])].append(lst[i:j])
    new_dict = {k:v for k,v in d.items() if v[0]}
    print(new_dict)
    key = max(new_dict.keys())
    if return_sublist:
        return (key, new_dict[key])
    return key

def maxSumsub(result):     
    for val in result:
        # print(i,val)
        maxi = 0
        sum1 = 0
        # traversal in list of lists
        for y in val:
            # print(y)
            sum1+= y
            maxi = max(sum1, maxi)
    return maxi
# def getval(result,maxi):
#     for i,val in enumerate(result):
#         # print(i,result[i])
#         if sum(val)==maxi:
#             return sum(val)
# def subse(result):
    # for i,val in enumerate(result):
    #     # print(val)
    #     r1 = finalre(val)
    #     # print(r1)
    #     r2 = maxSumsub(r1)
    #     # print(r2)
    # return r2
def maxSubarray(arr):
    re = finalre(arr)
    # print(re)
    maxi = maxSum(re)
    # print(maxi)
    # suval = subarray(arr)
    # print(suval)
    r6 = mssl(arr)
    return r6,maxi
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        # print(n)
        arr = list(map(int, input().rstrip().split()))
        # print(arr)
        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
