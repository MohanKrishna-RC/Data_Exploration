"""
Shell sort is an optimization over insertion sort. This is achieved by repeatedly doing
insertion sort on all elements fixed, decreasing intervals. Last iteration the interval is 1. 
Here it becomes a regular insert sort and it guarantees that the array will be sorted. But to note one point
is that by the time we do that array is almost sorted, hence the iteration is very fast.
"""
"""
1. Non recursive
2. Stable
3. In place
4. O(n^2) also depends on interval choice
"""
import math
def shell_sort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k-1
    print(k,interval)
    while interval>0:
        for i in range(interval,n):
            temp = array[i]
            j = i
            while j>=interval and array[j-interval] >temp:
                array[j] = array[j-interval]
                j-=interval
            array[j]= temp
        k-=1
        interval = 2**k-1
    return array

array1 = [5,2,4,3,1]
array2 = [10,2,7,1,5]
sorted_array1,sorted_array2 = shell_sort(array1),shell_sort(array2)
print(sorted_array1,sorted_array2)
