import math
import numpy as np
# 1)
def binomial (n,k):
    if k == 0:
        return 1
    else:
        return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

#2)
n = 20
for i in range(1,n):
    for j in range(i+1):
        print(binomial(i,j),end='')
    print()

#3)
def prob(n,k):
    return (binomial(n,k))/(2**n)

print(prob(100,60))

x = 0
for i in range(60,101):
    x += prob(100,i)

print(x)
