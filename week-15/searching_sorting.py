# iterative binary search
# fix it later!!!!
def binary_search(lst, target):
    pivot = len(lst) // 2
    end = len(lst) -1 
    start = 0
    while start<end:
        if target >= lst[pivot]:
            start = pivot + 1
        elif start > end:
            end = pivot - 1
        else:
            return pivot
        pivot = (end + start) // 2
    return -1

print(binary_search([1,2,7,8,9,77],9))
