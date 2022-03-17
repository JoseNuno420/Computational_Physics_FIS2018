import numpy as np
dados = np.loadtxt(r"sunspots.txt")

x = dados[:,0]
y = dados[:,1]

plt.plot(x,y)
plt.show()
