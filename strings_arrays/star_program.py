
seq = list(map(int,input().split()))

for i in range(seq[0]):
    for j in range(i,seq[0]):
        print("*"[i:j+1],end=" ")
    print("",end="\n")
    