def isPalindrome(lst):
    #temp = lst
    temp = lst[:]
    #temp.reverse
    temp.reverse()
    return temp == lst

def silly(n):
    result = []
    for i in range(n):
        #result = []
        elem = input('Enter element: ')
        result.append(elem)
    if isPalindrome(result):
        print('Yes')
    else:
        print('No')
silly(2)