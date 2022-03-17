import numpy as np
import matplotlyb.pyplot as plt

x,y = np.mgrid[-2:2:100j,-2:2:100j]

c = x + y*1j

def mandelbort(c,n=100):
    z = 0
    for i in range(n):
        z = c + z**2
    z2 = np.sqrt(z*z.conjugate())
    return z2 < 2

plt.imshow(mandelbort(c),plt.cm.jet)
