# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

N = 8
rot1 = (2.1374843572e-28, 1.39022425208e-28, 3.97461945027e-28, 2.34208296966e-28, 0, 2.18864645655e-27, 3.42287217651e-27, 2.37939356605e-28)
rot1Std = (6.97556826824e-29, 5.08254417314e-29, 1.14545110958e-28, 8.88875057904e-29, 0, 5.88453346638e-28, 1.49695435884e-27, 6.60495756017e-29)

rot2 = (1.08249310608e-28, 2.20635800478e-28, 1.60571505682e-28, 8.95289854378e-29, 7.11013836229e-29, 8.11710496305e-28, 1.71609182815e-28, 1.73935659009e-28)
rot2Std = (3.35467914241e-29, 9.42027465576e-29, 6.04356686081e-29, 3.71220379284e-29, 1.276425212e-29, 2.41937175768e-28, 4.72014918475e-29, 6.7671832184e-29)

rot3 = (3.97775831075e-26, 2.58103573215e-26, 2.33588693011e-28, 1.48614362339e-29, 2.89271034541e-26, 3.72563807902e-27, 3.08229903031e-26, 2.41897573927e-27)
rot3Std = (1.38635566704e-26, 7.11196552929e-27, 3.42667464941e-29, 6.22752702756e-30, 6.92524663535e-27, 9.7083776029e-28, 4.86219590623e-27, 5.46916995739e-28)

'''rot4 = ()
rot4Std = ()

rot5 = ()
rot5Std = ()

rot6 = ()
rot6Std = ()'''

ind = np.arange(N)  # the x locations for the groups
width = 0.35 / 2.5      # the width of the bars

fig, ax = plt.subplots(figsize=(9,6))
rects1 = ax.bar(ind, rot1, width, color='r', yerr=rot1Std)
rects2 = ax.bar(ind + width, rot2, width, color='r', yerr=rot2Std)
rects3 = ax.bar(ind + 2 * width, rot3, width, color='r', yerr=rot3Std)
'''rects4 = ax.bar(ind + 3 * width, rot4, width, color='r', yerr=rot4Std)
rects5 = ax.bar(ind + 4 * width, rot5, width, color='r', yerr=rot5Std)
rects6 = ax.bar(ind + 5 * width, rot6, width, color='r', yerr=rot6Std)'''

lin1 = (5.81244577918e-27, 9.14585742236e-28, 6.12635210327e-27, 1.02000249965e-31, 6.39805256648e-28, 6.76680920388e-28, 1.20535158617e-27, 1.09685379029e-28)
lin1Std = (1.87937175552e-27, 3.69245418486e-28, 2.58030575018e-27, 4.43727974598e-32, 1.72859694812e-28, 2.49731852084e-28, 5.69294202593e-28, 2.64055582396e-29)

lin2 = (6.21328753945e-28, 2.84871251336e-27, 9.90151577096e-28, 7.27493347039e-27, 8.35923275743e-32, 1.42155425769e-28, 2.41923212367e-30, 5.77917062403e-28)
lin2Std = (2.80330889744e-28, 7.2337596556e-28, 3.74899891691e-28, 2.3922240551e-27, 3.98467911207e-32, 3.47405100957e-29, 1.08583261503e-30, 2.76466325914e-28)

lin3 = (5.55184576962e-31, 5.13499543378e-28, 8.55289156505e-31, 1.90623619349e-30, 1.85107781438e-27, 7.64616344106e-29, 1.16276886475e-28, 8.04650585916e-29)
lin3Std = (1.42154987943e-31, 2.35734384389e-28, 2.38142897528e-31, 7.32776855931e-31, 4.59137190902e-28, 3.09773033733e-29, 3.6857152663e-29, 1.51326172367e-29)

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
ax.set_title('Slopes by location (HPI L4Cs)')
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