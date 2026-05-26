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
plot_name = 'SNR_sch.png'#'FFT_vs_Spec_sch.png'
title = '$\log\,B_{mag,neu}$ vs SNR for Magnetorotational Catalog'#'log Bsn vs Distance for sch_10, Sch PCs'

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

snr_1 = [30.2, 19.4, 16.5, 14.3, 12.7, 10.3, 8.7]
logBsn_1 = [260, 82, 50, 31, 19, 4.6, 0]
snr_2 = [36.8, 33.5, 30.8, 28.5, 26.5, 24.8, 23.2]
logBsn_2 = [27, 17.7, 12.7, 7.8, 4.5, 2.63, 0]
snr_3 = [33.6, 28.6, 25, 22.1, 19, 17, 15.6, 14.5, 14]
logBsn_3 = [90, 55, 34, 20, 12.6, 3.1, .57, .17, 0]
snr_4 = [28.8, 23.2, 17.6, 14.7, 12.6, 11.4, 10.1, 8.9, 7, 5, 3]
logBsn_4 = [579, 361, 193, 128, 90, 69.5, 52, 36, 20, 6, 0]
snr_5 = [5, 8, 12, 15, 20, 25, 26]
logBsn_5 = [0, .5, 4, 9, 27, 46, 50]
'''snr_5 = [20.1, 17.4, 15.3, 13.7, 12.3, 11.3, 10.3, 9.57, 8.9, 8.31, 7.81, 7.36, 6.96, 6.6]
logBsn_5 = [794, 507, 337, 221, 147, 100, 66, 45, 28, 16.2, 10.2, 4.85, .38, -.62]
logBsn_6 = [819, 509, 319, 209, 136, 87, 56, 34.4, 19.1, 8.57, 1.93, -.74]
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

'Scheidegger2010_R3E1AC*'
'Scheidegger2010_R4E1FC_L*'
'Scheidegger2010_R3STAC'

plt.plot(snr_1, logBsn_1, 'b-', zorder = 8, label='R2E1AC')
print('1')
plt.plot(snr_2, logBsn_2, 'g-', zorder = 7, label='R3E1AC*')
print('2')
plt.plot(snr_3, logBsn_3, 'y-', zorder = 6, label='R3STAC')
print('3')
plt.plot(snr_4, logBsn_4, 'm-', zorder = 6, label='R4E1FC_L*')
plt.plot(snr_5, logBsn_5, 'k-', zorder = 5, label='Mean')
print('4')

'''plt.plot(snr_5, logBsn_5, 'k-', zorder = 4, label='Mueller2012_N20-2*')
print('5')
plt.plot(snr_6, logBsn_6, 'm-', zorder = 3, label='Yakunin2017_C15')
print('6')
plt.plot(snr_mean, mean, 'c-', zorder = 2, label='Mean')
print('7')'''

plt.plot(line_x, line_y_2, 'c-', zorder = 1)
#plt.plot(line[0], line[1], color='c-', linestyle='-', linewidth=2)#, label='Full Data\nSlope = ' + rounding(full_slope, precision) + '\np = ' + rounding(full_p_value, precision), alpha=0.5, zorder=10)


plt.xlim([2, 30])
plt.ylim([0, 50])
plt.xlabel('Injection SNR', fontsize=18)
plt.ylabel('$\log\,B_{mag,neu}$', fontsize=18)#'Efficiency')
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








