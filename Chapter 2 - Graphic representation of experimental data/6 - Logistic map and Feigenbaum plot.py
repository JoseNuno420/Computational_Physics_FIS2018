import numpy as np
import matplotlyb.pyplot as plt

values = np.arange(1,4,0.01)
x = np.full_like(values,0.5)

for i in values:
    x = values*x*(1-x)
    plt.scatter(values,x,s=0.1)
plt.ylabel("x")
plt.xlabel("r")

plt.show()
