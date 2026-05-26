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
    
BS_s_str = '''H1:ISI-BS_ST1_BLND_X_L4C_CUR_IN1_DQ 1.27804666715e-24 3.6555472266e-25 0.00215162056614
H1:ISI-BS_ST1_BLND_RY_L4C_CUR_IN1_DQ 1.04814939961e-24 3.79232676653e-25 0.0127880458693
H1:ISI-BS_ST1_BLND_RX_L4C_CUR_IN1_DQ 9.98403277769e-26 3.75841774554e-26 0.0166164889875
H1:HPI-BS_BLND_L4C_RZ_IN1_DQ 2.72141033157e-26 9.11643560551e-27 0.00793719136342
H1:HPI-BS_BLND_L4C_X_IN1_DQ 4.61609792757e-27 1.23789574731e-27 0.00153619847756
H1:HPI-BS_BLND_L4C_RY_IN1_DQ 3.70019820767e-27 1.68784344348e-27 0.0425671881921
H1:HPI-BS_BLND_L4C_Y_IN1_DQ 5.31865428266e-28 1.83255379105e-28 0.0103908864607
H1:HPI-BS_BLND_L4C_Z_IN1_DQ 4.19918472505e-28 1.65822611754e-28 0.0189753148578
H1:HPI-BS_BLND_L4C_RX_IN1_DQ 1.05334933917e-28 4.84238013514e-29 0.0417770609098'''
BS_p_str = '''H1:HPI-BS_BLND_L4C_X_IN1_DQ 4.61609792757e-27 1.23789574731e-27 0.00153619847756
H1:ISI-BS_ST1_BLND_X_L4C_CUR_IN1_DQ 1.27804666715e-24 3.6555472266e-25 0.00215162056614
H1:HPI-BS_BLND_L4C_RZ_IN1_DQ 2.72141033157e-26 9.11643560551e-27 0.00793719136342
H1:HPI-BS_BLND_L4C_Y_IN1_DQ 5.31865428266e-28 1.83255379105e-28 0.0103908864607
H1:ISI-BS_ST1_BLND_RY_L4C_CUR_IN1_DQ 1.04814939961e-24 3.79232676653e-25 0.0127880458693
H1:ISI-BS_ST1_BLND_RX_L4C_CUR_IN1_DQ 9.98403277769e-26 3.75841774554e-26 0.0166164889875
H1:HPI-BS_BLND_L4C_Z_IN1_DQ 4.19918472505e-28 1.65822611754e-28 0.0189753148578
H1:HPI-BS_BLND_L4C_RX_IN1_DQ 1.05334933917e-28 4.84238013514e-29 0.0417770609098
H1:HPI-BS_BLND_L4C_RY_IN1_DQ 3.70019820767e-27 1.68784344348e-27 0.0425671881921'''
ITMX_s_str = '''H1:ISI-ITMX_ST2_BLND_Z_GS13_CUR_IN1_DQ 2.69261010815e-21 8.02312765244e-22 0.00571569476442
H1:ISI-ITMX_ST1_BLND_Y_L4C_CUR_IN1_DQ 2.40072220805e-24 5.87900581437e-25 0.000578661330278
H1:ISI-ITMX_ST1_BLND_RZ_L4C_CUR_IN1_DQ 1.75669227599e-24 4.86028532603e-25 0.0031441981552
H1:ISI-ITMX_ST1_BLND_RX_L4C_CUR_IN1_DQ 1.42735999961e-24 4.129420434e-25 0.0026433220493
H1:ISI-ITMX_ST1_BLND_X_L4C_CUR_IN1_DQ 6.66419269936e-25 2.34671205717e-25 0.00981185037692
H1:ISI-ITMX_ST1_BLND_RY_L4C_CUR_IN1_DQ 3.11595132863e-25 1.1785686545e-25 0.0155734925913
H1:ISI-ITMX_ST1_BLND_Z_L4C_CUR_IN1_DQ 1.87308774892e-25 5.50134070228e-26 0.0042720424237
H1:HPI-ITMX_BLND_L4C_RZ_IN1_DQ 1.43071453191e-26 4.04114595659e-27 0.00183709552805
H1:HPI-ITMX_BLND_L4C_Y_IN1_DQ 2.45397403504e-27 4.66578674077e-28 6.39018099746e-05
H1:HPI-ITMX_BLND_L4C_RX_IN1_DQ 1.11375443782e-27 4.61568821076e-28 0.0241931711277
H1:HPI-ITMX_BLND_L4C_X_IN1_DQ 7.04723577804e-28 2.28051338216e-28 0.00631321654553
H1:HPI-ITMX_BLND_L4C_Z_IN1_DQ 4.65664518573e-28 1.29864115856e-28 0.00156354987681
H1:HPI-ITMX_BLND_L4C_RY_IN1_DQ 3.29319172072e-28 1.04879727448e-28 0.00475829061719'''
ITMX_p_str = '''H1:HPI-ITMX_BLND_L4C_Y_IN1_DQ 2.45397403504e-27 4.66578674077e-28 6.39018099746e-05
H1:ISI-ITMX_ST1_BLND_Y_L4C_CUR_IN1_DQ 2.40072220805e-24 5.87900581437e-25 0.000578661330278
H1:HPI-ITMX_BLND_L4C_Z_IN1_DQ 4.65664518573e-28 1.29864115856e-28 0.00156354987681
H1:HPI-ITMX_BLND_L4C_RZ_IN1_DQ 1.43071453191e-26 4.04114595659e-27 0.00183709552805
H1:ISI-ITMX_ST1_BLND_RX_L4C_CUR_IN1_DQ 1.42735999961e-24 4.129420434e-25 0.0026433220493
H1:ISI-ITMX_ST1_BLND_RZ_L4C_CUR_IN1_DQ 1.75669227599e-24 4.86028532603e-25 0.0031441981552
H1:ISI-ITMX_ST1_BLND_Z_L4C_CUR_IN1_DQ 1.87308774892e-25 5.50134070228e-26 0.0042720424237
H1:HPI-ITMX_BLND_L4C_RY_IN1_DQ 3.29319172072e-28 1.04879727448e-28 0.00475829061719
H1:ISI-ITMX_ST2_BLND_Z_GS13_CUR_IN1_DQ 2.69261010815e-21 8.02312765244e-22 0.00571569476442
H1:HPI-ITMX_BLND_L4C_X_IN1_DQ 7.04723577804e-28 2.28051338216e-28 0.00631321654553
H1:ISI-ITMX_ST1_BLND_X_L4C_CUR_IN1_DQ 6.66419269936e-25 2.34671205717e-25 0.00981185037692
H1:ISI-ITMX_ST1_BLND_RY_L4C_CUR_IN1_DQ 3.11595132863e-25 1.1785686545e-25 0.0155734925913
H1:HPI-ITMX_BLND_L4C_RX_IN1_DQ 1.11375443782e-27 4.61568821076e-28 0.0241931711277'''
ITMY_s_str = '''H1:ISI-ITMY_ST2_BLND_Z_GS13_CUR_IN1_DQ 1.38493480607e-21 2.37490023716e-22 8.66927097094e-06
H1:ISI-ITMY_ST1_BLND_RY_L4C_CUR_IN1_DQ 1.08028224134e-24 2.17848882831e-25 4.14580441599e-05
H1:ISI-ITMY_ST1_BLND_X_L4C_CUR_IN1_DQ 6.32221583614e-25 1.27012629945e-25 4.93038946123e-05
H1:ISI-ITMY_ST1_BLND_RZ_L4C_CUR_IN1_DQ 5.92489208709e-25 9.50736664473e-26 1.61282953122e-06
H1:ISI-ITMY_ST1_BLND_Y_L4C_CUR_IN1_DQ 2.00846134321e-25 3.63970268731e-26 1.12634264425e-05
H1:ISI-ITMY_ST1_BLND_RX_L4C_CUR_IN1_DQ 1.2456634611e-25 2.93302886398e-26 0.000229579118819
H1:ISI-ITMY_ST1_BLND_Z_L4C_CUR_IN1_DQ 6.24739801117e-26 1.23267233154e-26 3.49766310255e-05
H1:HPI-ITMY_BLND_L4C_X_IN1_DQ 1.98149164869e-27 8.2824042532e-28 0.025711972702
H1:HPI-ITMY_BLND_L4C_Y_IN1_DQ 8.51682258057e-28 2.57316722356e-28 0.00368262334484
H1:HPI-ITMY_BLND_L4C_Z_IN1_DQ 2.34037526617e-28 8.97984497254e-29 0.0147185283764'''
ITMY_p_str = '''H1:ISI-ITMY_ST1_BLND_RZ_L4C_CUR_IN1_DQ 5.92489208709e-25 9.50736664473e-26 1.61282953122e-06
H1:ISI-ITMY_ST2_BLND_Z_GS13_CUR_IN1_DQ 1.38493480607e-21 2.37490023716e-22 8.66927097094e-06
H1:ISI-ITMY_ST1_BLND_Y_L4C_CUR_IN1_DQ 2.00846134321e-25 3.63970268731e-26 1.12634264425e-05
H1:ISI-ITMY_ST1_BLND_Z_L4C_CUR_IN1_DQ 6.24739801117e-26 1.23267233154e-26 3.49766310255e-05
H1:ISI-ITMY_ST1_BLND_RY_L4C_CUR_IN1_DQ 1.08028224134e-24 2.17848882831e-25 4.14580441599e-05
H1:ISI-ITMY_ST1_BLND_X_L4C_CUR_IN1_DQ 6.32221583614e-25 1.27012629945e-25 4.93038946123e-05
H1:ISI-ITMY_ST1_BLND_RX_L4C_CUR_IN1_DQ 1.2456634611e-25 2.93302886398e-26 0.000229579118819
H1:HPI-ITMY_BLND_L4C_Y_IN1_DQ 8.51682258057e-28 2.57316722356e-28 0.00368262334484
H1:HPI-ITMY_BLND_L4C_Z_IN1_DQ 2.34037526617e-28 8.97984497254e-29 0.0147185283764
H1:HPI-ITMY_BLND_L4C_X_IN1_DQ 1.98149164869e-27 8.2824042532e-28 0.025711972702'''
ETMX_s_str = '''G'''
ETMX_p_str = '''G'''
ETMY_s_str = '''H1:ISI-ETMY_ST1_BLND_X_L4C_CUR_IN1_DQ 1.05384405062e-25 3.9151730394e-26 0.0167351903358'''
ETMY_p_str = '''H1:ISI-ETMY_ST1_BLND_X_L4C_CUR_IN1_DQ 1.05384405062e-25 3.9151730394e-26 0.0167351903358'''
HAM1_s_str = '''H1:HPI-HAM1_BLND_L4C_RZ_IN1_DQ 5.49272156222e-28 1.77248575277e-28 0.0052388082447
H1:HPI-HAM1_BLND_L4C_RY_IN1_DQ 2.91073760588e-28 7.14850560349e-29 0.000715735525302
H1:HPI-HAM1_BLND_L4C_RX_IN1_DQ 7.04266754151e-29 1.24645704481e-29 9.44035714443e-06
H1:HPI-HAM1_BLND_L4C_Z_IN1_DQ 6.47616835003e-29 2.14041385659e-29 0.00695474484352
H1:HPI-HAM1_BLND_L4C_X_IN1_DQ 2.47160279401e-29 1.05721387891e-29 0.0318785875533
H1:HPI-HAM1_BLND_L4C_Y_IN1_DQ 2.44833032209e-30 9.29260094768e-31 0.015489862334'''
HAM1_p_str = '''H1:HPI-HAM1_BLND_L4C_RX_IN1_DQ 7.04266754151e-29 1.24645704481e-29 9.44035714443e-06
H1:HPI-HAM1_BLND_L4C_RY_IN1_DQ 2.91073760588e-28 7.14850560349e-29 0.000715735525302
H1:HPI-HAM1_BLND_L4C_RZ_IN1_DQ 5.49272156222e-28 1.77248575277e-28 0.0052388082447
H1:HPI-HAM1_BLND_L4C_Z_IN1_DQ 6.47616835003e-29 2.14041385659e-29 0.00695474484352
H1:HPI-HAM1_BLND_L4C_Y_IN1_DQ 2.44833032209e-30 9.29260094768e-31 0.015489862334
H1:HPI-HAM1_BLND_L4C_X_IN1_DQ 2.47160279401e-29 1.05721387891e-29 0.0318785875533'''
HAM2_s_str = '''H1:ISI-HAM2_BLND_GS13Y_IN1_DQ 1.17934477572e-23 1.85933565058e-24 7.35470110549e-06
H1:ISI-HAM2_BLND_GS13RX_IN1_DQ 9.97651912728e-24 1.64784854112e-24 2.51693300586e-06
H1:ISI-HAM2_BLND_GS13Z_IN1_DQ 3.83039640365e-24 1.36900796116e-24 0.00975688452549
H1:ISI-HAM2_BLND_GS13RY_IN1_DQ 1.93167146728e-24 7.99200359008e-25 0.0253246735148
H1:ISI-HAM2_BLND_GS13X_IN1_DQ 1.44704241826e-24 4.68587205342e-25 0.00519191061783
H1:HPI-HAM2_BLND_L4C_RY_IN1_DQ 5.03380767857e-28 1.40472252379e-28 0.00198148847125
H1:HPI-HAM2_BLND_L4C_RZ_IN1_DQ 1.33928535656e-28 5.84436117216e-29 0.0306263040463
H1:HPI-HAM2_BLND_L4C_Z_IN1_DQ 8.20489461368e-29 2.06526722632e-29 0.000749715036601
H1:HPI-HAM2_BLND_L4C_RX_IN1_DQ 4.1592121816e-29 1.06125657883e-29 0.00122344476947
H1:HPI-HAM2_BLND_L4C_X_IN1_DQ 1.26581065712e-29 3.75911839116e-30 0.0036575354069
H1:HPI-HAM2_BLND_L4C_Y_IN1_DQ 4.00330062409e-30 1.09886202503e-30 0.00219025903527'''
HAM2_p_str = '''H1:ISI-HAM2_BLND_GS13RX_IN1_DQ 9.97651912728e-24 1.64784854112e-24 2.51693300586e-06
H1:ISI-HAM2_BLND_GS13Y_IN1_DQ 1.17934477572e-23 1.85933565058e-24 7.35470110549e-06
H1:HPI-HAM2_BLND_L4C_Z_IN1_DQ 8.20489461368e-29 2.06526722632e-29 0.000749715036601
H1:HPI-HAM2_BLND_L4C_RX_IN1_DQ 4.1592121816e-29 1.06125657883e-29 0.00122344476947
H1:HPI-HAM2_BLND_L4C_RY_IN1_DQ 5.03380767857e-28 1.40472252379e-28 0.00198148847125
H1:HPI-HAM2_BLND_L4C_Y_IN1_DQ 4.00330062409e-30 1.09886202503e-30 0.00219025903527
H1:HPI-HAM2_BLND_L4C_X_IN1_DQ 1.26581065712e-29 3.75911839116e-30 0.0036575354069
H1:ISI-HAM2_BLND_GS13X_IN1_DQ 1.44704241826e-24 4.68587205342e-25 0.00519191061783
H1:ISI-HAM2_BLND_GS13Z_IN1_DQ 3.83039640365e-24 1.36900796116e-24 0.00975688452549
H1:ISI-HAM2_BLND_GS13RY_IN1_DQ 1.93167146728e-24 7.99200359008e-25 0.0253246735148
H1:HPI-HAM2_BLND_L4C_RZ_IN1_DQ 1.33928535656e-28 5.84436117216e-29 0.0306263040463'''
HAM6_s_str = '''H1:ISI-HAM6_BLND_GS13RX_IN1_DQ 5.36184517222e-24 2.01184416516e-24 0.0141404007204
H1:ISI-HAM6_BLND_GS13Y_IN1_DQ 3.18865950483e-24 8.51684662558e-25 0.00161603635879
H1:ISI-HAM6_BLND_GS13RY_IN1_DQ 8.69687106378e-25 3.42476533283e-25 0.0200032531586
H1:HPI-HAM6_BLND_L4C_Y_IN1_DQ 2.40149488106e-28 6.39283346649e-29 0.00116107664724
H1:HPI-HAM6_BLND_L4C_RY_IN1_DQ 9.7807068398e-29 4.13985391712e-29 0.0303330144077
H1:HPI-HAM6_BLND_L4C_X_IN1_DQ 9.62844457544e-29 1.69595591242e-29 1.23459788655e-05
H1:HPI-HAM6_BLND_L4C_Z_IN1_DQ 2.89286151435e-29 9.80446427626e-30 0.00790718637363'''
HAM6_p_str = '''H1:HPI-HAM6_BLND_L4C_X_IN1_DQ 9.62844457544e-29 1.69595591242e-29 1.23459788655e-05
H1:HPI-HAM6_BLND_L4C_Y_IN1_DQ 2.40149488106e-28 6.39283346649e-29 0.00116107664724
H1:ISI-HAM6_BLND_GS13Y_IN1_DQ 3.18865950483e-24 8.51684662558e-25 0.00161603635879
H1:HPI-HAM6_BLND_L4C_Z_IN1_DQ 2.89286151435e-29 9.80446427626e-30 0.00790718637363
H1:ISI-HAM6_BLND_GS13RX_IN1_DQ 5.36184517222e-24 2.01184416516e-24 0.0141404007204
H1:ISI-HAM6_BLND_GS13RY_IN1_DQ 8.69687106378e-25 3.42476533283e-25 0.0200032531586
H1:HPI-HAM6_BLND_L4C_RY_IN1_DQ 9.7807068398e-29 4.13985391712e-29 0.0303330144077'''