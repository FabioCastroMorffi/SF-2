import random
'''Given a dictionary of key-value pairs, convert it to a list of lists using the map function. '''
def converter(d):
    x = map(list, d.items())
    print(list(x))
converter({1:2,2:3,3:4})
'''
Create a list, called key_lst, of randomly generated n>0 strings characters of which are between 'a' and 'z'.  
Create a second list, called value_lst, which is a list of sublists.  Each sublist also contains randomly 
generated n>0 strings character of which are between 'a' and 'z'.  From the two lists create a dictionary, 
where the keys are the elements of the list keys.  The i-th element in each sublist of values is mapped 
as a value to the i-th element in the keys list.  Print each key-value pair of the resulting dictionary on a new line.   

For example: 

key_lst = [ 'fruit', 'vegetable' ] 

value_lst = [ ['apple', 'pumpkin'],  

['pear', 'eggplant'], 

['peach', 'cucumber'], 

['apricot', 'zucchini'] ] 

The resulting dictionary is: 

{ 'fruit': ['apple', 'pear', 'each', 'apricot'], 

  'vegetable': ['pumpkin', 'eggplant', 'cucumber', 'zucchini'] } '''

def lst_to_dic():
    d = {}
    lst_keys = ['lol','kid']
    lst_items = [['meh','hum'],
                 ['wha','sum']]
    for i in range(len(lst_keys)):
        d[lst_keys[i]] = [[lst_items[_][i]] for _ in range(len(lst_items))]
    return d
print(lst_to_dic())

'''
Fibonnacci recursively
'''

def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)
print(fibo(5))


'''
Write a function summarizeLetters that receives a string and returns a list of tuples 
containing the unique letters and their frequences in the string.  Your function should 
ignore case sensitivity (that is, 'a' and 'A' are the same), ignore spaces and punctuation.   
Test your function and display each letter with its frequency.  
Your program should further print a statement at the end saying whether the string has all the letters of the alphabet or not.   
'''
#def d_to_tuples(d):

def summarizeLetters(s):
    d = {}
    s.lower()
    for char in s:
        if char.isalpha():
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
    lst_tuples = [(key,value) for key,value in d.items()]#d_to_tuples(d)
    return lst_tuples
print(summarizeLetters('startending'))





