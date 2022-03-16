import numpy as np

def quadratic(a,b,c):
    x1 = ((-b+np.sqrt(b**2-4*a*c))/2*a)
    x2 = ((-b-np.sqrt(b**2 - 4*a*c))/2*a)
    return x1,x2

print(quadratic(0.001,1000,0.001))

def quadratic2(a,b,c):
    x1 = (2*c)/(-b+np.sqrt(b**2 - 4*a*c))
    x2 =  (2*c)/(-b-np.sqrt(b**2 - 4*a*c))
    return x1,x2
print(quadratic2(0.001,1000,0.001))

def quadratic3(a,b,c):
    x1 = ((-b+np.sqrt(b**2-4*a*c))/2*a)
    x2 =  2*c/(-b-np.sqrt(b**2 - 4*a*c))
    return x1,x2
print(quadratic3(0.001,1000,0.001))
