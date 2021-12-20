"""
Like selection sort, in this algorithm we segment the list into sorted the list into
sorted and unsorted parts. Then we iterate over the unsorted segment, and inser the 
element from this segment into correct position in the
sorted list
"""
"""
1.Non recursive
2.Stable
3. In place
4. O(n^2)
"""

def Insertion_sort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        # print(key)
        while array[j]> key and j>=0:
            array[j+1] = array[j]
            # print(array)
            j-=1  # j becomes -1 whenever it is coming outside
        # print(j)
        array[j+1] = key
        # print(array)
    return array


array1 = [5,2,4,3,1]
array2 = [10,2,7,1,5]
sorted_array1,sorted_array2 = Insertion_sort(array1),Insertion_sort(array2)
print(sorted_array1,sorted_array2)

"""
[5,2,4,3,1] [5,5,4,3,1] [2,5,4,3,1] [2,5,5,3,1] [2,4,5,3,1] [2,4,5,5,1] [2,4,4,5,1] [2,3,4,5,1]
[2,3,4,5,5] [2,3,4,4,5] [2,3,3,4,5] [2,2,3,4,5] [1,2,3,4,5]
"""