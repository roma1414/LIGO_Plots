# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

N = 7
rot1 = (1.46680679749e-25, 1.63723463743e-24, 1.44632157695e-25, 2.63537608953e-24, 1.70202097431e-24, 1.03951286278e-23, 8.7123141531e-24)
rot1Std = (5.74581908696e-26, 6.23047590638e-25, 4.64144654012e-26, 6.93559112146e-25, 5.85518181354e-25, 2.50214921605e-24, 3.33126036556e-24)

rot2 = (1.45145875473e-24, 4.04063184688e-25, 1.11213705349e-24, 4.25722473475e-26, 1.20259736445e-25, 5.62536124252e-22, 0)
rot2Std = (6.25157371098e-25, 1.82230913658e-25, 3.31692497729e-25, 1.67631798026e-26, 2.24389149699e-26, 2.45484211035e-22, 0)

rot3 = (2.7720709358e-24, 2.13592867651e-23, 7.0394394662e-25, 8.65822850527e-23, 5.99459678533e-24, 6.18302750515e-22, 9.80228570421e-25)
rot3Std = (1.11665187747e-24, 5.14278050622e-24, 1.51047073e-25, 1.53980691061e-23, 1.38557222539e-24, 1.06585737241e-22, 4.1881344713e-25)

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

lin1 = (1.71645838503e-24, 9.89596472944e-25, 7.45736018126e-25, 1.95802543461e-27, 2.62758198846e-25, 2.98435588056e-24, 7.3386054184e-23)
lin1Std = (6.2269228995e-25, 3.70047763325e-25, 1.88502150961e-25, 8.90568744689e-28, 3.43087867069e-26, 9.62151697261e-25, 3.34171673249e-23)

lin2 = (2.19384965752e-27, 2.99882985226e-24, 1.92630301244e-25, 1.00809659057e-22, 5.60868572379e-30, 0, 0)
lin2Std = (7.81502011762e-28, 8.93503384676e-25, 6.41744965598e-26, 4.10872147429e-23, 1.09301574563e-30, 0, 0)

lin3 = (1.08244498252e-26, 1.82026702072e-25, 1.05964073973e-25, 1.46405405249e-26, 1.85e-27, 0, 0)
lin3Std = (2.35187668017e-27, 8.32260259145e-26, 1.72341402113e-26, 6.72414056022e-27, 4.59e-28, 0, 0)

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
ax.set_title('Slopes by location (ST1 GS13s)')
ax.set_xticks(ind + width)
ax.set_xticklabels(('BS', 'ITMX', 'ITMY', 'ETMX', 'ETMY', 'HAM2', 'HAM6'))

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