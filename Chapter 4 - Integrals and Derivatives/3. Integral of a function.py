import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t**2)

def Simpson(x):
    a = 0
    b = x
    N = 100
    h = (b-a)/N
    sum_odd = 0
    for k in range(1,N,2):
        sum_odd = f(a + k*h)
    
    sum_even = 0
    for k in range(2,N,2):
        sum_even = f(a + k*h)
    return 1/3 * h * (f(a) + f(b) + 4*sum_odd + 2*sum_even)

xs = np.linspace(0,3,100)
values = np.array(list(map(Simpson,xs)))

plt.plot(xs,values)
plt.xlabel("x")
plt.ylabel("E(x)")
plt.show()
