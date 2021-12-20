"""
This is a divide and conquer algorithm. In this algorithm, we split a list in
half and keep splitting the list by 2 until it only has a single element. Then we merge
the sorted list. We keep doing this until we get a sorted list with all the elements
of the unsorted list.
"""
"""
Recursive
Stable
Needs extra space
O(nlogn)
"""

def mergeSort(nums):
    if len(nums)==1:
        return nums
    mid = (len(nums)-1) // 2
    lst1 = mergeSort(nums[:mid+1])
    lst2 = mergeSort(nums[mid+1:])
    result = merge(lst1, lst2)
    return result
def merge(lst1, lst2):
    lst = []
    i = 0
    j = 0
    while(i<=len(lst1)-1 and j<=len(lst2)-1):
        if lst1[i]<lst2[j]:
            lst.append(lst1[i])
            i+=1
        else:
            lst.append(lst2[j])
            j+=1
    if i>len(lst1)-1:
        while(j<=len(lst2)-1):
            lst.append(lst2[j])
            j+=1
    else:
        while(i<=len(lst1)-1):
            lst.append(lst1[i])
            i+=1
    return lst


array1 = [5,2,4,3,1]
array2 = [10,2,7,4,5]
final_array1,final_array2 = mergeSort(array1),mergeSort(array2)


print(final_array1,final_array2)