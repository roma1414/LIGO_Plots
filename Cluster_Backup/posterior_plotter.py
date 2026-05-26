from __future__ import division
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

post_file_path = '/home/vincent.roma/public_html/SMEE/results_injections/sch/inj_1_posts.txt'
out_dir = '/home/vincent.roma/public_html/SMEE/results_injections/sch/inj_1_stats/'
numIFOs = 2
numPCs = 5
numVars = 9 + numPCs + numIFOs#9   #18 + numIFOs
#print('numVars = ' + str(numVars))

stats_string = 'Maximum Likelihood Reconstruction\n\n'
PC_lists = []
for i in range(numVars):
    PC_lists.append([])

post_file = open(post_file_path, 'r')
line_list = post_file.readlines()
post_file.close()

params = line_list[0].split()

for line in line_list[1:]:
    if len(line) > 0:
        entry_list = line.split()
        for i in range(numVars):
            #print('entry = ' + str(entry_list[19-i]))
            #PC_lists[i].append(float(entry_list[19-i]))
            PC_lists[i].append(float(entry_list[i]))

def make_plot(data, num_bins, i):
    stats_add = ''
    x_min = min(data)
    x_max = max(data)
    bins = plt.hist(data, num_bins, (x_min, x_max), edgecolor='black')
    max_bin_index = np.argmax(bins[0])
    '''go = True
    n = 0
    while(go == True):
        if bins[0][n] == max_bin_value:
            max_bin_index = n
            go = False'''
    #bin_width = (x_max - x_min) / num_bins
    #low_cut = x_min + max_bin_index * bin_width
    #beta = low_cut + .5 * bin_width
    beta = data[-1]
    variable = params[i]
    #stats_add += variable + ' posterior estimate = ' + str(beta) + ' +- ' + str(.5*bin_width) + '\n'
    stats_add += variable + ' = ' + str(beta) + '\n'

    plt.xlim([x_min, x_max])
    plt.title('Posterior Histogram for ' + variable)
    plt.ylabel('Occurences')
    plt.xlabel('Value')
    plt.savefig(out_dir + 'plot_' + variable + '.png')
    plt.close()

    return stats_add

for i in range(numVars):
    stats_string += make_plot(PC_lists[i], 40, i)

stats_file = open(out_dir + 'stats.txt', 'w')
stats_file.write(stats_string)
stats_file.close()
