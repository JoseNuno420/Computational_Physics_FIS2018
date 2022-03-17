import numpy as np

def deltoid_curve(t):
    thetha = np.linspace(0,2*np.pi,t)
    
    xs = 2*np.cos(thetha) + np.cos(2*thetha)
    ys = 2*np.sin(thetha) - np.sin(2*thetha)
    
    return xs,ys

x,y = deltoid_curve(10000)

plt.plot(x,y)
plt.show()
