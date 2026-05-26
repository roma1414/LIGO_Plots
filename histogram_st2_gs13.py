# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

N = 5
rot1 = (1.31572955453e-23, 8.56943709617e-24, 2.17567233511e-23, 2.1192807075e-28, 0)
rot1Std = (2.89300613609e-24, 3.02918530483e-24, 7.57068036808e-24, 1.01565011602e-28, 0)

rot2 = (6.14912613542e-24, 6.46205586334e-24, 1.71201211357e-23, 3.90145976536e-24, 0)
rot2Std = (2.08383537951e-24, 2.53463760596e-24, 5.81529465311e-24, 1.54391008266e-24, 0)

rot3 = (3.30418079353e-23, 8.12670263834e-22, 3.59106814112e-21, 9.46751764257e-23, 1.5368006266e-27)
rot3Std = (9.86532306865e-24, 2.7963222414e-22, 1.40185785431e-21, 1.69996506512e-23, 7.07477797314e-28)

'''rot4 = ()
rot4Std = ()

rot5 = ()
rot5Std = ()

rot6 = ()
rot6Std = ()'''

ind = np.arange(N)  # the x locations for the groups
width = 0.35 / 2.5       # the width of the bars

fig, ax = plt.subplots(figsize=(9,6))
rects1 = ax.bar(ind, rot1, width, color='r', yerr=rot1Std)
rects2 = ax.bar(ind + width, rot2, width, color='r', yerr=rot2Std)
rects3 = ax.bar(ind + 2 * width, rot3, width, color='r', yerr=rot3Std)
'''rects4 = ax.bar(ind + 3 * width, rot4, width, color='r', yerr=rot4Std)
rects5 = ax.bar(ind + 4 * width, rot5, width, color='r', yerr=rot5Std)
rects6 = ax.bar(ind + 5 * width, rot6, width, color='r', yerr=rot6Std)'''

lin1 = (5.81016405785e-24, 3.2081969959e-23, 4.26870194056e-22, 5.93304124346e-23, 6.12409906029e-21)
lin1Std = (2.4157431676e-24, 4.87989077013e-24, 1.12245066927e-22, 2.4496484439e-23, 2.14748022785e-21)

lin2 = (1.15759194604e-24, 2.85915440929e-21, 2.23398780536e-21, 2.47469515786e-21, 6.33362985949e-23)
lin2Std = (2.26000470921e-25, 1.12586007146e-21, 1.02865165695e-21, 9.97355193903e-22, 2.81031831559e-23)

lin3 = (1.59718622792e-24, 2.83927379507e-21, 1.74852425334e-21, 2.72396409578e-23, 5.04859012248e-28)
lin3Std = (5.50078417678e-25, 1.28137446244e-21, 3.75301614281e-22, 1.13198137913e-23, 2.37264280057e-28)

'''lin4 = ()
lin4Std = ()

lin5 = ()
lin5Std = ()

lin6 = ()
lin6Std = ()'''

rects7 = ax.bar(ind + 3 * width, lin1, width, color='y', yerr=lin1Std)
rects8 = ax.bar(ind + 4 * width, lin2, width, color='y', yerr=lin2Std)
rects9 = ax.bar(ind + 5 * width, lin3, width, color='y', yerr=lin3Std)
'''rects10 = ax.bar(ind + 9 * width, lin4, width, color='y', yerr=lin4Std)
rects11 = ax.bar(ind + 10 * width, lin5, width, color='y', yerr=lin5Std)
rects12 = ax.bar(ind + 11 * width, lin6, width, color='y', yerr=lin6Std)'''

# add some text for labels, title and axes ticks
ax.set_ylabel('Max Slope')
ax.set_xlabel('Each location ordered by: RX, RY, RZ, X, Y, Z')
ax.set_title('Slopes by location (ST2 GS13s')
ax.set_xticks(ind + width)
ax.set_xticklabels(('BS', 'ITMX', 'ITMY', 'ETMX', 'ETMY', 'HAM1', 'HAM2', 'HAM6'))

legend = ax.legend((rects1[0], rects7[0]), ('Rotational', 'Linear'))
legend.get_frame().set_alpha(0.5)

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

#autolabel(rects1)
#autolabel(rects2)

plt.yscale('log')

plt.savefig('hist.png')
plt.close()