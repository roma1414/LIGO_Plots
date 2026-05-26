# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:02:27 2018

@author: Asus
"""

import numpy as np
import scipy
import scipy.signal

'''a = []
avg = 0

for i in range(1000):
    x = np.random.normal(0, 10)
    y = np.random.normal(0, 10)
    a.append(x**2 + y**2)
    
for i in range(len(a)):
    avg += a[i]
    
avg /= len(a)

print('average value = ' + str(avg))
'''

dt = 4096.0**-1

data = []
for i in range(12288):
    data.append(np.random.normal(0, 10))
    
data = np.array(data)

x = np.fft.fft(data, n=12288)
f = np.fft.fftfreq(data.shape[-1])
#f, psd = scipy.signal.welch(data, fs=4096, window=None, nperseg=12288, noverlap=0, return_onesided=True, scaling='density')

print('f = 1000    ' + str(2 * dt**2 * x[1000] * np.conj(x[5]) / 3))
print('f = 2000    ' + str(2 * dt**2 * x[2000] * np.conj(x[2000]) / 3))
print('f = 3500    ' + str(2 * dt**2 * x[3500] * np.conj(x[3500]) / 3))
print('f = 5000    ' + str(2 * dt**2 * x[5000] * np.conj(x[5000]) / 3))
print('f = 6000    ' + str(2 * dt**2 * x[6000] * np.conj(x[6000]) / 3))

