import numpy as np
def f(x):
    return np.sqrt(1-x**2)

def integral(slices):
    total = 0.0
    h = 2/slices
    for i in range(slices):
        x_i = -1+i*h
        total += f(x_i)*i
    return total
    
print(integral(300000))
print(np.pi/2)
%timeit -r 1 -n 1 integral(300000) #nmaximum number of slices to have the calculation under 1 second of duration
