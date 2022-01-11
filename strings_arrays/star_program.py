
# seq = list(map(int,input().split()))
n = int(input("Enter pyramid: "))

for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print("",end="\n")

k = 1
for i in range(0,n):
    for j in range(0,n-1-i):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print(end="\n")


# for i in range(0,n):
#     for j in range(0,n-i-1):
#         print("*",end=" ")
#     for j in range(n-i-1,n):
#         print(end=" ")
#     print()

for i in range(0,n):
    for j in range(0,i+1):
        print(end=" ")
    # k = k-2
    for j in range(0,n-i-1):
        print("*",end=" ")
    print(end="\n")

# for i in range(len)