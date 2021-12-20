"""
We create two segments of the list one sorted and one unsorted.
In this we used heap data structure to efficiently get the max element
from the unsorted segment of the list. 
Heapify method uses recursion to get the max element at the top.

"""

"""
1. Non recursive
2. Unstable
3. In place
4. O(nlogn)
"""

def heapify(array,n,i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l<n and array[i]<array[l]:
        largest = l
    if r<n and array[largest] <array[r]:
        largest = r
    
    if largest!=i:
        array[i],array[largest] = array[largest],array[i]
        heapify(array,n,largest)
def heap_sort(array):
    n = len(array)
    for i in range(n//2,-1,-1):
        heapify(array,n,i)
    for i in range(n-1,0,-1):
        array[i],array[0] = array[0],array[i]
        heapify(array,i,0)
    return array

array1 = [5,2,4,3,1]
array2 = [10,2,7,1,5]
sorted_array1,sorted_array2 = heap_sort(array1),heap_sort(array2)
print(sorted_array1,sorted_array2)
