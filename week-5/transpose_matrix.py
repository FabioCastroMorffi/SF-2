lst = [[1,2,7,3],[3,4,9,5],[6,7,8,0],[3,4,5,9]]
rows, columns = (len(lst[0]),len(lst))
trans_matrix = [[0 for number in range(columns)] for row in range(rows)] #missing check for empty
print(trans_matrix)
j = 0
i = 0
while j < len(lst[0]):
    trans_matrix[j][i] = lst[i][j]
    i+=1
    if i == len(lst):
        i = 0
        j+=1
print(trans_matrix)