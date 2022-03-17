import numpy as np
# 1
def deltoid_curve(t):
    thetha = np.linspace(0,2*np.pi,t)
    
    xs = 2*np.cos(thetha) + np.cos(2*thetha)
    ys = 2*np.sin(thetha) - np.sin(2*thetha)
    
    return xs,ys

x,y = deltoid_curve(10000)

plt.plot(x,y)
plt.show()

# 2

def f(r,thetha):
    """
    Transformation from polar coordinates to xy coordinates
    """
    x = r*np.cos(thetha)
    y = r*np.sin(thetha)
    
    return x,y

def spiral(lim,n):
    """
    Create graphic for the galilean spiral
    """
    thetha = np.linspace(0,lim,n) #creates values for thete between 0 and chosen limit
    r = thetha**2
    return r,thetha

r,thetha = spiral(20*np.pi,1000) # obtains spiral in polar coordinates
x,y = f(r,thetha) #changes coordinates types from polar to xx,yy

plt.plot(x,y)
plt.show()

# 3
def frey(lim,n):
    """
    Frey function graphical representation
    """
    thetha = np.linspace(0,lim,n)
    r = np.exp(np.cos(thetha)) - 2*np.cos(4*thetha) + np.sin(thetha/12)**5
    return r,thetha

r,thetha = frey(2*np.pi,1000)
x,y = f(r,thetha)

plt.plot(x,y)
plt.show()
