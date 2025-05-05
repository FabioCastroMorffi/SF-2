def binarySearchRecursive(lst, target, low, high):
    if low <=high:
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid
        if lst[mid] < target: # search in right
            return binarySearchRecursive(lst, target, mid+1, high)
        else:
            return binarySearchRecursive(lst, target, low, mid -1)
        
    return -1

print(binarySearchRecursive([1,2,3,6,7,8], 6, 0, 6))    
