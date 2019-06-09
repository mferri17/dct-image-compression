import numpy as np
from scipy.fftpack import dct

# 1D DCT type-II
def dct1(f):
    f = np.ravel(f)
    c = []
    N = f.size
    alpha = np.pad([1/np.sqrt(N)], (0, N-1), 'constant', constant_values = (np.sqrt(2/N)))

    for k in range(N):
        sum = 0.0

        for index, val in np.ndenumerate(f):
            i = index[0]
            sum += val*np.cos(np.pi*k*(2*i+1)/(2*N))
            
        sum = alpha[k] * sum
        c.append(sum)
  
    return c

# 2D DCT type-II
def dct2(f):

    # Applies DCT1 on both axises of the matrix to compute the 2D DCT
    c = np.apply_along_axis(dct1, 1, np.apply_along_axis(dct1, 0, f))

    return c

        
