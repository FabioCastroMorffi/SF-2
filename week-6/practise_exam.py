'''
countPeaks(2dlist) -> int:
integers strictly greater than neighbours
'''
def countPeaks(lsts) -> int:
    for lst in lsts:
        for i in range(len(lst)):
            num = lst[i]
