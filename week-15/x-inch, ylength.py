def recursiveRuler(inch, length):
    lst = []
    if length==1:
        return [1,2]
    lst += [1,length]
    return recursiveRuler(inch, length-1) + lst
print(recursiveRuler(1, 4))