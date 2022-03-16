import math
def prime(lim):
    primes = [2]
    n = 3
    while n <= lim:
        for prime in primes:
            if n % prime == 0:
                break
            elif prime > math.sqrt(n):
                primes.append(n)
                break
        n += 1
    return primes

print(prime(10000))
