# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

N = 1
rot1 = (1.31572955453e-23)
rot1Std = ()

rot2 = ()
rot2Std = ()

rot3 = ()
rot3Std = ()

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

lin1 = ()
lin1Std = ()

lin2 = ()
lin2Std = ()

lin3 = ()
lin3Std = ()

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