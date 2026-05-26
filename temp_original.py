# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

N = 8
menMeans = (2.57 * 10**-23, 5.75 * 10**-22, 1.86 * 10**-23, 9.43 * 10**-23, 1.25 * 10**-25, 4.07 * 10**-27, 6.28 * 10**-22, 2.31 * 10**-27)
menStd = (5.41 * 10**-24, 1.32 * 10**-22, 3.56 * 10**-24, 1.7 * 10**-23, 2.24 * 10**-26, 1.05 * 10**-27, 1.07 * 10**-22, 5.58 * 10**-28)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots(figsize=(9,6))
rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

womenMeans = (2.59 * 10**-24, 2.87 * 10**-23, 1.81 * 10**-21, 3.98 * 10**-24, 2.52 * 10**-25, 6.83 * 10**-28, 1.09 * 10**-28, 5.84 * 10**-27)
womenStd = (5.92 * 10**-25, 4.78 * 10**-24, 3.29 * 10**-22, 8.03 * 10**-25, 3.43 * 10**-26, 2.53 * 10**-28, 3.62 * 10**-29, 1.73 * 10**-27)
rects2 = ax.bar(ind + width, womenMeans, width, color='y', yerr=womenStd)

# add some text for labels, title and axes ticks
ax.set_ylabel('Max Slope')
ax.set_title('Slopes by location')
ax.set_xticks(ind + width)
ax.set_xticklabels(('BS', 'ITMX', 'ITMY', 'ETMX', 'ETMY', 'HAM1', 'HAM2', 'HAM6'))

legend = ax.legend((rects1[0], rects2[0]), ('Rotational', 'Linear'))
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