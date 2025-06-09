from math import factorial
lst = [12,45,73,4]
current_max = lst[0] # 2

for i in range(1,len(lst)): # n + n
    if lst[i] > current_max: #2(n-1)
        current_max = lst[i] #2(n-1)
print(current_max) #1
                   # 7n -1 

## Primitive operations: Assignment, comparaison, etc1

## Constant time give or take between 
# a = shortest time it takes to run the fastest primitive operation
# b = longest time it takes to run the slowest primitive operation
# so the bounds: a(7n -1) <= T(n) <= b(7n-1), where T(n) is the run time

# Space complexity
# Very similar but with space
# 2d lists have space complexity of O(mk) 

#def binom(n, k):
#    num = factorial(n)
#    denom = factorial(n-k)*factorial(k)
#    return num//denom

#creating pascal triangles(store in list of lists)
#finish this with n^2 time
#reduce space complexity to linear

def pascalTriangles(desired_length):
    lst_pascal = [[1]]
    for row in range(1,desired_length):
        now_empty = []
        for j in range(i+1):
            if 
        lst_pascal.append(now_empty)
    return lst_pascal
pasc = pascalTriangles(4)

def printPascal(pasc):
    for row in pasc:
        for i in range(len(row)):
            print(row[i], end= '')
        print()

    
print(pascalTriangles(4))

#What is running time of your algo?
#What is the auxiliary space used?




#


