import math
def orbit(x):
    l1 = int(input("Distance of planet to Sun"))
    v1 = int(input("Velocity on perineum:"))
    
    M = 1.9891*10**30 #Sun's mass
    G = 6.6738*10**-11 #Gravitational Constant
    
    v2 = (G*M/(v1*l1)) + math.sqrt(((G*M/(v1*l1))**2)+ 2*G*M/l1 - v1)
    l2 = l1*v1/v2
    
    a = 0.5 * (l1 + l2)
    b = math.sqrt(l1*l2)
    T = 2*math.pi*a*b/(l1*v1)
    e = (l2-l1)/(l2+l1)
    
    return ("l2 is",l2," v2 :",v2,"orbital period is:",T," orbital excentricity is:",e)

print(orbit(1))
