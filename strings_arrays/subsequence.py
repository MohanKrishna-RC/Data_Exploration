#Subsequence
"""
A subsequence is a sequence that can be derived from another sequence
by deleting some elements without changing the order of the remaining elements.
"""

"""
It is confused between a subarray/substring and a subsequence. A subarray or substring
will always be continuous, but a subsequence need not be continuous. That is,
subsequences are not required to occupy consecutive positions within the original subsequences.
But we can say that both contiguous subsequence and subarray are the same.
"""
#Subset
"""
A subset is any possible combination of the original set. The term subset is often used for subsequence, but that's not right.
A subsequence always maintains the relative order of the array elements(i.e increasing index), but there is 
no such restriciton on a subset.
"""

"""
Subsequence can be in the context of both arrays and strings.
Generating all subsequences of an array/string is equivalent to generating
a power set of an array/string.
"""

def printSubsequence(input,output):
    if len(input) ==0:
        print(output,end=' ')
        return 
    # output is passed with including the
    # 1st character of input string
    printSubsequence(input[1:],output+input[0])
    
    # output is passed without including the
    # 1st character of input string
    printSubsequence(input[1:],output)


output = ""
input = str(input(f'Enter string here: '))


printSubsequence(input,output)

def finaPowerset(seq):
    #N stores the total number of subsets
    N = int(pow(2,len(seq)))

    #generate each subset one by one
    result = []
    for i in range(N):
        s = ''
        #check every bit of 'i'
        for j in range(len(seq)):
            #if j'th bit of 'i' is set, print s[j]
            if (i&(1<<j))!=0:
                s+=seq[j]
        result.append(s)
    print(result)

finaPowerset(input)












