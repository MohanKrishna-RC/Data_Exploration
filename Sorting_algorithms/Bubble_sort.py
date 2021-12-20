""" Sorting means putting items in a particular order. That particular
order is determined by the comparison property of the elements.
Arranging items in a particular order improves the searching of the elements.
Hence sorting has heavy usage.
"""
#BUBBLE SORT
""" Simplest sorting algorithm. Iterates over the list, in each iteration it compares elements
in pairs and keeps swapping them such that the larger element is moved towards the end of the list.
"""

""" 1. Non Recursive
    2. Stable
    3. In place
    4. O(n^2)
"""

def bubblesort(array):
    swapped = False
    # print(swapped)
    for i in range(len(array)-1,0,-1):
        # print(i)
        # print(swapped)
        for j in range(i):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                # print(array)
                swapped = True
        
        # print(swapped)
        if swapped:
            swapped = False
        else:
            break
    return array

array1 = [5,2,4,3,1]
array2 = [10,2,7,4,5]
final_array1,final_array2 = bubblesort(array1),bubblesort(array2)


print(final_array1,final_array2)

""" Output explanation

[5,2,4,3,1] [2,5,4,3,1] [2,4,5,3,1] [2,4,3,5,1] [2,4,3,1,5]
[2,4,3,1,5] [2,4,3,1,5] [2,3,4,1,5] [ 2,3,1,4,5]
[2,3,1,4,5] [2,3,1,4,5] [2,1,3,4,5]
[2,1,3,4,5] [1,2,3,4,5]

[10,2,7,4,5] [2,10,7,4,5] [2,7,10,4,5] [2,7,4,10,5] [2,7,4,5,10]
[2,7,4,5,10] [2,7,4,5,10] [2,4,7,5,10] [2,4,5,7,10]
[2,4,5,7,10] [2,4,5,7,10] [2,4,7,5,10]
"""
