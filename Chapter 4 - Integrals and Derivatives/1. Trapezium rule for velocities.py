import numpy as np
import matplotlib.pyplot as plt

def integral(data):
    N = len(data)
    h = (data[-1] - data[0])/N
    sum = 0.5*data[0] + 0.5*data[-1]
    for k in range(N):
        sum += (data[k])
    return sum

data = np.loadtxt(r"velocities.txt")

t = data[:,0]
velocities = data[:,1]

distance = integral(velocities)
distance_per_time = np.linspace(0,distance,len(t))

plt.plot(t,velocities)#orange
plt.plot(t,distance_per_time)#blue
plt.xlabel("Time")
plt.ylabel("Distance per time unit(orange) / Velocity (blue)")
plt.show()

