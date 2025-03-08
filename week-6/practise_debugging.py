'''
DEBUGGING

The function below should group a list of strings in a dictionary by length where the keys 
are integers representing the length of the word and the values are lists containing all 
words with the given length. The function should return the said dictionary. You can only change the
given lines of code.
    
    Example Input:
    > ["apple", "banana", "pear", "grape", "kiwi", "peach"]
    
    Example Output: 
    > {5: ['apple', 'grape', 'peach'], 6: ['banana'], 4: ['pear', 'kiwi']}
    
    NOTE: This function DOES compile. It contains 2 Semantic Errors
'''
def group_words_by_length(words):
    grouped = {}  
    for word in words:  
        length = len(word)
        if length in grouped:
            grouped[length] += word  
        else:
            grouped[length] = word  
    
    return grouped

print(group_words_by_length(["apple", "banana", "pear", "grape", "kiwi", "peach"]))

'''
Corrected function below
'''

def group_words_by_length_corrected(words):
    grouped = {}  
    for word in words:  
        length = len(word)
        if length in grouped:
            '''Since += concatenates, word needs to also be inside a list so that the output is ['word1', 'word2']
               ,otherwise, it will change the string in list by making each character in the string a value in the list
               and concatenate that: ['word1','w','o','r','d','2']
            
                Alternate solution: using .append(word) and leaving word as a string and not a list of strings
            '''
            grouped[length] += [word]  #Semantic Error 1
        else:
            '''
            The type of word is string so it should be put inside a list because we need to 
            output a list of strings
            '''
            grouped[length] = [word]  #Semantic Error 2
    
    return grouped

print(group_words_by_length_corrected(["apple", "banana", "pear", "grape", "kiwi", "peach"]))





