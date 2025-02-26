'''
We are given n unopened boxes with k number of figurines in each box. 
The boxes cannot be opened and hence, the order of the figurines that are in the boxes cannot be changed.
A box cannot be rotated(otherwise, the figurines will be facing the wrong way).

Each figurine has a specified height. for example, in a given box the height of the figurines
from left to right could be 4, 5, or 6
Note that the number of figurines in each box may vary.
May assume a box is not empty.

We would like to organize all the toy boxes 
such that they are arranged in increasing order (or same height) of figurine heights 
from left to right. However, this may not necessarily be possible at all time with the given boxes. 
Hence, write a program to determine if we can have a such an arrangement or not.

INPUT SPECIFICATION

first line: integer n representing numer of toy boxes
next n lines: one for each box. Each of these lines begins with
--> integer k indicating the number of figurines in each box (k>=1)
--> followed by k integers giving the height of each figurine from left to right separaed by a space(heights >= 1)

Example 

Input:

2 -> n
3 4 5 7 <-- heights of each fig
^- k

Output: 

False
'''

'''
Top-down Design: capturing the main tasks of the solution
--> some tasks dont require much code
    => will solve directly
--> other tasks will require more code
    => will turn into functions
'''

def readBoxes(n):
    lst_boxes = []
    for i in range(n):
        box = input().split() #box content
        box.pop(0)            # 
        for i in range(len(box)):
            box[i] = int(box[i])
        lst_boxes.append(box)
    return lst_boxes
def allBoxesOK(lst_boxes) -> bool:
    '''
    determine if each box in lst_boxes has figurines
    in nondecreasing order of height.
    if so return True; otherwise, return False
    '''
    for box in lst_boxes:
        if sorted(box) != box:
            return False
        return True
def boxIntervals(lst_boxes):
    intervals = []

    for box in lst_boxes:
        intervals.append(box[0], box[-1])

def allIntervalsOK(lst_intervals):
    '''
    return True if all intervals in non-decreasing order otherwise, return False

    Example:
    [[1,6],[9,25],[32,36]]
    --> each box sorted
    -->sublists already sorted according to first element
    --> only need to check if first value of current sublist is > second value of previous sublist
    '''

    prev_max_height = lst_intervals[0][1]
    for box in range(1, len(lst_intervals)):
        current_min_height = lst_intervals[box][0]
        if current_min_height < prev_max_height:
            return False
        prev_max_height = lst_intervals[box][1]
    return True

#MAIN PROGRAM
#read input
n = int(input())
boxes = readBoxes(n)

# TODO: check if all boxes are sorted increasingly
if not allBoxesOK(boxes):
    print('NO')
else:

    # TODO: obtain a new list of boxes only with endpoints(as intervals)
    intervals = boxIntervals(boxes)
    # TODO: sort the boxes according to interval
    intervals.sort()
    # TODO: determine whether boxes are organized 
    if allIntervalsOK(intervals):
        print("Yes")
    else:
        print("No")
