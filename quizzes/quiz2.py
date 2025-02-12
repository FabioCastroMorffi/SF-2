#Find all divisors of an integer n that is not 0

def divisors(n):
    divisors = []
    for i in range(1, n+1):
        if not(n%i):
            divisors.append(i)
            divisors.append(-1*i)

