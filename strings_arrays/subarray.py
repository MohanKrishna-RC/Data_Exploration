
nums =list(map(int,input(f'Enter list here: ').split()))

def sublist(nums):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            print(nums[i:j+1])

sublist(nums)