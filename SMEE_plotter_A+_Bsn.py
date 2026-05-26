# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 14:37:47 2017

@author: Vincent
"""

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plot_name = 'A+_Bsn.png'
title = 'log B vs Distance'

distances = [5, 10, 25, 30, 35, 40, 50, 100, 150, 200, 250, 300, 350]
dim_data = [33734, 8410, 1316, 902, 652, 493, 305, 61, 19, 5.8, 0.4, -1.9, -3.1]
mur_data = [869, 183, 9.2, 2.2, -1.9, -4.4, -6.4, -7.6, -7.6, -7.8, -7.6, -7.7, -8]

line_x = [.000001, 99999]
line_y = [10, 10]

plt.figure(figsize=(9,6))
plt.title(title, fontsize=18, y = 1.05)

plt.loglog(distances, dim_data, 'ro', zorder = 2, label='Dimmelmeier Injections')
plt.loglog(distances, mur_data, 'bo', zorder = 2, label='Murphy Injections')
plt.loglog(line_x, line_y, 'g-', zorder = 1)

#plt.plot(line[0], line[1], color='g', linestyle='-', linewidth=2)#, label='Full Data\nSlope = ' + rounding(full_slope, precision) + '\np = ' + rounding(full_p_value, precision), alpha=0.5, zorder=10)


plt.xlim([2, 400])
plt.ylim([0, 100000])
plt.xlabel('Distance [kpc]')
plt.ylabel('Avg. log B')
plt.grid(b=True, which='major',color='0.75',linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor',color='0.85',linestyle='--')
#plt.ticklabel_format(axis = 'y', style = 'sci', scilimits = (-2,2))
#plt.ticklabel_format(axis = 'x', style = 'sci', scilimits = (-2,2))
legend = plt.legend(prop={'size':6})
legend.get_frame().set_alpha(0.5)
for label in legend.get_texts():
    label.set_fontsize('large')
# save and close figure
plt.savefig(plot_name, bbox_inches='tight')
#plt.clf()
plt.close()








