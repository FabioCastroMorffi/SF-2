def uniquePaths(lst: list[list]):
    empty_lst = []
    for i in range(len(lst)):
        empty_lst.append([])
        for j in range(len(lst[i])):
            if not(i) or not(j):
                empty_lst[i].append(1)
            else:
                empty_lst[i].append(empty_lst[i-1][j]+empty_lst[i-1][j-1])
    return empty_lst


    




new_lst = uniquePaths([["x","x","x"],["x","x","x"],["x",'x','x'],['x','x','x']])
print(new_lst)