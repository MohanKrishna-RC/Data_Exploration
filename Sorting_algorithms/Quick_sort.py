"""
In this algorithm, we partition the list around a pivot element, sorting values around the pivot.
Best performance achieved when the pivot value splits the list into two almost equal halves.
"""

"""
Recursive
In Place
Unstable
O(nlogn)
"""

from abc import abstractproperty


def quicksort(array):
    print(len(array))
    if len(array)>1:
        mid = (len(array)-1) // 2
        # print(mid)
        if len(array)%2==0:
            pivot = (array[mid+1] + array[mid])//2  #Here pivot is the last element
        else:
            pivot = array[mid]
        print(pivot)
        grtr_lst,equal_lst,smlr_lst = [],[pivot],[]
        for item in array:
            if item == pivot:
                equal_lst.append(item)
            elif item>pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return (quicksort(smlr_lst) + equal_lst + quicksort(grtr_lst))
    else:
        return array

array1 = [5,2,4,3,1]
array2 = [10,2,7,4,5]
final_array1,final_array2 = quicksort(array1),quicksort(array2)


print(final_array1,final_array2)