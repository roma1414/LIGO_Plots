# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

N = 8
rot1 = (2.48e-23, 8.12670263834e-22, 8.46e-22, 9.46751764257e-23, 5.99459678533e-24, 3.72563807902e-27, 6.18302750515e-22, 8.7123141531e-24)
rot1Std = (5.43e-24, 2.7963222414e-22, 1.82e-22, 1.69996506512e-23, 1.38557222539e-24, 9.7083776029e-28, 1.06585737241e-22, 3.33126036556e-24)

rot2 = (1.32e-23, 2.13592867651e-23, 1.78e-23, 8.65822850527e-23, 1.70202097431e-24, 2.18864645655e-27, 5.62536124252e-22, 9.80228570421e-25)
rot2Std = (2.89e-24, 5.14278050622e-24, 3.56e-24, 1.53980691061e-23, 5.85518181354e-25, 5.88453346638e-28, 2.45484211035e-22, 4.1881344713e-25)

rot3 = (1.27e-23, 8.56943709617e-24, 1.52e-23, 3.90145976536e-24, 1.20259736445e-25, 8.11710496305e-28, 1.03951286278e-23, 2.41897573927e-27)
rot3Std = (1.59e-24, 3.02918530483e-24, 2.68e-24, 1.54391008266e-24, 2.24389149699e-26, 2.41937175768e-28, 2.50214921605e-24, 5.46916995739e-28)

rot4 = (4.24e-24, 6.46205586334e-24, 7.04e-25, 2.63537608953e-24, 2.89271034541e-26, 0, 3.08229903031e-26, 2.37939356605e-28)
rot4Std = (9.78e-25, 2.53463760596e-24, 1.51e-25, 6.93559112146e-25, 6.92524663535e-27, 0, 4.86219590623e-27, 6.60495756017e-29)

rot5 = (1.16e-25, 1.63723463743e-24, 3.43e-25, 4.25722473475e-26, 1.5368006266e-27, 0, 3.42287217651e-27, 1.73935659009e-28)
rot5Std = (2.24e-26, 6.23047590638e-25, 6.23e-26, 1.67631798026e-26, 7.07477797314e-28, 0, 1.49695435884e-27, 6.7671832184e-29)

rot6 = (1.9e-28, 4.04063184688e-25, 2.39e-25, 2.34208296966e-28, 7.11013836229e-29, 0, 1.71609182815e-28, 0)
rot6Std = (4.1e-29, 1.82230913658e-25, 4.24e-26, 8.88875057904e-29, 1.276425212e-29, 0, 4.72014918475e-29, 0)

ind = np.arange(N)  # the x locations for the groups
width = 0.35 / 5       # the width of the bars

fig, ax = plt.subplots(figsize=(9,6))
rects1 = ax.bar(ind, rot1, width, color='r', yerr=rot1Std)
rects2 = ax.bar(ind + width, rot2, width, color='r', yerr=rot2Std)
rects3 = ax.bar(ind + 2 * width, rot3, width, color='r', yerr=rot3Std)
rects4 = ax.bar(ind + 3 * width, rot4, width, color='r', yerr=rot4Std)
rects5 = ax.bar(ind + 4 * width, rot5, width, color='r', yerr=rot5Std)
rects6 = ax.bar(ind + 5 * width, rot6, width, color='r', yerr=rot6Std)

lin1 = (2.67e-24, 2.85915440929e-21, 1.75e-21, 2.47469515786e-21, 6.12409906029e-21, 6.76680920388e-28, 2.98435588056e-24, 7.3386054184e-23)
lin1Std = (5.92e-25, 1.12586007146e-21, 3.75e-22, 9.97355193903e-22, 2.14748022785e-21, 2.49731852084e-28, 9.62151697261e-25, 3.34171673249e-23)

lin2 = (1.59e-24, 2.83927379507e-21, 1.34e-21, 1.00809659057e-22, 6.33362985949e-23, 1.42155425769e-28, 1.20535158617e-27, 5.77917062403e-28)
lin2Std = (3.91e-25, 1.28137446244e-21, 3.17e-22, 4.10872147429e-23, 2.81031831559e-23, 3.47405100957e-29, 5.69294202593e-28, 2.76466325914e-28)

lin3 = (1.16e-24, 3.2081969959e-23, 4.79e-22, 5.93304124346e-23, 2.62758198846e-25, 7.64616344106e-29, 1.16276886475e-28, 1.09685379029e-28)
lin3Std = (2.26e-25, 4.87989077013e-24, 1.22e-22, 2.4496484439e-23, 3.43087867069e-26, 3.09773033733e-29, 3.6857152663e-29, 2.64055582396e-29)

lin4 = (1.14e-24, 2.99882985226e-24, 4.27e-22, 2.72396409578e-23, 1.85107781438e-27, 0, 2.41923212367e-30, 8.04650585916e-29)
lin4Std = (2.29e-25, 8.93503384676e-25, 1.12e-22, 1.13198137913e-23, 4.59137190902e-28, 0, 1.08583261503e-30, 1.51326172367e-29)

lin5 = (1.08e-26, 9.89596472944e-25, 3.69e-22, 1.46405405249e-26, 6.39805256648e-28, 0, 0, 0)
lin5Std = (2.35e-27, 3.70047763325e-25, 6.87e-23, 6.72414056022e-27, 1.72859694812e-28, 0, 0, 0)

lin6 = (8.68e-27, 1.82026702072e-25, 3.59e-22, 7.27493347039e-27, 5.04859012248e-28, 0, 0, 0)
lin6Std = (1.31e-27, 8.32260259145e-26, 6.22e-23, 2.3922240551e-27, 2.37264280057e-28, 0, 0, 0)

rects7 = ax.bar(ind + 6 * width, lin1, width, color='y', yerr=lin1Std)
rects8 = ax.bar(ind + 7 * width, lin2, width, color='y', yerr=lin2Std)
rects9 = ax.bar(ind + 8 * width, lin3, width, color='y', yerr=lin3Std)
rects10 = ax.bar(ind + 9 * width, lin4, width, color='y', yerr=lin4Std)
rects11 = ax.bar(ind + 10 * width, lin5, width, color='y', yerr=lin5Std)
rects12 = ax.bar(ind + 11 * width, lin6, width, color='y', yerr=lin6Std)

# add some text for labels, title and axes ticks
ax.set_ylabel('Max Slope')
ax.set_title('Slopes by location')
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