
def minElem(lst):
    min =9
    if len(lst) == 1:
        return lst[0]
    else:
        minRest = minElem(lst[1:])
        if minRest < lst[0]:
            return minRest
        else:
            return lst[0]

print(minElem([1,2,8]))