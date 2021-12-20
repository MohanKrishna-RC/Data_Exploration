"""
This algorithm does not do a comparison between the elements. We use the mathematical properties
of the integers to sort. We count how many times a number has come and store
the count in the array where the index is mapped to the key's value.
"""

"""
Non Recursive
In place but needs extra space
Stable
O(n)
"""

def Counting_sort(nums):
    i_lower_bound , upper_bound = min(nums), max(nums)
    lower_bound = i_lower_bound
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        nums = [item + lb for item in nums]
        lower_bound , upper_bound = min(nums), max(nums)
    
    counter_nums = [0]*(upper_bound-lower_bound+1)
    for item in nums:
        counter_nums[item-lower_bound] += 1
    pos = 0
    for idx, item in enumerate(counter_nums):
        num = idx + lower_bound
        for i in range(item):
            nums[pos] = num
            pos += 1
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        nums = [item - lb for item in nums]
    return nums

array1 = [5,2,4,3,1]
array2 = [10,2,7,4,5]
final_array1,final_array2 = Counting_sort(array1),Counting_sort(array2)


print(final_array1,final_array2)