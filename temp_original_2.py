# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

N = 5
rot1 = (3.30418079353e-23, 8.12670263834e-22, 3.59106814112e-21, 9.46751764257e-23, 3.72563807902e-27)
rot1Std = (9.86532306865e-24, 2.7963222414e-22, 1.40185785431e-21, 1.69996506512e-23, 9.7083776029e-28)

rot2 = (1.31572955453e-23, 2.13592867651e-23, 2.17567233511e-23, 8.65822850527e-23, 2.18864645655e-27)
rot2Std = (2.89300613609e-24, 5.14278050622e-24, 7.57068036808e-24, 1.53980691061e-23, 5.88453346638e-28)

rot3 = (6.14912613542e-24, 8.56943709617e-24, 1.71201211357e-23, 3.90145976536e-24, 8.11710496305e-28)
rot3Std = (2.08383537951e-24, 3.02918530483e-24, 5.81529465311e-24, 1.54391008266e-24, 2.41937175768e-28)

rot4 = (2.7720709358e-24, 6.46205586334e-24, 1.11213705349e-24, 2.63537608953e-24, 0)
rot4Std = (1.11665187747e-24, 2.53463760596e-24, 3.31692497729e-25, 6.93559112146e-25, 0)

rot5 = (1.45145875473e-24, 1.63723463743e-24, 7.0394394662e-25, 4.25722473475e-26, 0)
rot5Std = (6.25157371098e-25, 6.23047590638e-25, 1.51047073e-25, 1.67631798026e-26, 0)

rot6 = (1.46680679749e-25, 4.04063184688e-25, 1.44632157695e-25, 2.34208296966e-28, 0)
rot6Std = (5.74581908696e-26, 1.82230913658e-25, 4.64144654012e-26, 8.88875057904e-29, 0)

ind = np.arange(N)  # the x locations for the groups
width = 0.35 / 5       # the width of the bars

fig, ax = plt.subplots(figsize=(9,6))
rects1 = ax.bar(ind, rot1, width, color='r', yerr=rot1Std)
rects2 = ax.bar(ind + width, rot2, width, color='r', yerr=rot2Std)
rects3 = ax.bar(ind + 2 * width, rot3, width, color='r', yerr=rot3Std)
rects4 = ax.bar(ind + 3 * width, rot4, width, color='r', yerr=rot4Std)
rects5 = ax.bar(ind + 4 * width, rot5, width, color='r', yerr=rot5Std)
rects6 = ax.bar(ind + 5 * width, rot6, width, color='r', yerr=rot6Std)

lin1 = (5.81016405785e-24, 2.85915440929e-21, 2.23398780536e-21, 2.47469515786e-21, 6.76680920388e-28)
lin1Std = (2.4157431676e-24, 1.12586007146e-21, 1.02865165695e-21, 9.97355193903e-22, 2.49731852084e-28)

lin2 = (1.71645838503e-24, 2.83927379507e-21, 1.74852425334e-21, 1.00809659057e-22, 1.42155425769e-28)
lin2Std = (6.2269228995e-25, 1.28137446244e-21, 3.75301614281e-22, 4.10872147429e-23, 3.47405100957e-29)

lin3 = (1.59718622792e-24, 3.2081969959e-23, 4.26870194056e-22, 5.93304124346e-23, 7.64616344106e-29)
lin3Std = (5.50078417678e-25, 4.87989077013e-24, 1.12245066927e-22, 2.4496484439e-23, 3.09773033733e-29)

lin4 = (1.15759194604e-24, 2.99882985226e-24, 7.45736018126e-25, 2.72396409578e-23, 0)
lin4Std = (2.26000470921e-25, 8.93503384676e-25, 1.88502150961e-25, 1.13198137913e-23, 0)

lin5 = (1.08244498252e-26, 9.89596472944e-25, 1.92630301244e-25, 1.46405405249e-26, 0)
lin5Std = (2.35187668017e-27, 3.70047763325e-25, 6.41744965598e-26, 6.72414056022e-27, 0)

lin6 = (5.81244577918e-27, 1.82026702072e-25, 1.05964073973e-25, 7.27493347039e-27, 0)
lin6Std = (1.87937175552e-27, 8.32260259145e-26, 1.72341402113e-26, 2.3922240551e-27, 0)

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