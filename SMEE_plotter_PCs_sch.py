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
plot_name = 'PCs_sch_paper_2.png'#'FFT_vs_Spec_sch.png'
title = '$\log\,B_{S,N}$ vs Number of PCs'#'log Bsn vs Distance for sch_10, Sch PCs'

'''distances_aLigo = [.2, 1, 2, 4, 5, 7, 10, 15, 25, 50, 75, 100, 150, 200]
distances_Aplus = [.2, 1, 2, 5, 10, 15, 25, 50, 100, 200, 300, 400, 450]
distances_voyager = [.2, 5, 10, 25, 35, 50, 75, 100, 150, 400, 500, 600]
distances_CE = [10, 25, 75, 100, 200, 400, 500, 750, 1000, 1500]'''

dist_spec = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
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

logBsn_1 = [1589.3333333333333, 1658.6666666666667, 1760.6666666666667, 1786.3333333333333, 1807.0, 1896.0, 2056.3333333333335, 2092.6666666666665, 2092.0, 2122.6666666666665]
logBsn_2 = [2159.6666666666665, 2215.3333333333335, 2378.3333333333335, 2376.0, 2374.6666666666665, 2375.3333333333335, 2391.3333333333335, 2388.0, 2393.0, 2432.0]
logBsn_3 = [2098.6666666666665, 2146.6666666666665, 2312.6666666666665, 2320.0, 2323.0, 2330.0, 2345.0, 2344.3333333333335, 2342.6666666666665, 2362.0]
logBsn_4 = [2093.0, 2158.0, 2333.6666666666665, 2352.3333333333335, 2350.6666666666665, 2353.3333333333335, 2367.6666666666665, 2387.6666666666665, 2387.3333333333335, 2407.0]
logBsn_5 = [1442.3333333333333, 1672.0, 1729.3333333333333, 1727.0, 1728.3333333333333, 1728.6666666666667, 1728.3333333333333, 1736.0, 1740.0, 1750.0]
logBsn_6 = [2217.6666666666665, 2214.6666666666665, 2255.3333333333335, 2480.0, 2480.0, 2478.6666666666665, 2499.0, 2496.0, 2503.6666666666665, 2522.0]
mean = [1933.4444444444443, 2010.8888888888887, 2128.3333333333335, 2173.611111111111, 2177.277777777778, 2193.6666666666665, 2231.277777777778, 2240.777777777778, 2243.111111111111, 2265.9444444444443]
        
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

plt.plot(dist_spec, logBsn_1, 'bo-', zorder = 8, label='R2E1AC')
print('1')
plt.plot(dist_spec, logBsn_2, 'go-', zorder = 7, label='R3E1AC*')
print('2')
plt.plot(dist_spec, logBsn_3, 'yo-', zorder = 6, label='R3E1DB')
print('3')
plt.plot(dist_spec, logBsn_4, 'co-', zorder = 5, label='R3STAC')
print('4')
plt.plot(dist_spec, logBsn_5, 'mo-', zorder = 4, label='R4E1FC_L*')
print('5')
plt.plot(dist_spec, logBsn_6, 'ro-', zorder = 3, label='R4STAC')
print('6')
plt.plot(dist_spec, mean, 'ko-', zorder = 9, label='Mean')
print('7')

#plt.loglog(line_x, line_y, 'g-', zorder = 1)

#plt.plot(line[0], line[1], color='g', linestyle='-', linewidth=2)#, label='Full Data\nSlope = ' + rounding(full_slope, precision) + '\np = ' + rounding(full_p_value, precision), alpha=0.5, zorder=10)


plt.xlim([1, 10])
plt.ylim([1200, 2600])
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








