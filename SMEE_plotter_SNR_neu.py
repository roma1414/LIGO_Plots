# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 14:37:47 2017

@author: Vincent
"""

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

#plot_name = '1det_eff_sch_edited.png'
plot_name = 'SNR_neu.png'#'FFT_vs_Spec_sch.png'
title = '$\log\,B_{neu,mag}$ vs SNR for Neutrino Catalog'#'log Bsn vs Distance for sch_10, Sch PCs'

'''distances_aLigo = [.2, 1, 2, 4, 5, 7, 10, 15, 25, 50, 75, 100, 150, 200]
distances_Aplus = [.2, 1, 2, 5, 10, 15, 25, 50, 100, 200, 300, 400, 450]
distances_voyager = [.2, 5, 10, 25, 35, 50, 75, 100, 150, 400, 500, 600]
distances_CE = [10, 25, 75, 100, 200, 400, 500, 750, 1000, 1500]'''

#dist_spec = [2, 3, 4, 5, 6, 7, 8]
#dist_FFT = [10, 20, 30, 40, 50]
'''asd = [5e-23, 2e-23, 2e-23, 3e-23, 7e-23]
psd = [x**2 for x in asd]
#asd = [entry * 10**-23 for entry in asd]
logBsn_spec = []
c = []

for f in range(len(dist_spec)):
    a = np.random.normal(0, psd[f]**.5, 10000)
    #a = sum(a) / 10000
    a = [x**2 for x in a]
    #b = np.random.normal(0, (psd[f] / 2)**.5, 10000)
    #b = [x**2 for x in b]
    #b = sum(b) / 10000
    c = sum(a) / len(a)
    logBsn_spec.append(c**.5)
    
print(logBsn_spec)'''

snr_1 = [25.3, 19.2, 16.5, 12.9, 11.1, 9.8, 9.2, 8.5]
logBsn_1 = [218, 68, 45, 22, 9.5, 2, .45, 0]
snr_2 = [31.6, 19, 13.5, 10.5, 9.5, 8.6, 8]
logBsn_2 = [439, 122, 44, 13, 4.85, .54, 0]
snr_3 = [26.8, 22, 18.6, 16.1, 15.1, 14.2, 13.5, 12.7, 12.1, 11]
logBsn_3 = [124, 63, 33, 16.4, 10.78, 5.7, 2.8, .63, .1, 0]
snr_4 = [30, 26.7, 24.1, 20.1, 17.3, 16.5, 15.1, 15]
logBsn_4 = [27, 18.6, 13, 5.6, .6, .2, .02, 0]
snr_5 = [9, 10, 11, 12, 14, 15, 16, 18, 20.5]
logBsn_5 = [0, 1, 2, 3.5, 9, 14, 22, 36, 50]
'''logBsn_6 = [819, 509, 319, 209, 136, 87, 56, 34.4, 19.1, 8.57, 1.93, -.74]
snr_6 = [20.4, 17.6, 15.5, 13.8, 12.5, 11.4, 10.5, 9.67, 9, 8.41, 7.9, 7.4]
snr_mean = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20]
mean = [-0.8650000000000001, -0.8650000000000001, -0.8650000000000001, -0.8650000000000001, -0.8650000000000001, -0.8650000000000001, 3.8325555555555564, 12.88924836601307, 29.098665762098587, 53.24165334734756, 96.02370370185184, 146.05054542424242, 203.5164835934066, 269.6134518224468, 345.85033231083844, 433.8800378937197, 527.7863526808143, 636.8551588042328, 755.2744709365079, 872.1629188712523]
'''

line_x = [.000001, 99999]
line_y_2 = [8, 8]

plt.figure(figsize=(9,6))
plt.title(title, fontsize=20, y = 1.05)

'''plt.semilogx(distances_2D, eff_rr_2D, 'bo-', zorder = 8, label='RR:2D CE(3)')
plt.semilogx(distances_3D, eff_rr_3D, 'go-', zorder = 7, label='RR:3D CE(3)')
plt.semilogx(distances_2D, eff_neu_2D, 'yo-', zorder = 6, label='Neu:2D CE(3)')
plt.semilogx(distances_3D, eff_neu_3D, 'ro-', zorder = 5, label='Neu:3D CE(3)')
plt.semilogx(distances_3D2, eff_rr_3D2, 'ko-', zorder = 4, label='RR:3D CE(2)')
plt.semilogx(distances_3D2, eff_neu_3D2, 'mo-', zorder = 3, label='Neu:3D CE(2)')'''

plt.plot(snr_1, logBsn_1, 'b-', zorder = 8, label='L15')
print('1')
plt.plot(snr_2, logBsn_2, 'g-', zorder = 7, label='sfhx*')
print('2')
plt.plot(snr_3, logBsn_3, 'y-', zorder = 6, label='he3.5')
print('3')
plt.plot(snr_4, logBsn_4, 'm-', zorder = 5, label='s20s*')
print('4')
plt.plot(snr_5, logBsn_5, 'k-', zorder = 4, label='Mean')
print('5')
'''plt.plot(snr_6, logBsn_6, 'm-', zorder = 3, label='Yakunin2017_C15')
print('6')
plt.plot(snr_mean, mean, 'c-', zorder = 2, label='Mean')
print('7')'''

plt.plot(line_x, line_y_2, 'c-', zorder = 1)

#plt.plot(line[0], line[1], color='c-', linestyle='-', linewidth=2)#, label='Full Data\nSlope = ' + rounding(full_slope, precision) + '\np = ' + rounding(full_p_value, precision), alpha=0.5, zorder=10)


plt.xlim([7, 25])
plt.ylim([0, 50])
plt.xlabel('Injection SNR', fontsize=18)
plt.ylabel('$\log\,B_{neu,mag}$', fontsize=18)#'Efficiency')
plt.grid(b=True, which='major',color='0.75',linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor',color='0.85',linestyle='--')
#plt.ticklabel_format(axis = 'y', style = 'sci', scilimits = (-2,2))
#plt.ticklabel_format(axis = 'x', style = 'sci', scilimits = (-2,2))
legend = plt.legend(loc='best', prop={'size':14})
legend.get_frame().set_alpha(0.5)
#plt.legend(loc = 'best')
'''for label in legend.get_texts():
    label.set_fontsize('large')'''
# save and close figure
plt.savefig(plot_name, bbox_inches='tight')
#plt.clf()
plt.close()








