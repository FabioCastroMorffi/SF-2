#question 1 
def sum_strings(dict):
    count = 0
    for key in dict.keys():
        if type(key) == str:
            count += len(dict[key])
    return count
#print(sum_strings({2: [1,2,3], '2': [2,3,4,4]}))

def wordTally(n):
    count = 0
    d = {}
    while count < n:
        m = input()
        if m in d.keys():
            d[m] += 1
        else:
            d[m] = 0
        count += 1
    return d

#print(wordTally(3))   

def invertDictionary(d):
    d_inverted = {}
    for key,val in d.items():
        if val not in d_inverted:
            d_inverted[val] = [key]
        else:
            d_inverted[val] += [key]
    return d_inverted

#print(invertDictionary({1:2,2:2,3:2}))
#dothis
def kCommon(k, lst):
    d = {}
    for word in lst:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    
    other_lst = list(d.values())
    other_lst.sort(reverse=True)
    
    
    

print(kCommon(2, ['l','l','l']))
        

            

