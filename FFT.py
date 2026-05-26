# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 17:38:08 2017

@author: Vincent
"""

import numpy as np

def DFT_slow(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

def FFT(x):
    """A recursive implementation of the 1D Cooley-Tukey FFT"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    print('N = ' + str(N))    

    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:  # this cutoff should be optimized
        return DFT_slow(x)
    else:
        X_even = FFT(x[::2])
        print('length of X_even = ' + str(len(X_even)))
        X_odd = FFT(x[1::2])
        print('length of X_odd = ' + str(len(X_odd)))
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        print('factor length = ' + str(len(factor)))
        return np.concatenate([X_even + factor[:N / 2] * X_odd,
                               X_even + factor[N / 2:] * X_odd])
        
        
z = np.random.random(256)
a = np.asarray([1, 2, 3])
b = np.asarray([1, 1, 2])
N = 16
c = np.arange(N)
d = c[N/2:]
print(d)
FFT(z)




































