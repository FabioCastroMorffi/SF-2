
lst = [1,3,2]
def inertSort(lst):
    if len(lst) <= 1:
        return lst
    
    for i in range(1, n):
        elem = lst[i]
        j = i -1 
        while j>=0 and elem < lst[j]:
            lst[j+1] = lst[j+1]
            j -=1
        lst[j+1] = elem
    return lst
print(insertSort(lst))
##for decreasing vars