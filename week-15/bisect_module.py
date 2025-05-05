'''
bisect arguments:
--> lst to work with 
--> num to insert into the lst
--> [start, end] interval of lst to consider (defaulted to the entire lst)

bisect(lst, num, start, end)
returns index where num can be inserted so lst stays sorted 
if num is already in lst, returns rightmost index where num can be inserted

bisect_left(lst, num, start, end)
returns the index where num can be inserted so lst stays sorted
if num is already in lst, returns the leftmost index where num can be inserted


'''
import bisect
lst = [1, 2, 7, 7, 8, 9]
num = 7
print(bisect.bisect(lst, num))