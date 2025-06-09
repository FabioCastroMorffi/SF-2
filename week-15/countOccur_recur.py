count = 0
def countOccur(lst,target):
    '''count number of ocurrences of element in a list'''
    if len(lst) == 0:
        return 0
    if lst[0] == target:
        count = 1
    else:
        count = 0
    return count + countOccur(lst[1:],target)

print(countOccur([1,2,3,3], 3))


def allSubsets(lst):
    if not lst:
        return []
    
    return [lst[:] + allSubsets(lst[1:])]

print(allSubsets([1,2,3]))