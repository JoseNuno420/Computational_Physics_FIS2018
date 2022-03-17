import numpy as np
import vpython as vp

# 1
vp.canvas()
L = 5
R = 0.3
count = 1
for i in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1):
            if count %2 == 0:
                vp.sphere(pos=vp.vector(i,j,k),radius=R,color=vp.color.blue)
            else:
                vp.sphere(pos=vp.vector(i,j,k),radius=R,color=vp.color.red)
            count += 1

# 2
vp.canvas()
L = 5
R = 0.2
count = 1
for i in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1): 
            vp.sphere(pos=vp.vector(i,j,k),radius=R,color=vp.color.blue)
            vp.sphere(pos=vp.vector(i+0.5,j+0.5,k),radius=R,color=vp.color.blue)
            vp.sphere(pos=vp.vector(i+0.5,j,k+0.5),radius=R,color=vp.color.blue)
            vp.sphere(pos=vp.vector(i,j+0.5,k+0.5),radius=R,color=vp.color.blue)
