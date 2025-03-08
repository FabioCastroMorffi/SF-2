'''
Nested loops

Create a function that takes a list of strings and removes all asterisks (*) by modifying the original list.
The function modifies the list in place, thus it does not return anything. Do not use the replace()
built-in python function for this exercice.

Example input:
> ['wo*rd','sal*m*on','mat*h**'] 

Example output:
> ['word','salmon','math']
'''


lst = ['wo*rd','sal*m*on','mat*h**']
def removeAsterisk(lst):
    for i in range(len(lst)):
        new_word = lst[i]
        for j in range(len(new_word)-1,-1,-1):
            if new_word[j] == "*":
                new_word = new_word[:j] + new_word[j+1:]
        lst[i] = new_word
            
            
removeAsterisk(lst)
print(lst)


