# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 17:57:41 2016

@author: Vincent
"""

import numpy as np
import matplotlib.pyplot as plt

def make_plot(locations, mode, stage):
    N = len(locations)
    rot1 = []
    rot1Std = []
    rot2 = []
    rot2Std = []
    rot3 = []
    rot3Std = []
    lin1 = []
    lin1Std = []
    lin2 = []
    lin2Std = []
    lin3 = []
    lin3Std = []
    
    for loc in locations:
        data = []
        if loc == 'BS':
            if mode == 'slope':
                the_string = BS_s_str
            else:
                the_string = BS_p_str
            data = get_data(the_string, stage)
        elif loc == 'ITMX':
            if mode == 'slope':
                the_string = ITMX_s_str
            else:
                the_string = ITMX_p_str
            data = get_data(the_string, stage)
        elif loc == 'ITMY':
            if mode == 'slope':
                the_string = ITMY_s_str
            else:
                the_string = ITMY_p_str
            data = get_data(the_string, stage)
        elif loc == 'ETMX':
            if mode == 'slope':
                the_string = ETMX_s_str
            else:
                the_string = ETMX_p_str
            data = get_data(the_string, stage)
        elif loc == 'ETMY':
            if mode == 'slope':
                the_string = ETMY_s_str
            else:
                the_string = ETMY_p_str
            data = get_data(the_string, stage)
        elif loc == 'HAM1':
            if mode == 'slope':
                the_string = HAM1_s_str
            else:
                the_string = HAM1_p_str
            data = get_data(the_string, stage)
        elif loc == 'HAM2':
            if mode == 'slope':
                the_string = HAM2_s_str
            else:
                the_string = HAM2_p_str
            data = get_data(the_string, stage)
        elif loc == 'HAM6':
            if mode == 'slope':
                the_string = HAM6_s_str
            else:
                the_string = HAM6_p_str
            data = get_data(the_string, stage)
        
        rot1.append(data[0][1])
        rot1Std.append(data[0][2])
        rot2.append(data[1][1])
        rot2Std.append(data[1][2])
        rot3.append(data[2][1])
        rot3Std.append(data[2][2])
        lin1.append(data[3][1])
        lin1Std.append(data[3][2])
        lin2.append(data[4][1])
        lin2Std.append(data[4][2])
        lin3.append(data[5][1])
        lin3Std.append(data[5][2])
    
    rot1 = tuple(rot1)
    rot1Std = tuple(rot1Std)
    
    rot2 = tuple(rot2)
    rot2Std = tuple(rot2Std)
    
    rot3 = tuple(rot3)
    rot3Std = tuple(rot3Std)
    
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35 / 2.5       # the width of the bars
    
    fig, ax = plt.subplots(figsize=(13.5,9))
    rects1 = ax.bar(ind, rot1, width, color='r', yerr=rot1Std)
    rects2 = ax.bar(ind + width, rot2, width, color='r', yerr=rot2Std)
    rects3 = ax.bar(ind + 2 * width, rot3, width, color='r', yerr=rot3Std)
    
    lin1 = tuple(lin1)
    lin1Std = tuple(lin1Std)
    
    lin2 = tuple(lin2)
    lin2Std = tuple(lin2Std)
    
    lin3 = tuple(lin3)
    lin3Std = tuple(lin3Std)
    
    rects7 = ax.bar(ind + 3 * width, lin1, width, color='y', yerr=lin1Std)
    rects8 = ax.bar(ind + 4 * width, lin2, width, color='y', yerr=lin2Std)
    rects9 = ax.bar(ind + 5 * width, lin3, width, color='y', yerr=lin3Std)
    
    # add some text for labels, title and axes ticks
    ax.set_ylabel('Max Slope')
    ax.set_xlabel('Each location ordered by: RX, RY, RZ, X, Y, Z')
    ax.set_title('Slopes by location (' + stage + ')')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(tuple(locations))
    
    def autolabel(rects, label):
        # attach some text labels
        for rect in rects:
            '''the_string = ''
            if i == 1 and label_type == 'angular':
                the_string = 'RX'
            elif i == 1 and label_type == 'linear':
                the_string = 'X'
            elif i == 2 and label_type == 'angular':
                the_string = 'RY'
            elif i == 2 and label_type == 'linear':
                the_string = 'Y'
            elif i == 3 and label_type == 'angular':
                the_string = 'RZ'
            elif i == 3 and label_type == 'linear':
                the_string = 'Z' '''
                
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height, label, ha='center', va='bottom')
            
    autolabel(rects1, 'RX')
    autolabel(rects2, 'RY')
    autolabel(rects3, 'RZ')
    autolabel(rects7, 'X')
    autolabel(rects8, 'Y')
    autolabel(rects9, 'Z')
    
    legend = ax.legend((rects1[0], rects7[0]), ('Rotational', 'Linear'))
    legend.get_frame().set_alpha(0.5)
    
    plt.yscale('log')
    
    plt.savefig('hist_mid_' + stage + '_' + mode + '.png')
    plt.close()
    
def get_data(input_string, stage):
    data = [[], [], [], [], [], []]
    line_list = input_string.split('\n')
    for line in line_list:
        if len(line) > 1:        
            original_entry_list = line.split(' ')
            entry_list = []
            for entry in original_entry_list:
                if entry != '':
                    entry_list.append(entry)
            channel = entry_list[0]
            #print(entry_list)
            if stage in channel or (stage == 'ST1' and '_BLND_GS13' in channel):
                slope = float(entry_list[1])
                error = float(entry_list[2])
                p_value = float(entry_list[3])
                entry = [channel, slope, error, p_value]
                if ('_RX_' in channel or '_GS13RX_' in channel):
                    data[0] = entry
                elif ('_RY_' in channel or '_GS13RY_' in channel):
                    data[1] = entry
                elif ('_RZ_' in channel or '_GS13RZ_' in channel):
                    data[2] = entry
                elif ('_X_' in channel or '_GS13X_' in channel):
                    data[3] = entry
                elif ('_Y_' in channel or '_GS13Y_' in channel):
                    data[4] = entry
                elif ('_Z_' in channel or '_GS13Z_' in channel):
                    data[5] = entry
    for i in range(len(data)):
        if len(data[i]) < 2:
            data[i] = ['none', 0, 0, 1]
    return data
    
BS_s_str = '''H1:ISI-BS_ST2_BLND_RX_GS13_CUR_IN1_DQ 2.78202412524e-21 8.38088660267e-22 0.0127740239683
H1:ISI-BS_ST2_BLND_RY_GS13_CUR_IN1_DQ 2.72810009117e-21 9.51646045134e-22 0.0241048846226'''
BS_p_str = '''H1:ISI-BS_ST2_BLND_RX_GS13_CUR_IN1_DQ 2.78202412524e-21 8.38088660267e-22 0.0127740239683
H1:ISI-BS_ST2_BLND_RY_GS13_CUR_IN1_DQ 2.72810009117e-21 9.51646045134e-22 0.0241048846226'''
ITMX_s_str = '''H1:HPI-ITMX_BLND_L4C_Y_IN1_DQ 1.00396597682e-27 2.83404576289e-28 0.00250233435229
H1:HPI-ITMX_BLND_L4C_RY_IN1_DQ 1.39977199641e-28 6.42178732247e-29 0.0402630817773'''
ITMX_p_str = '''H1:HPI-ITMX_BLND_L4C_Y_IN1_DQ 1.00396597682e-27 2.83404576289e-28 0.00250233435229
H1:HPI-ITMX_BLND_L4C_RY_IN1_DQ 1.39977199641e-28 6.42178732247e-29 0.0402630817773'''
ITMY_s_str = '''G'''
ITMY_p_str = '''G'''
ETMX_s_str = '''H1:ISI-ETMX_ST2_BLND_Y_GS13_CUR_IN1_DQ 1.38326925035e-21 4.51666692746e-22 0.0182568179889
H1:ISI-ETMX_ST1_BLND_RZ_L4C_CUR_IN1_DQ 9.33383509781e-24 7.85869282553e-25 5.42331659365e-08
H1:ISI-ETMX_ST1_BLND_RY_L4C_CUR_IN1_DQ 4.5653300736e-24 4.66907159259e-25 4.31276598545e-06
H1:ISI-ETMX_ST1_BLND_Y_L4C_CUR_IN1_DQ 3.61782077769e-24 1.93745606323e-25 4.19426379511e-09
H1:ISI-ETMX_ST1_BLND_X_L4C_CUR_IN1_DQ 3.34574960447e-24 3.6962643673e-25 1.98183019189e-06
H1:ISI-ETMX_ST1_BLND_RX_L4C_CUR_IN1_DQ 3.18275982453e-24 1.94153351223e-25 1.56326276056e-10
H1:ISI-ETMX_ST1_BLND_Z_L4C_CUR_IN1_DQ 9.057823068e-25 1.17720867641e-25 3.41665480125e-06
H1:HPI-ETMX_BLND_L4C_RZ_IN1_DQ 4.99403438927e-26 5.14894819694e-27 1.35614031841e-09
H1:HPI-ETMX_BLND_L4C_Y_IN1_DQ 8.51435301062e-27 6.37948122408e-28 1.94565055058e-10
H1:HPI-ETMX_BLND_L4C_Z_IN1_DQ 4.37966614835e-27 1.01893877426e-27 0.000432761164777
H1:HPI-ETMX_BLND_L4C_RX_IN1_DQ 1.34939516337e-27 2.54443688724e-28 0.000143046310205'''
ETMX_p_str = '''H1:ISI-ETMX_ST1_BLND_RX_L4C_CUR_IN1_DQ 3.18275982453e-24 1.94153351223e-25 1.56326276056e-10
H1:HPI-ETMX_BLND_L4C_Y_IN1_DQ 8.51435301062e-27 6.37948122408e-28 1.94565055058e-10
H1:HPI-ETMX_BLND_L4C_RZ_IN1_DQ 4.99403438927e-26 5.14894819694e-27 1.35614031841e-09
H1:ISI-ETMX_ST1_BLND_Y_L4C_CUR_IN1_DQ 3.61782077769e-24 1.93745606323e-25 4.19426379511e-09
H1:ISI-ETMX_ST1_BLND_RZ_L4C_CUR_IN1_DQ 9.33383509781e-24 7.85869282553e-25 5.42331659365e-08
H1:ISI-ETMX_ST1_BLND_X_L4C_CUR_IN1_DQ 3.34574960447e-24 3.6962643673e-25 1.98183019189e-06
H1:ISI-ETMX_ST1_BLND_Z_L4C_CUR_IN1_DQ 9.057823068e-25 1.17720867641e-25 3.41665480125e-06
H1:ISI-ETMX_ST1_BLND_RY_L4C_CUR_IN1_DQ 4.5653300736e-24 4.66907159259e-25 4.31276598545e-06
H1:HPI-ETMX_BLND_L4C_RX_IN1_DQ 1.34939516337e-27 2.54443688724e-28 0.000143046310205
H1:HPI-ETMX_BLND_L4C_Z_IN1_DQ 4.37966614835e-27 1.01893877426e-27 0.000432761164777
H1:ISI-ETMX_ST2_BLND_Y_GS13_CUR_IN1_DQ 1.38326925035e-21 4.51666692746e-22 0.0182568179889'''
ETMY_s_str = '''H1:ISI-ETMY_ST2_BLND_X_GS13_CUR_IN1_DQ 1.95095330176e-21 6.46785543675e-22 0.0166508969825
H1:ISI-ETMY_ST1_BLND_RZ_L4C_CUR_IN1_DQ 5.48324115403e-24 1.01112383064e-24 3.75207650616e-05
H1:ISI-ETMY_ST1_BLND_RX_L4C_CUR_IN1_DQ 9.40721835948e-25 4.1700168847e-25 0.0375398693082
H1:ISI-ETMY_ST1_BLND_X_L4C_CUR_IN1_DQ 2.1005322244e-25 2.37175836211e-26 2.40825784927e-07
H1:ISI-ETMY_ST1_BLND_RY_L4C_CUR_IN1_DQ 9.05034624073e-26 1.55201081456e-26 3.30532720605e-05
H1:HPI-ETMY_BLND_L4C_RZ_IN1_DQ 1.23954403993e-26 4.10982582553e-27 0.0145722751994
H1:HPI-ETMY_BLND_L4C_Z_IN1_DQ 1.72676546059e-27 3.25273996183e-28 0.000110422748892
H1:HPI-ETMY_BLND_L4C_X_IN1_DQ 2.45818604366e-28 1.03145286896e-28 0.0384002493856
H1:HPI-ETMY_BLND_L4C_RY_IN1_DQ 4.72235276591e-29 8.79880709845e-30 6.29188833948e-05'''
ETMY_p_str = '''H1:ISI-ETMY_ST1_BLND_X_L4C_CUR_IN1_DQ 2.1005322244e-25 2.37175836211e-26 2.40825784927e-07
H1:ISI-ETMY_ST1_BLND_RY_L4C_CUR_IN1_DQ 9.05034624073e-26 1.55201081456e-26 3.30532720605e-05
H1:ISI-ETMY_ST1_BLND_RZ_L4C_CUR_IN1_DQ 5.48324115403e-24 1.01112383064e-24 3.75207650616e-05
H1:HPI-ETMY_BLND_L4C_RY_IN1_DQ 4.72235276591e-29 8.79880709845e-30 6.29188833948e-05
H1:HPI-ETMY_BLND_L4C_Z_IN1_DQ 1.72676546059e-27 3.25273996183e-28 0.000110422748892
H1:HPI-ETMY_BLND_L4C_RZ_IN1_DQ 1.23954403993e-26 4.10982582553e-27 0.0145722751994
H1:ISI-ETMY_ST2_BLND_X_GS13_CUR_IN1_DQ 1.95095330176e-21 6.46785543675e-22 0.0166508969825
H1:ISI-ETMY_ST1_BLND_RX_L4C_CUR_IN1_DQ 9.40721835948e-25 4.1700168847e-25 0.0375398693082
H1:HPI-ETMY_BLND_L4C_X_IN1_DQ 2.45818604366e-28 1.03145286896e-28 0.0384002493856'''
HAM1_s_str = '''H1:HPI-HAM1_BLND_L4C_RZ_IN1_DQ 2.33048306048e-28 1.10973636313e-28 0.0479852766198'''
HAM1_p_str = '''H1:HPI-HAM1_BLND_L4C_RZ_IN1_DQ 2.33048306048e-28 1.10973636313e-28 0.0479852766198'''
HAM2_s_str = '''H1:HPI-HAM2_BLND_L4C_RY_IN1_DQ 1.93180356128e-28 8.5383552853e-29 0.0355766487699
H1:HPI-HAM2_BLND_L4C_RX_IN1_DQ 1.68889591267e-29 6.42340768197e-30 0.018222589723
H1:HPI-HAM2_BLND_L4C_Y_IN1_DQ 1.48268179318e-30 6.65030000829e-31 0.0404594596883'''
HAM2_p_str = '''H1:HPI-HAM2_BLND_L4C_RX_IN1_DQ 1.68889591267e-29 6.42340768197e-30 0.018222589723
H1:HPI-HAM2_BLND_L4C_RY_IN1_DQ 1.93180356128e-28 8.5383552853e-29 0.0355766487699
H1:HPI-HAM2_BLND_L4C_Y_IN1_DQ 1.48268179318e-30 6.65030000829e-31 0.0404594596883'''
HAM6_s_str = '''H1:ISI-HAM6_BLND_GS13RZ_IN1_DQ 5.14316108664e-24 2.31989476049e-24 0.0397389893214
H1:HPI-HAM6_BLND_L4C_X_IN1_DQ 3.17316021337e-29 1.03934516572e-29 0.00627808236943'''
HAM6_p_str = '''H1:HPI-HAM6_BLND_L4C_X_IN1_DQ 3.17316021337e-29 1.03934516572e-29 0.00627808236943
H1:ISI-HAM6_BLND_GS13RZ_IN1_DQ 5.14316108664e-24 2.31989476049e-24 0.0397389893214'''