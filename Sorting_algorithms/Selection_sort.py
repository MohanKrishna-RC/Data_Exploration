#SELECTION SORT
""" 
In this algorithm we create two segments of the list one sorted and other
unsorted. We continuously remove the smallest element from the unsorted segment
of the list and append it to the sorted segment. We don't swap intermediate elements.
Hence the algorithm sorts the array in minumum number of swaps.
"""

#Smallest element moves to the left end

"""
1. Non Recursive
2. Unstable
3. In place
4. O(n^2)
"""

def selection_sort(array):
    for i in range(len(array)-1):
        min_idx = i
        for idx in range(i+1,len(array)):
            # print(idx)
            # print("idx",array[idx])
            # print("min_idx",array[min_idx])
            if array[idx] < array[min_idx]:
                min_idx = idx
        print(min_idx)
        array[i],array[min_idx] = array[min_idx],array[i]
        # print(array)
    return(array)

array1 = [5,2,4,3,1]
array2 = [10,2,7,1,5]
sorted_array1,sorted_array2 = selection_sort(array1),selection_sort(array2)
print(sorted_array1,sorted_array2)

"""
[5,2,4,3,1] [1,2,4,3,5]  min_idx = 4
[1,2,4,3,5] [1,2,4,3,5]  min_idx = 1
[1,2,4,3,5] [1,2,3,4,5]  min_idx = 3
[1,2,3,4,5] [1,2,3,4,5]  min_idx = 3

[10,2,7,1,5] [1,2,7,10,5] min_idx = 3
[1,2,7,10,5] [1,2,7,10,5] min_idx = 1
[1,2,7,10,5] [1,2,5,10,7] min_idx = 4
[1,2,5,10,7] [1,2,5,7,10] min_idx = 4

"""
