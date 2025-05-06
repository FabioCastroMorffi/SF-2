#def partition(lst)

def recursiveQuicksort(lst):
    if len(lst) <= 1:
        return lst
    
    mid_lst = [lst[0]]
    mid = lst.pop(0)
    smaller_lst = [num for num in lst if num <= mid]
    greater_lst = [num for num in lst if num > mid]
    
    return recursiveQuicksort(smaller_lst) + mid_lst + recursiveQuicksort(greater_lst)

def inPlaceRecQuicksort(lst):
    if len(lst) <= 1:
        return lst
    
print(recursiveQuicksort([9,5,8,3]))