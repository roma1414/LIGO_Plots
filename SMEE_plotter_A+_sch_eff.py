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
plot_name = 'sch_A+.png'#'FFT_vs_Spec_sch.png'
title = 'Model Selection Efficiency for Scheidegger Waveforms'#'log Bsn vs Distance for sch_10, Sch PCs'

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

dist_1 = [1, 2, 5, 10, 15, 20, 25, 50, 75, 100, 125]
logBsn_1 = [1, 1, 1, .975, .928, .858, .795, .453, .203, .128, .056]
dist_2 = [1, 2, 5, 10, 15, 20, 50, 100, 150]
logBsn_2 = [1, 1, 1, .994, .989, .967, .711, .294, .128]
'''dist_3 = [1, 2, 5, 10, 15, 20, 50, 75]
logBsn_3 = [1, 1, 1, .975, .925, .861, .447, .197]
dist_4 = [1, 2, 5, 10, 15, 20, 50, 100, 150]
logBsn_4 = [1, 1, 1, .994, .989, .967, .711, .294, .128]'''

'''snr_mean = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20]
mean = [-0.8650000000000001, -0.8650000000000001, -0.8650000000000001, -0.8650000000000001, -0.8650000000000001, -0.8650000000000001, 3.8325555555555564, 12.88924836601307, 29.098665762098587, 53.24165334734756, 96.02370370185184, 146.05054542424242, 203.5164835934066, 269.6134518224468, 345.85033231083844, 433.8800378937197, 527.7863526808143, 636.8551588042328, 755.2744709365079, 872.1629188712523]
'''
'''eff_aLigo = [1, .986, .973, .896, .907, .862, .833, .78, .68, .547, .42, .393, .26, .18]
eff_Aplus = [1, 1, .973, .947, .88, .859, .787, .673, .507, .347, .207, .147, .12]
eff_voyager = [1, .96, .913, .813, .726, .72, .647, .58, .487, .267, .196, .15]
eff_ET_D = [1, 1, 1, 1, 1, 1, .987, .993]
eff_CE = [.987, .973, .883, .864, .76, .653, .62, .54, .427, .333]'''
#eff_CE2 = []

#print(str(len(distances_CE)))
#print(str(len(eff_CE)))

#print(str(len(distances_ET_D)))
#print(str(len(eff_ET_D)))
#line_x = [.000001, 99999]
#line_y = [10, 10]

plt.figure(figsize=(9,6))
plt.title(title, fontsize=20, y = 1.05)

'''plt.semilogx(distances_2D, eff_rr_2D, 'bo-', zorder = 8, label='RR:2D CE(3)')
plt.semilogx(distances_3D, eff_rr_3D, 'go-', zorder = 7, label='RR:3D CE(3)')
plt.semilogx(distances_2D, eff_neu_2D, 'yo-', zorder = 6, label='Neu:2D CE(3)')
plt.semilogx(distances_3D, eff_neu_3D, 'ro-', zorder = 5, label='Neu:3D CE(3)')
plt.semilogx(distances_3D2, eff_rr_3D2, 'ko-', zorder = 4, label='RR:3D CE(2)')
plt.semilogx(distances_3D2, eff_neu_3D2, 'mo-', zorder = 3, label='Neu:3D CE(2)')'''

plt.plot(dist_1, logBsn_1, 'b-', zorder = 8, label='A+ Catalog')
print('1')
plt.plot(dist_2, logBsn_2, 'g-', zorder = 7, label='A+ Non-Catalog*')
print('2')
'''plt.plot(dist_3, logBsn_3, 'm-', zorder = 6, label='A+/Kagra Catalog')
print('3')
plt.plot(dist_4, logBsn_4, 'r-', zorder = 5, label='A+/Kagra Non-Catalog')
print('4')
plt.plot(snr_5, logBsn_5, 'ko-', zorder = 4, label='Scheidegger2010_R4E1FC_L*')
print('5')
plt.plot(snr_6, logBsn_6, 'yo-', zorder = 3, label='Scheidegger2010_R5E1AC')
print('6')
plt.plot(snr_mean, mean, 'co-', zorder = 2, label='Mean')
print('7')'''

#plt.loglog(line_x, line_y, 'g-', zorder = 1)

#plt.plot(line[0], line[1], color='g', linestyle='-', linewidth=2)#, label='Full Data\nSlope = ' + rounding(full_slope, precision) + '\np = ' + rounding(full_p_value, precision), alpha=0.5, zorder=10)


plt.xlim([1, 150])
plt.ylim([0, 1.0])
plt.xlabel('Injection Distance [kpc]', fontsize=18)
plt.ylabel('Classification Efficiency', fontsize=18)#'Efficiency')
plt.grid(b=True, which='major',color='0.75',linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor',color='0.85',linestyle='--')
#plt.ticklabel_format(axis = 'y', style = 'sci', scilimits = (-2,2))
#plt.ticklabel_format(axis = 'x', style = 'sci', scilimits = (-2,2))
legend = plt.legend(prop={'size':6})
legend.get_frame().set_alpha(0.5)
plt.legend(loc = 'best')
for label in legend.get_texts():
    label.set_fontsize('large')
# save and close figure
plt.savefig(plot_name, bbox_inches='tight')
#plt.clf()
plt.close()








