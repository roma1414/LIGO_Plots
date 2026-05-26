from __future__ import division
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import splrep,splev
import scipy.signal as sig
import sys

# Some contants
fs = 4096.0
freq_N = 65
df = (fs / 2.0) / (freq_N - 1)
dt = fs**-1
duration = 3.0
N_t = 191 #63
N_spec = N_t * freq_N #936 * 65 # len(t) * len(f)
Nperseg = 128 #384
nperseg = 128 #128
Noverlap = 64 #192
noverlap = 0 #115
flow = 30
t_min = .95#.999
t_max = 2.0 #1.11
num_PCs = 6
SMEE_recon_name = 'inj_1.png'
recon_log_hrss = -49.1821060782
recon_hrss = np.exp(recon_log_hrss)
timeshift = 0.0
time = 1134913935.96
BETAS = [419.631001426, -91.9389255221, 40.6133088168, -137.597994875, 22.989317966, -53.7086727041]
#BETAS = [i * 6.1535136e-23 for i in BETAS]
duration_threshold = 5 * 10**-24

w_dir = '/home/vincent.roma/public_html/SMEE/time_series/'
#plot_dir = '/home/vincent.roma/public_html/SMEE/plots/'
out_dir = '/home/vincent.roma/public_html/SMEE/spec_PCs/neu_recon/'

waveforms = ['Andresen2016_s11.txt', 'cross_Andresen2016_s11.txt', 'Andresen2016_s20.txt', 'cross_Andresen2016_s20.txt', 'Andresen2016_s20s.txt', 'cross_Andresen2016_s20s.txt', 'Andresen2016_s27.txt', 'cross_Andresen2016_s27.txt', 'Mueller2012_L15-3.txt', 'cross_Mueller2012_L15-3.txt', 'Mueller2012_N20-2.txt', 'cross_Mueller2012_N20-2.txt', 'Mueller2012_W15-4.txt', 'cross_Mueller2012_W15-4.txt', 'Kuroda2016_sfhx.txt', 'cross_Kuroda2016_sfhx.txt', 'Kuroda2016_tm1.txt', 'cross_Kuroda2016_tm1.txt', 'Powell2018_he3pt5.txt', 'cross_Powell2018_he3pt5.txt', 'Powell2018_s18.txt', 'cross_Powell2018_s18.txt', 'mesa20_LR_gw.txt', 'cross_mesa20_LR_gw.txt', 'mesa20_gw.txt', 'cross_mesa20_gw.txt', 'mesa20_pert_LR_gw.txt', 'cross_mesa20_pert_LR_gw.txt', 'mesa20_pert_gw.txt', 'cross_mesa20_pert_gw.txt', 'mesa20_v_LR_gw.txt', 'cross_mesa20_v_LR_gw.txt']

# True All
#['Andresen2016_s11.txt', 'cross_Andresen2016_s11.txt', 'Andresen2016_s20.txt', 'cross_Andresen2016_s20.txt', 'Andresen2016_s20s.txt', 'cross_Andresen2016_s20s.txt', 'Andresen2016_s27.txt', 'cross_Andresen2016_s27.txt', 'Mueller2012_L15-3.txt', 'cross_Mueller2012_L15-3.txt', 'Mueller2012_N20-2.txt', 'cross_Mueller2012_N20-2.txt', 'Mueller2012_W15-4.txt', 'cross_Mueller2012_W15-4.txt', 'Kuroda2016_sfhx.txt', 'cross_Kuroda2016_sfhx.txt', 'Kuroda2016_tm1.txt', 'cross_Kuroda2016_tm1.txt', 'Yakunin2017_C15.txt', 'cross_Yakunin2017_C15.txt', 'Powell2018_he3pt5.txt', 'cross_Powell2018_he3pt5.txt', 'Powell2018_s18.txt', 'cross_Powell2018_s18.txt', 'Kuroda2017_S11.txt', 'cross_Kuroda2017_S11.txt', 'Kuroda2017_S15.txt', 'cross_Kuroda2017_S15.txt', 'Ott2013_s27_00.txt', 'cross_Ott2013_s27_00.txt', 'Ott2013_s27_05.txt', 'cross_Ott2013_s27_05.txt', 'Ott2013_s27_1.txt', 'cross_Ott2013_s27_1.txt', 'Ott2013_s27_15.txt', 'cross_Ott2013_s27_15.txt', 'mesa20_LR_gw.txt', 'cross_mesa20_LR_gw.txt', 'mesa20_gw.txt', 'cross_mesa20_gw.txt', 'mesa20_pert_LR_gw.txt', 'cross_mesa20_pert_LR_gw.txt', 'mesa20_pert_gw.txt', 'cross_mesa20_pert_gw.txt', 'mesa20_v_LR_gw.txt', 'cross_mesa20_v_LR_gw.txt']

# Review Neutrino
#['Andresen2016_s11.txt', 'cross_Andresen2016_s11.txt', 'Andresen2016_s20.txt', 'cross_Andresen2016_s20.txt', 'Andresen2016_s20s.txt', 'cross_Andresen2016_s20s.txt', 'Andresen2016_s27.txt', 'cross_Andresen2016_s27.txt', 'Mueller2012_L15-3.txt', 'cross_Mueller2012_L15-3.txt', 'Mueller2012_N20-2.txt', 'cross_Mueller2012_N20-2.txt', 'Mueller2012_W15-4.txt', 'cross_Mueller2012_W15-4.txt', 'Kuroda2016_sfhx.txt', 'cross_Kuroda2016_sfhx.txt', 'Kuroda2016_tm1.txt', 'cross_Kuroda2016_tm1.txt', 'Powell2018_he3pt5.txt', 'cross_Powell2018_he3pt5.txt', 'Powell2018_s18.txt', 'cross_Powell2018_s18.txt', 'mesa20_LR_gw.txt', 'cross_mesa20_LR_gw.txt', 'mesa20_gw.txt', 'cross_mesa20_gw.txt', 'mesa20_pert_LR_gw.txt', 'cross_mesa20_pert_LR_gw.txt', 'mesa20_pert_gw.txt', 'cross_mesa20_pert_gw.txt', 'mesa20_v_LR_gw.txt', 'cross_mesa20_v_LR_gw.txt']

# Two left out, crosses
#['Andresen2016_s11.txt', 'cross_Andresen2016_s11.txt', 'Andresen2016_s20.txt', 'cross_Andresen2016_s20.txt', 'Andresen2016_s27.txt', 'cross_Andresen2016_s27.txt', 'Mueller2012_L15-3.txt', 'cross_Mueller2012_L15-3.txt', 'Mueller2012_N20-2.txt', 'cross_Mueller2012_N20-2.txt', 'Mueller2012_W15-4.txt', 'cross_Mueller2012_W15-4.txt', 'Kuroda2016_tm1.txt', 'cross_Kuroda2016_tm1.txt', 'Yakunin2017_C15.txt', 'cross_Yakunin2017_C15.txt', 'Powell2018_s3pt5si.txt', 'cross_Powell2018_s3pt5si.txt', 'Powell2018_s18.txt', 'cross_Powell2018_s18.txt']

# g_mode ["Andresen2016_s11.txt", "cross_Andresen2016_s11.txt", "Andresen2016_s20.txt", "cross_Andresen2016_s20.txt", "Andresen2016_s27.txt", "cross_Andresen2016_s27.txt", 'Kuroda2016_sfhx.txt', 'cross_Kuroda2016_sfhx.txt', "Kuroda2016_tm1.txt", "cross_Kuroda2016_tm1.txt", "Powell2018_he3pt5.txt", "cross_Powell2018_he3pt5.txt", "Powell2018_s18.txt", "cross_Powell2018_s18.txt", 'mesa20_gw.txt', 'cross_mesa20_gw.txt', 'mesa20_LR_gw.txt', 'cross_mesa20_LR_gw.txt', 'mesa20_pert_gw.txt', 'cross_mesa20_pert_gw.txt', 'mesa20_pert_LR_gw.txt', 'cross_mesa20_pert_LR_gw.txt', 'mesa20_v_LR_gw.txt', 'cross_mesa20_v_LR_gw.txt']

# no g-mode ["Andresen2016_s20.txt", "cross_Andresen2016_s20.txt", "Andresen2016_s20s.txt", "cross_Andresen2016_s20s.txt", "Andresen2016_s27.txt", "cross_Andresen2016_s27.txt", "Yakunin2017_C15.txt", "cross_Yakunin2017_C15.txt", 'Mueller2012_L15-3.txt', 'cross_Mueller2012_L15-3.txt', "Mueller2012_N20-2.txt", "cross_Mueller2012_N20-2.txt"]

# SASI ["Andresen2016_s20.txt", "cross_Andresen2016_s20.txt", "Andresen2016_s20s.txt", "cross_Andresen2016_s20s.txt", "Andresen2016_s27.txt", "cross_Andresen2016_s27.txt", "Kuroda2016_sfhx.txt", "cross_Kuroda2016_sfhx.txt", "Mueller2012_L15-3.txt", "cross_Mueller2012_L15-3.txt", "Mueller2012_N20-2.txt", "cross_Mueller2012_N20-2.txt", "Yakunin2017_C15.txt", "cross_Yakunin2017_C15.txt", 'mesa20_gw.txt', 'cross_mesa20_gw.txt', 'mesa20_LR_gw.txt', 'cross_mesa20_LR_gw.txt', 'mesa20_pert_gw.txt', 'cross_mesa20_pert_gw.txt', 'mesa20_pert_LR_gw.txt', 'cross_mesa20_pert_LR_gw.txt']

# no SASI ["Andresen2016_s11.txt", "cross_Andresen2016_s11.txt", "Kuroda2016_tm1.txt", "cross_Kuroda2016_tm1.txt", "Powell2018_he3pt5.txt", "cross_Powell2018_he3pt5.txt", 'Powell2018_s18.txt', 'cross_Powell2018_s18.txt']

def spec(t_data):
    advance = Nperseg - Noverlap
    #Sxx = np.zeros((65, 628), float)
    Sxx = np.ndarray(shape=(freq_N, N_t), dtype=float)
    df = 2048 / (freq_N - 1)
    freqs = np.ndarray(shape=(freq_N,)) * df
    advance_t = advance / fs
    times = np.ndarray(shape=(N_t,), dtype=float)
    for t in range(N_t):
        times[t] = t * advance_t + .5 * Nperseg / fs
        start = advance * t
        stop = start + Nperseg
        data = t_data[start:stop]
        freqs, Pxx = sig.welch(data, fs=fs, window='hann', nperseg=nperseg, noverlap=noverlap, return_onesided=True, scaling='density')
        for f in range(freq_N):
            Sxx[f][t] = Pxx[f]
    #print('length of f = ' + str(len(f)) + ' , length of Pxx = ' + str(len(Pxx)) + ', length of Sxx = ' + str(len(Sxx)))
    return freqs, times, Sxx

def circshift(in_spec, num_of_ffts, fs, timeshift):
    timeshift_n = 0
    #fft_N = (freq_N - 1) * 2
    #advance = fft_N - overlap
    advance = Nperseg - Noverlap
    
    deltaT = advance / fs

    result = np.copy(in_spec)

    if (timeshift >= 0):
        timeshift_n = int((timeshift / deltaT) + .5)
    else:
        timeshift_n = int((timeshift / deltaT) - .5)

    if (timeshift_n >= 0):
        for f in range(freq_N):
            for t in range(timeshift_n, num_of_ffts):
                result[f][t] = in_spec[f][t-timeshift_n]
            for t in range(timeshift_n):
                result[f][t] = in_spec[f][num_of_ffts-timeshift_n+t]
    else:
        timeshift_n *= -1
        for f in range(freq_N):
            for t in range(num_of_ffts - timeshift_n):
                result[f][t] = in_spec[f][t+timeshift_n]
            for t in range(timeshift_n):
                result[f][num_of_ffts-timeshift_n+t] = in_spec[f][t]

    return result

numWfs = len(waveforms)
Avec = np.zeros((N_spec, numWfs), float)
times = np.array([dt * i for i in range(int(duration * fs))])

bHP, aHP = sig.cheby1(4, 3, flow / (fs / 2), btype='highpass')
bHP2, aHP2 = sig.cheby1(4, 3, 255.0 / (fs / 2), btype='lowpass')

'''w = 0
for n in range(nperseg):
    #w += (.54 - .46 * np.cos(2 * np.pi * n / (nperseg - 1)))**2  #Hamming
    w += (.5 - .5 * np.cos(2 * np.pi * n / (nperseg - 1)))**2   # Hann
winNorm = (w / nperseg)**.5
#winNorm = w**.5
print('winnorm = ' + str(winNorm))'''

f_spec = np.array([])
t_spec = np.array([])
# Loop through waveforms
for i in range(0, numWfs):
    name = waveforms[i]
    # Load data
    t_data = np.loadtxt(w_dir + name)[:,0]
    '''for n in range(int(duration * fs)):
        t_data[n] *= (10.0 / 2)# * 2**.5'''
    #t_data = np.pad(t_data, 4096, 'constant')
    t_data = sig.filtfilt(bHP, aHP, t_data, axis=-1)
    #t_data = t_data[4096:16384]
    #print('t_data length = ' + str(len(t_data)))
    '''if (i < 8):
        t_data = sig.filtfilt(bHP2, aHP2, t_data, axis=-1)'''
    #f, t, Sxx = sig.spectrogram(t_data, fs=fs, window='hann', nperseg=nperseg, noverlap=Noverlap, mode='psd')
    f, t, Sxx = spec(t_data)

    #print('t[0] = ' + str(t[0]) + '    t[1] = ' + str(t[1]))
    hrss = 0.0
    max_amp = 0
    initial_t = 0
    final_t = 0
    for n in range(12288):
        hrss += t_data[n]**2
        if initial_t == 0 and t_data[n] != 0:
            initial_t = n
        if initial_t != 0 and final_t == 0 and t_data[n] == 0:
            final_t = n - 1
        if np.absolute(t_data[n]) > max_amp:
            max_amp = np.absolute(t_data[n])

    hrss *= 1.0 / 4096.0
    hrss = hrss**.5
    loghrss = np.log(hrss)
    print('Name = ' + name)
    print 'hrss = %e' % hrss,
    print '    loghrss = %f' % loghrss
    
    Sxx = Sxx**.5

    max_test = 0.0
    max_f = 0
    max_t = 0
    for g in range(freq_N):
        for u in range(N_t):
            if Sxx[g][u] > max_test:
                max_test = Sxx[g][u]
                max_f = g
                max_t = u
    #print('Max amp = ' + str(max_amp) + '   Max ASD = ' + str(max_test) + '   max_f = ' + str((f[1] - f[0]) * max_f) + ' Hz   duration = ' + str((final_t - initial_t) * (1.0 / fs)))

    plt.pcolormesh(t, f, Sxx, cmap='jet')
    plt.colorbar()
    plt.title(name[:-4], fontsize=20)
    plt.ylabel('Frequency [Hz]', fontsize=18)
    plt.xlabel('Time [sec]', fontsize=18)
    plt.xlim([t_min, t_max])
    plt.ylim([0, fs * .5])
    plt.savefig(out_dir + 'spectrogram_' + name[:-4] + '.png')
    plt.close()

    plt.plot(times, t_data, '-r')
    plt.title(name[:-4])
    plt.ylabel('Amplitude [strain]')
    plt.xlabel('Time [sec]')
    plt.xlim([t_min, t_max])
    plt.savefig(out_dir + 'time_' + name[:-4] + '.png')
    plt.close()

    data = np.array([])

    for j in range(len(t)):
        col = Sxx[:,j]        
        data = np.concatenate((data, col))

    Avec[:,i] = data[:]
    #Avec[i,:] = data[:]
    if (i + 1) == numWfs:
        f_spec = f
        t_spec = t

U, s, V = np.linalg.svd(Avec, full_matrices=False)

recon_betas = []
for i in range(numWfs):
    recon_betas.append([])

Sxx = np.zeros((freq_N, N_t), float)
Sxx_rec = np.zeros((freq_N, N_t), float)
for i in range(len(U[0])):
    PC_vector = U[:, i]
    for j in range(N_t):
        Sxx[:,j] = PC_vector[freq_N*j:freq_N*(j+1)]
    #Sxx *= -1 # Make PCs negative #############################################

    if i < num_PCs:
        Sxx_rec = Sxx_rec + BETAS[i] * Sxx

    for j in range(numWfs):
        recon_betas[j].append(np.dot(PC_vector, Avec[:,j]))

    plt.pcolormesh(t_spec, f_spec, Sxx, cmap='jet')
    plt.colorbar()
    plt.title('PC ' + str(i+1), fontsize=20)
    plt.ylabel('Frequency [Hz]', fontsize=18)
    plt.xlabel('Time [sec]', fontsize=18)
    plt.xlim([t_min, t_max])
    plt.ylim([0, fs * .5])
    plt.savefig(out_dir + 'spectrogram_neu_PC_' + str(i+1) + '.png')
    plt.close()

Sxx_rec = Sxx_rec
Sxx_rec = np.absolute(Sxx_rec)

avg = [0.0] * freq_N
avg = np.array(avg)
hrss = 0.0
for y in range(N_t):
    for n in range(freq_N):
        avg[n] = avg[n] + Sxx_rec[n][y]**2
for n in range(freq_N):
    avg[n] = avg[n] / float(N_t)
    hrss += avg[n]
hrss *= 32.0
hrss = hrss**.5
factor = recon_hrss / hrss
print('hrss = ' + str(hrss))
print('recon_hrss = ' + str(recon_hrss))
print('factor = ' + str(factor))
for n in range(freq_N):
    for y in range(N_t):
        Sxx_rec[n][y] *= factor

Sxx_rec = circshift(Sxx_rec, N_t, 4096.0, timeshift)

print('\nReconstruction from PCs:')
# find peak frequency from reconstruction
max_sum = 0
max_f = 0
for f in range(freq_N):
    the_sum = 0
    for t in range(N_t):
        the_sum += Sxx_rec[f][t]
    if the_sum > max_sum:
        max_sum = the_sum
        max_f = f
print('Peak frequency (total emission) = ' + str(max_f * df))

# find duration
t_start = 0
t_end = 0
t = 0
temp_data = []
while (t_start == 0 and t < N_t):
    for f in range(freq_N):
        if (Sxx_rec[f][t] > duration_threshold):
            t_start = t
    t += 1
while (t_end == 0 and t < N_t):
    for f in range(freq_N):
        temp_data.append(Sxx_rec[f][t])
    if (max(temp_data) < duration_threshold):
        t_end = t
    #print(str(max(temp_data)))
    t += 1
    temp_data = []
#print('t_start = ' + str(t_spec[t_start]))
#print('t_end = ' + str(t_spec[t_end]))
duration = t_spec[t_end] - t_spec[t_start]
print('Duration = ' + str(duration))

# plot Reconstruction
rec_t_spec = [entry + time for entry in t_spec]
plt.pcolormesh(rec_t_spec, f_spec, Sxx_rec, cmap='jet')#, vmin=0.0, vmax=2.70922578059e-24)
plt.colorbar()
plt.title('Reconstruction from PCs', fontsize=20)
plt.ylabel('Frequency [Hz]', fontsize=18)
plt.xlabel('Time [sec]', fontsize=18)
plt.xlim([t_min + time, t_max + time])
plt.ylim([0, fs * .5])
plt.savefig(out_dir + SMEE_recon_name)#2_sch_14_5kpc.png')
plt.close()

for w in range(numWfs):
    Sxx = np.zeros((freq_N, N_t), float)
    for p in range(len(U[0])):
        PC_vector = U[:, p]
        for j in range(N_t):
            Sxx[:,j] += recon_betas[w][p] *  PC_vector[freq_N*j:freq_N*(j+1)]

    plt.pcolormesh(t_spec, f_spec, Sxx, cmap='jet')
    plt.colorbar()
    plt.title('Neutrino Waveform ' + str(w+1))
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.xlim([t_min, t_max])
    plt.ylim([0, fs * .5])
    plt.savefig(out_dir + 'reconstruction_neu_' + str(w+1) + '.png')
    plt.close()

recon_matrix = []
for i in range(numWfs):
    recon_matrix.append(recon_betas[i])

recon_matrix = np.array(recon_matrix)
np.savetxt(out_dir + 'PCs.txt', recon_matrix)

dat_file = open(out_dir + 'neu_spec.dat', 'wb')
pc_matrix = U + 0j
dat_file.write(pc_matrix)
dat_file.close()

