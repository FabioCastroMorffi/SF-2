from stack import Stack
def isMatched(s:str)-> bool:
    stack = Stack()
    d = {'(': ')', '[':']', '{':'}'}
    for char in s:
        if char == '(' == '[' == '{': 
            stack.push(char)
        if not(stack.isEmpty()) and stack.top() == char :
            stack.pop()
        else: 
            return False
    return True
    '''
    Write a function called isMatched that takes 
    one string argument of parentheses and 
    determines if the given sequence of parentheses
    is matched.

    Examples:
    ()(()){([])} --> true
    ({[]})} --> false
    
    '''
print(isMatched('()()[{}]'))


