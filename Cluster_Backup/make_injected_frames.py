from __future__ import division
import numpy as np
import scipy.signal as sig
import sys
from py_help import *

Fplus = 0.857067 # LHO: -0.878705 # LLO: 0.857067
Fcross = -0.878705 # LHO: -0.0211554 # LLO: -0.878705
injection_times = [1134913937, 1134913997, 1134914057, 1134914117, 1134914177, 1134914237, 1134914297, 1134914357, 1134914417, 1134914477] #1128230297
# Shift them so times above are their core bounce times
injection_times = [entry - 1.0 for entry in injection_times]
injection_dist = [0.2, 0.5, 2.0, 1.0, 1.5, 0.5, 5.0, 6.0, 6.0, 7.0]
waveform_dir = '/home/vincent.roma/public_html/SMEE/time_series/'
waveforms = ['Andresen2016_s11.txt', 'Andresen2016_s27.txt', 'Kuroda2016_sfhx.txt', 'Mueller2012_L15-3.txt', 'Powell2018_s18.txt', 'mesa20_pert_gw.txt', 'Scheidegger2010_R2E3AC.txt', 'Scheidegger2010_R3E1AC_L.txt', 'Scheidegger2010_R3E1DB.txt', 'Scheidegger2010_R4E1FC_L.txt']
#frame_cache = '/home/vincent.roma/public_html/SMEE/caches/pre_injection_A+_2.cache'
out_frame_dir = '/home/vincent.roma/public_html/SMEE/frames/SN_injections/LLO/'
frame_name = 'L-L1_HOFT_C00-1134913817-4096.gwf'
#frame_name = 'L-L1_HOFT_C00-1134913817-4096.gwf'
fs = 4096.0

#data = TimeSeries.read(frame_cache, 'L1:GDS-CALIB_STRAIN')
print('Getting data...')
data = TimeSeries.fetch('L1:GDS-CALIB_STRAIN', 1134913817, 1134914717)
data = data.resample(4096)

def inject(h_plus, h_cross, fplus, fcross, time):
    start_time = data.times.value[0]
    #print('Start time = ' + str(start_time))
    time_add = time - start_time
    #print('time_add = ' + str(time_add))
    n_add = time_add / (1.0 / fs)
    n_add = int(n_add + .5)
    #print('n_add = ' + str(n_add))
    
    for i in range(12288):
        data.value[n_add + i] += fplus * h_plus[i] + fcross * h_cross[i]

for i in range(len(injection_times)):

    fplus = Fplus * 10.0 / injection_dist[i]
    fcross = Fcross * 10.0 / injection_dist[i]
    waveform_path = waveform_dir + waveforms[i]

    t_data_plus = np.loadtxt(waveform_path)[:,0]
    t_data_cross = np.loadtxt(waveform_path)[:,1]
    print('i = ' + str(i))

    inject(t_data_plus, t_data_cross, fplus, fcross, injection_times[i])

#data = data.crop(start=injection_time-60, end=injection_time+60)

#save_time_series(data, out_frame_dir, frame_type='L1_HOFT_C00')
data.write(out_frame_dir + frame_name, format='gwf')
