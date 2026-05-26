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
plot_name = 'PCs_review_no_sasi.png'#'FFT_vs_Spec_sch.png'
title = '$\log\,B_{S,N}$ vs Number of PCs'#'log Bsn vs Distance for sch_10, Sch PCs'

'''distances_aLigo = [.2, 1, 2, 4, 5, 7, 10, 15, 25, 50, 75, 100, 150, 200]
distances_Aplus = [.2, 1, 2, 5, 10, 15, 25, 50, 100, 200, 300, 400, 450]
distances_voyager = [.2, 5, 10, 25, 35, 50, 75, 100, 150, 400, 500, 600]
distances_CE = [10, 25, 75, 100, 200, 400, 500, 750, 1000, 1500]'''

dist_spec = [1, 2, 3, 4, 5, 6, 7, 8]#, 9, 10]
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

logBsn_1 = [1035, 1102, 1099, 1160, 1158, 1160, 1855, 1953]
logBsn_2 = [958, 1494, 1502, 1499, 1567, 1567, 1564, 1561]
logBsn_3 = [988, 1023, 1020, 1205, 1208, 1261, 1260, 1266]
logBsn_4 = [1166, 1242, 1314, 1323, 1322, 1320, 1319, 1315]
logBsn_5 = [138, 159, 177, 623, 1912, 1943, 2002, 2139, 2137, 2140]
logBsn_6 = [88, 232, 241, 274, 926, 938, 936, 981, 979, 1099]
mean = [1036.75, 1215.25, 1233.75, 1296.75, 1313.75, 1327.0, 1499.5, 1523.75]

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

plt.plot(dist_spec, logBsn_1, 'mo-', zorder = 8, label='Andresen2016_s11')
print('1')
plt.plot(dist_spec, logBsn_2, 'ro-', zorder = 7, label='Kuroda2016_tm1')
print('2')
plt.plot(dist_spec, logBsn_3, 'go-', zorder = 6, label='Powell2018_he3pt5')
print('3')
plt.plot(dist_spec, logBsn_4, 'co-', zorder = 5, label='Powell2018_s18')
print('4')
#plt.plot(dist_spec, logBsn_5, 'bo-', zorder = 4, label='Couch2018_gw')
print('5')
#plt.plot(dist_spec, logBsn_6, 'yo-', zorder = 3, label='Couch2018_pert_LR_gw')
print('6')
plt.plot(dist_spec, mean, 'ko-', zorder = 9, label='Mean')
print('7')

#plt.loglog(line_x, line_y, 'g-', zorder = 1)

#plt.plot(line[0], line[1], color='g', linestyle='-', linewidth=2)#, label='Full Data\nSlope = ' + rounding(full_slope, precision) + '\np = ' + rounding(full_p_value, precision), alpha=0.5, zorder=10)


plt.xlim([1, 8])
plt.ylim([900, 2000])
plt.xlabel('Number of PCs Used', fontsize=18)
plt.ylabel('$\log\,B_{S,N}$', fontsize=18)#'Efficiency')
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








