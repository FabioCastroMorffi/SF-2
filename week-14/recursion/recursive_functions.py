sum = 0
def recursiveSum(n):
    if n == 1:
        return 1
    else:   
        return recursiveSum(n-1) + n

print(recursiveSum(6))

def recursiveFactorial(n):
    if n == 1:
        return 1
    else:
        return recursiveFactorial(n-1) * n

def badfibonacci(n):
    if n <= 1:
        return n
    else:
        return badfibonacci(n-1) + badfibonacci(n-2)
