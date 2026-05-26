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
plot_name = 'SNR_sasi.png'#'FFT_vs_Spec_sch.png'
title = '$\log\,B_{SASI,no\,\,SASI}$ vs SNR for SASI Classification'#'log Bsn vs Distance for sch_10, Sch PCs'

snr_1 = [30, 26.7, 24.1, 20.1, 18.6, 17.3, 16.1, 14.2, 13.5]
logBsn_1 = [24, 17, 11.5, 4.66, 2.09, .64, .14, .037, 0]
snr_2 = [15.8, 13.4, 11.7, 10.3, 9.7, 9.2, 8.8, 8.4, 8, 7.3, 6.9]
logBsn_2 = [90, 50, 26.3, 11.3, 7.4, 3, .84, .33, .14, .03, 0]
snr_3 = [24, 21.4, 17.4, 16.2, 14, 13.1, 11.6, 11.4]
logBsn_3 = [50, 32.7, 17, 11.5, 3.76, 1.7, .03, 0]
snr_4 = [28.3, 24, 20.9, 18.4, 16.5, 15]
logBsn_4 = [80, 43, 21, 10, 2.47, 0]
#snr_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#snr_5.reverse()
#logBsn_5 = [135.00702728643907, 115.83865918873093, 101.14154819355682, 87.59550671709925, 74.04946524064171, 60.27195096868698, 51.36578896869346, 44.32284527660508, 37.265128829789035, 29.11374748346275, 22.576417349726775, 18.601861338797814, 15.108333333333334, 10.911111111111111, 9.0625, 7.99702380952381, 7.5, 5.304545454545455, -1.1655844155844166, -6.75]
snr_5 = [8, 10, 12.5, 15, 17.5, 20, 22.5, 23.5]
logBsn_5 = [0, .5, 2, 8, 18, 27, 42, 50]
'''logBsn_6 = [819, 509, 319, 209, 136, 87, 56, 34.4, 19.1, 8.57, 1.93, -.74]
snr_6 = [20.4, 17.6, 15.5, 13.8, 12.5, 11.4, 10.5, 9.67, 9, 8.41, 7.9, 7.4]
snr_mean = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20]
mean = [-0.8650000000000001, -0.8650000000000001, -0.8650000000000001, -0.8650000000000001, -0.8650000000000001, -0.8650000000000001, 3.8325555555555564, 12.88924836601307, 29.098665762098587, 53.24165334734756, 96.02370370185184, 146.05054542424242, 203.5164835934066, 269.6134518224468, 345.85033231083844, 433.8800378937197, 527.7863526808143, 636.8551588042328, 755.2744709365079, 872.1629188712523]
'''

plt.figure(figsize=(9,6))
plt.title(title, fontsize=20, y = 1.05)

'''plt.semilogx(distances_2D, eff_rr_2D, 'bo-', zorder = 8, label='RR:2D CE(3)')
plt.semilogx(distances_3D, eff_rr_3D, 'go-', zorder = 7, label='RR:3D CE(3)')
plt.semilogx(distances_2D, eff_neu_2D, 'yo-', zorder = 6, label='Neu:2D CE(3)')
plt.semilogx(distances_3D, eff_neu_3D, 'ro-', zorder = 5, label='Neu:3D CE(3)')
plt.semilogx(distances_3D2, eff_rr_3D2, 'ko-', zorder = 4, label='RR:3D CE(2)')
plt.semilogx(distances_3D2, eff_neu_3D2, 'mo-', zorder = 3, label='Neu:3D CE(2)')'''

plt.plot(snr_1, logBsn_1, 'm-', zorder = 8, label='s20s*')
print('1')
plt.plot(snr_2, logBsn_2, 'y-', zorder = 7, label='L15')
print('2')
plt.plot(snr_3, logBsn_3, 'r-', zorder = 6, label='s18* (no SASI)')
print('3')
plt.plot(snr_4, logBsn_4, 'g-', zorder = 5, label='tm1 (no SASI)')
print('4')
plt.plot(snr_5, logBsn_5, 'k-', zorder = 4, label='Mean')
print('5')
'''plt.plot(snr_6, logBsn_6, 'y-', zorder = 3, label='Yakunin2017_C15')
print('6')
plt.plot(snr_mean, mean, 'c-', zorder = 2, label='Mean')
print('7')'''

line_x = [.000001, 99999]
line_y_2 = [8, 8]
plt.plot(line_x, line_y_2, 'c-', zorder = 1)

#plt.plot(line[0], line[1], color='g', linestyle='-', linewidth=2)#, label='Full Data\nSlope = ' + rounding(full_slope, precision) + '\np = ' + rounding(full_p_value, precision), alpha=0.5, zorder=10)


plt.xlim([5, 25])
plt.ylim([0, 50])
plt.xlabel('Injection SNR', fontsize=18)
plt.ylabel('$\log\,B_{SASI,no\,\,SASI}$', fontsize=18)#'Efficiency')
plt.grid(b=True, which='major',color='0.75',linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor',color='0.85',linestyle='--')
#plt.ticklabel_format(axis = 'y', style = 'sci', scilimits = (-2,2))
#plt.ticklabel_format(axis = 'x', style = 'sci', scilimits = (-2,2))
legend = plt.legend(loc='best', prop={'size':14})
legend.get_frame().set_alpha(0.5)
'''plt.legend(loc = 'best')
for label in legend.get_texts():
    label.set_fontsize('large')'''
# save and close figure
plt.savefig(plot_name, bbox_inches='tight')
#plt.clf()
plt.close()








