import numpy as np
data = np.loadtxt(r"sunspots.txt")

x = data[:,0]
y = data[:,1]

plt.plot(x,y)
plt.show()

# (2)

X = data[:1001,0]
Y = data[:1001,1]

plt.plot(X,Y)
plt.show()

# (3)

X = data[:1001,0]
Y = data[:1001,1]


def average(y):
    r = 5
    for m in range(-r,r+1):
        sum = y + m
    return (1/(2*r+1)* sum)

plt.plot(X,Y) # blue graph
plt.plot(X,average(Y)) #orange graph
plt.show()
