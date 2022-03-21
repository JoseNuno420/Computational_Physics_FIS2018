import numpy as np

def f(x):
    return np.sqrt(1-x**2)

def integrar(N):
    soma = 0
    h = 2/N
    for k in range(N):
        x_k = -1 + h*k
        soma += f(x_k)*h
    return soma
print(integrar(100000)
print(np.pi/2)
