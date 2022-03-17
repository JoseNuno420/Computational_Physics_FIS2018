import numpy as np

data = np.loadtxt(r"stm.txt")
plt.imshow(data,origin="lower") #density plot
plt.show()

x = data[:,0]
y = data[:,1]
plt.plot(x,y) # regular xy plot
plt.show()
