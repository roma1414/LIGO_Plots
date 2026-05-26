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
plot_name = 'SNR_gmode.png'#'FFT_vs_Spec_sch.png'
title = '$\log\,B_{gmode,no\,\,gmode}$ vs SNR for G-Mode Classification'#'log Bsn vs Distance for sch_10, Sch PCs'

snr_1 = [27.6, 21.5, 17.6, 14.9, 12.1, 10.8, 9.7, 8.8, 8.1, 7.2]
logBsn_1 = [291, 155, 91, 57, 31, 18, 11, 4.6, 1.18, 0]
snr_2 = [24.1, 16.1, 12.1, 9.7, 8.8]
logBsn_2 = [100, 31, 7, .2,.05]
snr_3 = [25.4, 20.5, 17.2, 14.8, 13, 11.6, 10.4, 8.7, 8.3]
logBsn_3 = [158, 89, 54, 36, 24, 15, 5.51, .07, 0]
snr_4 = [15.1, 13.4, 11.1, 9.4, 8.2, 7.3, 6.9, 6.5, 5.9, 5.5]
logBsn_4 = [73, 57, 37, 23, 12, 5.5, 3, .9, .08, 0]
snr_5 = [6.5, 7.5, 8, 9, 10, 12, 14, 15.5]
logBsn_5 = [0, .25, .75, 4, 10, 23, 36, 50]
#snr_5 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
#snr_5.reverse()
#logBsn_5 = [822.368233355991, 774.5188472618707, 727.0351526571121, 679.5514580523534, 632.0677634475946, 584.584068842836, 537.3009821408128, 490.06804741447365, 444.0860469664849, 409.6357469491167, 375.82312809116877, 342.01050923322083, 308.1978903752729, 274.5494816551202, 244.58716032608692, 219.57923460144926, 195.59616477272726, 177.14114583333333, 158.6861268939394, 140.23110795454545, 121.77608901515151, 105.52771990740742, 90.22505787037038, 75.1890625, 62.765542763157896, 50.253966346153845, 36.949879807692305, 26.4765625, 16.0546875, 8.263461538461538, 4.291666666666668, 2.3365384615384617, 2.28409090909091, 0.5500000000000007, -6.75]
#logBsn_5 = [822.368233355991, 774.5188472618707, 727.0351526571121, 679.5514580523534, 632.0677634475946, 584.584068842836, 537.3009821408128, 490.06804741447365, 444.0860469664849, 409.6357469491167, 375.82312809116877, 342.01050923322083, 308.1978903752729, 274.5494816551202, 244.58716032608692, 219.57923460144926, 195.59616477272726, 177.14114583333333, 158.6861268939394, 140.23110795454545, 121.77608901515151, 105.52771990740742, 90.22505787037038, 75.1890625, 62.765542763157896, 50.253966346153845, 36.949879807692305, 26.4765625, 16.0546875, 8.263461538461538, 4.291666666666668, 3, 0]
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

plt.plot(snr_1, logBsn_1, 'g-', zorder = 8, label='sfhx*')
print('1')
plt.plot(snr_2, logBsn_2, 'r-', zorder = 7, label='s18')
print('2')
plt.plot(snr_3, logBsn_3, 'b-', zorder = 6, label='L15* (no g-mode)')
print('3')
plt.plot(snr_4, logBsn_4, 'y-', zorder = 5, label='N20 (no g-mode)')
print('4')
plt.plot(snr_5, logBsn_5, 'k-', zorder = 4, label='Mean')
print('5')
'''plt.plot(snr_6, logBsn_6, 'm-', zorder = 3, label='Yakunin2017_C15')
print('6')
plt.plot(snr_mean, mean, 'c-', zorder = 2, label='Mean')
print('7')'''

line_x = [.000001, 99999]
line_y_2 = [8, 8]
plt.plot(line_x, line_y_2, 'c-', zorder = 1)

#plt.plot(line[0], line[1], color='g', linestyle='-', linewidth=2)#, label='Full Data\nSlope = ' + rounding(full_slope, precision) + '\np = ' + rounding(full_p_value, precision), alpha=0.5, zorder=10)


plt.xlim([3, 20])
plt.ylim([0, 50])
plt.xlabel('Injection SNR', fontsize=18)
plt.ylabel('$\log\,B_{gmode,no\,\,gmode}$', fontsize=18)#'Efficiency')
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








