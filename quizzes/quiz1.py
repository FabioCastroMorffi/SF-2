'''
Find prime numbers
'''


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, round(n**0.5)):
        if not(n%i):
            return False
    return True

''' print first 100 numbers '''

primes = []
n = 2 
while len(primes) < 100:
    if isPrime(n):
        primes.append(n)
    n += 1
print(primes)