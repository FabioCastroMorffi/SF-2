def isDistinc(num: int) -> bool:
    s = str(year)
    for char in s:
        if char in digits_used:
            return False
        digits_used.append(char)
    return True
year = int(input())

while not isDistinc(year):
    year += 1
    
