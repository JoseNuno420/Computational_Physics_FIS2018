import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def reator(t,CT):
    #definimos CT como sendo uma lista 
    #CT[0] = valor inicial de C
    #CT[1] = valor inicial de T
    dCdT = [-CT[0]*np.exp(-10/(CT[1]+273)),-1000*(-CT[0]*np.exp(-10/(CT[1]+273)))-5*(CT[1]-20)]
    return dCdT

CT0 = [1.0,15] #C0 = 1.0 & T0 = 15 ºC
ts = [0,5] #range dos tempos
sol = solve_ivp(reator,ts,CT0) #calcular a soluçao

CT = sol.y

C = CT[0,:] #solucao de C
T = CT[1,:] #solucao de T
t = sol.t #vector do tempo

#plots separados devido a diferença de escalas nos yys
plt.figure(figsize=(15,7))

ax1 =plt.subplot(1,2,1)
ax1.plot(t,C,color='r')
plt.xlabel("Tempo(minutos)")
plt.ylabel("Concentração")

ax2 = plt.subplot(1,2,2)
ax2.plot(t,T,color='b')
plt.xlabel("Tempo(minutos)")
plt.ylabel("Temperatura")
plt.show()
