def main():
    str1 = input("Enter string: ")
    # print(type(str1))
    pa = 0
    if str1 in ['a','e','i','o','u']:
        print(1)
    else:
        print(1)
    # print(pa)

def find_most_frequent(arr):
    # YOUR CODE GOES HERE
    # print(arr)
    # print(arr)
    # arr = arr.remove("None")
    rep = {}
    # for j in range()
    for i in arr:
        if i in rep:
            rep[i]+=1
        else:
            rep[i]=1

    for k, v in rep.items():
        # print(k)
        if v is None:
            del rep[k]
        if k is None:
            del rep[k]
    # print(rep)
    Keymax = max(rep, key= lambda x: rep[x])
    return Keymax

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    
    T = int(input())
    
    while T > 0:
        
        A = input().split()
        N = int(A[0])
        
        largeIdx = 1
        
        for i in range(1, N + 1):
            A[i] = int(A[i])
            
        for i in range(1, N + 1):
            if A[i] > A[largeIdx]:
                largeIdx = i
            
        secondLargest = -1
        
        for i in range(1, N + 1):
            if i != largeIdx:
                secondLargest = max(secondLargest, A[i])
    
        print(secondLargest)
        T -= 1
        
    return 0

if __name__ == '__main__':
    main()

if __name__=="__main__":
    main()
    a = [1,2,3,45]
    a.pop()