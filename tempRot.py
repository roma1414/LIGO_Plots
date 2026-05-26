# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

N = 2
rot1 = (1, 2)
rot1Std = (.5, .5)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots(figsize=(9,6))
rects1 = ax.bar(ind, rot1, width, color='r', yerr=rot1Std)

lin1 = (3, 2)
lin1Std = (.5, .5)
rects2 = ax.bar(ind + width, lin1, width, color='y', yerr=lin1Std)

# add some text for labels, title and axes ticks
ax.set_ylabel('Max Slope')
ax.set_title('Slopes by location')
ax.set_xticks(ind2 + width)
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