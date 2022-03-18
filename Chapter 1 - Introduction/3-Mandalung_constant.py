## Developing a Cubic Lattice on numpy
L = 3
x_val = np.arange(-L,L+1)
y_val = np.arange(-L,L+1)
z_val = np.arange(-L,L+1)

xx,yy,zz = np.meshgrid(x_val, y_val, z_val, indexing='ij')

def dist(x,y,z):
    """Calculates distances.
    """
    
    return 1/np.sqrt(np.power(x, 2) + np.power(y, 2) + np.power(z, 2))


def mandalung_constant(L):
    """Calculates mandalung constant on grin on the center position.
    """
    s = 0
    x = np.arange(L+1)
    y = np.arange(L+1)
    z = np.arange(L+1)
    
    # calculate cube
    xx, yy, zz = np.meshgrid(x[1:], y[1:], z[1:], indexing='ij')
    distances_square =  dist(xx, yy, zz)
    
    sum_coordinates = xx+ yy + zz
    signal = np.ones(np.shape(sum_coordinates), dtype=float) * -1
    signal = np.power(signal, sum_coordinates)
    distances_square = distances_square * signal
    
    s += np.sum(distances_square) * 8
    
    
    # calculate square
    yy, zz = np.meshgrid(y[1:], z[1:], indexing='ij')
    distances_square = dist(0, yy, zz)
    signal = np.power(-1, yy + zz)
    distances_square = distances_square * signal
    
    s += np.sum(distances_square) * 12
    
    
    # calculate line
    distances_line = dist(x[1:], 0, 0)
    signal = np.power(-1, x[1:])
    distances_line = distances_line * signal
    
    s += np.sum(distances_line) * 6
    
    return s

print(mandalung_constant(200))

##########################################################################################
def Mandelung(L):
    plane = np.zeros([L+1,L+1])
    signal = np.zeros([L+1,L+1])
    for i in range (L+1):
        for j in range(L+1):
            plane[i,j] = i**2 + j**2
            signal[i,j] = 1-2*((i+j)%2)
    sum = 0
    
    for k in range(1,L+1):
        sum += np.sum((1-2*(k%2))*signal[1:,1:]/np.sqrt(plane[1:,1:]+k**2))
    
    sum *= 8
    sum += 12*np.sum(signal[1:,1:]/np.sqrt(plane[1:,1:]))
    sum += 6*np.sum(signal[1:,0]/np.sqrt(plane[1:,0]))
    
    print(sum)
    return sum

tempo = %timeit -n1 -r4 -o value=Mandelung(200)
