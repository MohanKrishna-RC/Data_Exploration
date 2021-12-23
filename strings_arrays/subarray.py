
nums =list(map(int,input(f'Enter list here: ').split()))
string = input(f'Enter string here')
def sublist(nums):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            print(nums[i:j+1])

sublist(nums)

#Substring
"""
A substring of a string s is a string s' that occurs in s.
A substring is almost similar to a subarray, but it is in the
context of strings.
"""
def printAllSubstrings(string):
    for i in range(len(string)):
        for j in range(i,len(string)):
            print(string[i:j+1])

printAllSubstrings(string)