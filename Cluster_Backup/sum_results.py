from __future__ import division
#x = 15

dim_dir = '/home/vincent.roma/public_html/SMEE/recoloring_results/sasi/sch_aLigo/'
mur_dir = '/home/vincent.roma/public_html/SMEE/recoloring_results/sasi/neu_aLigo/'
output_dir = '/home/vincent.roma/public_html/SMEE/recoloring_stats/'
out_file_name = 'sasi_aLigo_2kpc.txt'

distances = ['2']
num_times = 5
num_s = 6
num_p = 3

confident_threshold = 5
output_string = ''
dim_dict = {}
mur_dict = {}
job_names = []
dim_bad_keys = []
mur_bad_keys = []
dim_Bsn_list = []
mur_Bsn_list = []

sch_waveforms = ['Scheidegger2010_R2E1AC.txt']#, 'Scheidegger2010_R3E1DB.txt']#, 'Scheidegger2010_R3STAC.txt', 'Scheidegger2010_R4STAC.txt']#['Scheidegger2010_R2E1AC.txt', 'Scheidegger2010_R2E3AC.txt', 'Scheidegger2010_R2STAC.txt', 'Scheidegger2010_R3E1AC.txt', 'Scheidegger2010_R3E1AC_L.txt', 'Scheidegger2010_R3E1CA.txt', 'Scheidegger2010_R3E1DB.txt', 'Scheidegger2010_R3E2AC.txt', 'Scheidegger2010_R3E3AC.txt', 'Scheidegger2010_R3STAC.txt', 'Scheidegger2010_R4E1AC.txt', 'Scheidegger2010_R4E1EC.txt', 'Scheidegger2010_R4E1FC_L.txt', 'Scheidegger2010_R4STAC.txt', 'Scheidegger2010_R5E1AC.txt']

dim_waveforms = ['Dimmelmeier2008Rapid_s11a1o09ls.txt', 'Dimmelmeier2008Rapid_s11a1o09shen.txt', 'Dimmelmeier2008Rapid_s11a1o13ls.txt', 'Dimmelmeier2008Rapid_s11a1o13shen.txt', 'Dimmelmeier2008Rapid_s11a2o05shen.txt', 'Dimmelmeier2008Rapid_s11a2o07ls.txt', 'Dimmelmeier2008Rapid_s11a2o07shen.txt', 'Dimmelmeier2008Rapid_s11a2o09ls.txt', 'Dimmelmeier2008Rapid_s11a2o09shen.txt', 'Dimmelmeier2008Rapid_s11a2o13ls.txt', 'Dimmelmeier2008Rapid_s11a2o13shen.txt', 'Dimmelmeier2008Rapid_s11a2o15ls.txt', 'Dimmelmeier2008Rapid_s11a2o15shen.txt', 'Dimmelmeier2008Rapid_s11a3o05ls.txt', 'Dimmelmeier2008Rapid_s11a3o05shen.txt', 'Dimmelmeier2008Rapid_s11a3o07ls.txt', 'Dimmelmeier2008Rapid_s11a3o07shen.txt', 'Dimmelmeier2008Rapid_s11a3o09ls.txt', 'Dimmelmeier2008Rapid_s11a3o09shen.txt', 'Dimmelmeier2008Rapid_s11a3o12ls.txt', 'Dimmelmeier2008Rapid_s11a3o12shen.txt', 'Dimmelmeier2008Rapid_s11a3o13ls.txt', 'Dimmelmeier2008Rapid_s11a3o13shen.txt', 'Dimmelmeier2008Rapid_s11a3o15ls.txt', 'Dimmelmeier2008Rapid_s11a3o15shen.txt', 'Dimmelmeier2008Rapid_s15a1o07ls.txt', 'Dimmelmeier2008Rapid_s15a1o07shen.txt', 'Dimmelmeier2008Rapid_s15a1o09ls.txt', 'Dimmelmeier2008Rapid_s15a1o09shen.txt', 'Dimmelmeier2008Rapid_s15a1o13ls.txt', 'Dimmelmeier2008Rapid_s15a1o13shen.txt', 'Dimmelmeier2008Rapid_s15a2o05ls.txt', 'Dimmelmeier2008Rapid_s15a2o05shen.txt', 'Dimmelmeier2008Rapid_s15a2o07ls.txt', 'Dimmelmeier2008Rapid_s15a2o07shen.txt', 'Dimmelmeier2008Rapid_s15a2o09ls.txt', 'Dimmelmeier2008Rapid_s15a2o09shen.txt', 'Dimmelmeier2008Rapid_s15a2o13ls.txt', 'Dimmelmeier2008Rapid_s15a2o13shen.txt', 'Dimmelmeier2008Rapid_s15a2o15ls.txt', 'Dimmelmeier2008Rapid_s15a2o15shen.txt', 'Dimmelmeier2008Rapid_s15a3o05ls.txt', 'Dimmelmeier2008Rapid_s15a3o05shen.txt', 'Dimmelmeier2008Rapid_s15a3o07ls.txt', 'Dimmelmeier2008Rapid_s15a3o07shen.txt', 'Dimmelmeier2008Rapid_s15a3o09ls.txt', 'Dimmelmeier2008Rapid_s15a3o09shen.txt', 'Dimmelmeier2008Rapid_s15a3o12ls.txt', 'Dimmelmeier2008Rapid_s15a3o12shen.txt', 'Dimmelmeier2008Rapid_s15a3o13ls.txt', 'Dimmelmeier2008Rapid_s15a3o13shen.txt', 'Dimmelmeier2008Rapid_s15a3o15ls.txt', 'Dimmelmeier2008Rapid_s15a3o15shen.txt', 'Dimmelmeier2008Rapid_s20a1o07shen.txt', 'Dimmelmeier2008Rapid_s20a1o09ls.txt', 'Dimmelmeier2008Rapid_s20a1o09shen.txt', 'Dimmelmeier2008Rapid_s20a1o13ls.txt', 'Dimmelmeier2008Rapid_s20a1o13shen.txt', 'Dimmelmeier2008Rapid_s20a2o05ls.txt', 'Dimmelmeier2008Rapid_s20a2o05shen.txt', 'Dimmelmeier2008Rapid_s20a2o07ls.txt', 'Dimmelmeier2008Rapid_s20a2o07shen.txt', 'Dimmelmeier2008Rapid_s20a2o09ls.txt', 'Dimmelmeier2008Rapid_s20a2o09shen.txt', 'Dimmelmeier2008Rapid_s20a2o13ls.txt', 'Dimmelmeier2008Rapid_s20a2o13shen.txt', 'Dimmelmeier2008Rapid_s20a2o15ls.txt', 'Dimmelmeier2008Rapid_s20a2o15shen.txt', 'Dimmelmeier2008Rapid_s20a3o05ls.txt', 'Dimmelmeier2008Rapid_s20a3o05shen.txt', 'Dimmelmeier2008Rapid_s20a3o07ls.txt', 'Dimmelmeier2008Rapid_s20a3o07shen.txt', 'Dimmelmeier2008Rapid_s20a3o09ls.txt', 'Dimmelmeier2008Rapid_s20a3o09shen.txt', 'Dimmelmeier2008Rapid_s20a3o12ls.txt', 'Dimmelmeier2008Rapid_s20a3o12shen.txt', 'Dimmelmeier2008Rapid_s20a3o13ls.txt', 'Dimmelmeier2008Rapid_s20a3o13shen.txt', 'Dimmelmeier2008Rapid_s20a3o15ls.txt', 'Dimmelmeier2008Rapid_s20a3o15shen.txt', 'Dimmelmeier2008Rapid_s40a1o05shen.txt', 'Dimmelmeier2008Rapid_s40a1o07ls.txt', 'Dimmelmeier2008Rapid_s40a1o07shen.txt', 'Dimmelmeier2008Rapid_s40a1o09ls.txt', 'Dimmelmeier2008Rapid_s40a1o09shen.txt', 'Dimmelmeier2008Rapid_s40a1o13ls.txt', 'Dimmelmeier2008Rapid_s40a1o13shen.txt', 'Dimmelmeier2008Rapid_s40a2o05ls.txt', 'Dimmelmeier2008Rapid_s40a2o05shen.txt', 'Dimmelmeier2008Rapid_s40a2o07ls.txt', 'Dimmelmeier2008Rapid_s40a2o07shen.txt', 'Dimmelmeier2008Rapid_s40a2o09ls.txt', 'Dimmelmeier2008Rapid_s40a2o09shen.txt', 'Dimmelmeier2008Rapid_s40a2o13ls.txt', 'Dimmelmeier2008Rapid_s40a2o13shen.txt', 'Dimmelmeier2008Rapid_s40a2o15ls.txt', 'Dimmelmeier2008Rapid_s40a2o15shen.txt', 'Dimmelmeier2008Rapid_s40a3o05ls.txt', 'Dimmelmeier2008Rapid_s40a3o05shen.txt', 'Dimmelmeier2008Rapid_s40a3o07ls.txt', 'Dimmelmeier2008Rapid_s40a3o07shen.txt', 'Dimmelmeier2008Rapid_s40a3o09ls.txt', 'Dimmelmeier2008Rapid_s40a3o09shen.txt', 'Dimmelmeier2008Rapid_s40a3o12ls.txt', 'Dimmelmeier2008Rapid_s40a3o12shen.txt', 'Dimmelmeier2008Rapid_s40a3o13ls.txt', 'Dimmelmeier2008Rapid_s40a3o13shen.txt', 'Dimmelmeier2008Rapid_s40a3o15ls.txt', 'Dimmelmeier2008Rapid_s40a3o15shen.txt', 'Dimmelmeier2008Slow_s11a1o01ls.txt', 'Dimmelmeier2008Slow_s11a1o01shen.txt', 'Dimmelmeier2008Slow_s11a1o05ls.txt', 'Dimmelmeier2008Slow_s11a1o05shen.txt', 'Dimmelmeier2008Slow_s11a1o07ls.txt', 'Dimmelmeier2008Slow_s11a1o07shen.txt', 'Dimmelmeier2008Slow_s11a2o05ls.txt', 'Dimmelmeier2008Slow_s15a1o01ls.txt', 'Dimmelmeier2008Slow_s15a1o01shen.txt', 'Dimmelmeier2008Slow_s15a1o05ls.txt', 'Dimmelmeier2008Slow_s15a1o05shen.txt', 'Dimmelmeier2008Slow_s20a1o01ls.txt', 'Dimmelmeier2008Slow_s20a1o01shen.txt', 'Dimmelmeier2008Slow_s20a1o05ls.txt', 'Dimmelmeier2008Slow_s20a1o05shen.txt', 'Dimmelmeier2008Slow_s20a1o07ls.txt', 'Dimmelmeier2008Slow_s40a1o01ls.txt', 'Dimmelmeier2008Slow_s40a1o01shen.txt', 'Dimmelmeier2008Slow_s40a1o05ls.txt']

neu_waveforms = ['Andresen2016_s11.txt']#, 'Mueller2012_L15-3.txt']#, 'Kuroda2016_tm1.txt', 'Yakunin2017_C15.txt']#['Andresen2016_s11.txt', 'Andresen2016_s20.txt', 'Andresen2016_s20s.txt', 'Andresen2016_s27.txt', 'Kuroda2016_sfhx.txt', 'Kuroda2016_tm1.txt','Mueller2012_L15-3.txt', 'Mueller2012_N20-2.txt', 'Mueller2012_W15-4.txt']

mur_waveforms = ['Murphy2009_12_1.8.txt', 'Murphy2009_12_2.2.txt', 'Murphy2009_12_2.8.txt', 'Murphy2009_12_3.2.txt', 'Murphy2009_15_3.2.txt', 'Murphy2009_15_3.4.txt', 'Murphy2009_15_3.7.txt', 'Murphy2009_15_4.0.txt', 'Murphy2009_20_3.2.txt', 'Murphy2009_20_3.4.txt', 'Murphy2009_20_3.6.txt', 'Murphy2009_20_3.8.txt', 'Murphy2009_40_6.0.txt', 'Murphy2009_40_10.0.txt', 'Murphy2009_40_12.0.txt', 'Murphy2009_40_13.0.txt']

catalogs = [sch_waveforms, neu_waveforms]

def stdDev(data):
    n = float(len(data))
    if n <= 1:
        return 0
    mean = sum(data) / n
    diffs = [dataPoint - mean for dataPoint in data]
    diffsSquared = [dataPoint**2 for dataPoint in diffs]
    sumOfSquares = sum(diffsSquared)
    sigma2 = sumOfSquares / n
    sigma = sigma2**(.5)
    return sigma

for time_num in range(num_times):
    #print('time_num = ' + str(time_num))
    for dist in distances:
        for s_num in range(num_s):
            for p_num in range(num_p):
                for catalog in catalogs:
                    cat = ''
                    the_dir = ''
                    if 'Dim' in catalog[0] or 'Sch' in catalog[0]:
                        cat = 'dim'
                    elif 'Mur' in catalog[0] or 'And' in catalog[0] or 'Mue' in catalog[0] or 'Kur' in catalog[0] or 'Yak' in catalog[0]:
                        cat = 'mur'
                    #print('cat = ' + str(cat))
                    for waveform in catalog:
                        dist_mod = dist.replace('.', 'pt')
                        '''if cat == 'dim':
                        num = str(x)
                        else:
                        num = str(catalog.index(waveform) + 1)'''
                        #print('waveform = ' + str(waveform))
                        num = str(catalog.index(waveform) + 1)
                        #print('num defined, num =' + str(num))
                        job_name = cat + '_inj' + num + '_t' + str(time_num + 1) + '_s' + str(s_num+1) + '_p' + str(p_num+1) +'_' + dist_mod + 'kpc'
                        job_names.append(job_name)
                        try:
                            #print(dim_dir + job_name + '_B.txt')
                            the_file = open(dim_dir + job_name + '_B.txt', 'r')
                            the_string = the_file.read()
                            #print('the_string =')
                            #print(the_string)
                            the_list = the_string.split(' ')
                            Bsn = float(the_list[0])
                            dim_dict[job_name] = Bsn
                            if 'Dim' in waveform or 'Sch' in waveform:
                                dim_Bsn_list.append(Bsn)
                        except IOError:
                            dim_bad_keys.append(job_name)
                        try:
                            the_file = open(mur_dir + job_name + '_B.txt', 'r')
                            #print(mur_dir + job_name + '_B.txt')
                            the_string = the_file.read()
                            #print('the_string =')
                            #print(the_string)
                            the_list = the_string.split(' ')
                            #print('the_list =')
                            #print(the_list)

                            if the_list[0] != '':
                                Bsn = float(the_list[0])
                                mur_dict[job_name] = Bsn
                                if 'Mur' in waveform or 'And' in waveform or 'Mue' in waveform or 'Kur' in waveform or 'Yak' in waveform:
                                    mur_Bsn_list.append(Bsn)
                        except IOError:
                            mur_bad_keys.append(job_name)
#print('###############################################')
#print('first loop complete')
#print('dim_dict = \n')
#print(dim_dict)
output_string += 'Confidence Threshold: ' + str(confident_threshold) + '\n\n'
                    
output_string += 'dim_dict length: ' + str(len(dim_dict)) + '\n'
output_string += 'mur_dict length: ' + str(len(mur_dict)) + '\n\n'
output_string += 'dim_Bsn_list length: ' + str(len(dim_Bsn_list)) + '\n'

#print('dim_bad_keys =')
#print(dim_bad_keys)

avg = sum(dim_Bsn_list) / len(dim_Bsn_list)
sigma = stdDev(dim_Bsn_list)
Min = min(dim_Bsn_list)
Max = max(dim_Bsn_list)
output_string += 'Average: ' + str(avg) + ' +- ' + str(sigma) + '  min: ' + str(Min) + '  max: ' + str(Max) + '\n\n'
output_string += 'mur_Bsn_list length: ' + str(len(mur_Bsn_list)) + '\n'
avg = sum(mur_Bsn_list) / len(mur_Bsn_list)
sigma = stdDev(mur_Bsn_list)
Min = min(mur_Bsn_list)
Max = max(mur_Bsn_list)
output_string += 'Average: ' + str(avg) + ' +- ' + str(sigma) + '  min: ' + str(Min) + '  max: ' + str(Max) + '\n\n'
output_string += 'dim_bad_keys length: ' + str(len(dim_bad_keys)) + '\n'
output_string += 'mur_bad_keys length: ' + str(len(mur_bad_keys)) + '\n\n'

dim_Bdm_list = []
mur_Bmd_list = []
for key in job_names:
    if key in dim_dict and key in mur_dict:
        dim_result = dim_dict[key]
        mur_result = mur_dict[key]
        if 'dim' in key:
            Bdm = dim_result - mur_result
            dim_Bdm_list.append(Bdm)
            #output_string += 'key = ' + str(key) + '  dim_result = ' + str(dim_result) + '  mur_result = ' + str(mur_result) + '  result = ' + str(Bdm) + '\n'
        elif 'mur' in key:
            Bmd = mur_result - dim_result
            mur_Bmd_list.append(Bmd)
            #output_string += 'key = ' + str(key) + '  dim_result = ' + str(dim_result) + '  mur_result = ' + str(mur_result) + '  result = ' + str(Bmd) + '\n'

output_string += 'dim_Bdm_list length: ' + str(len(dim_Bdm_list)) + '\n'
avg = sum(dim_Bdm_list) / len(dim_Bdm_list)
sigma = stdDev(dim_Bdm_list)
Min = min(dim_Bdm_list)
Max = max(dim_Bdm_list)
output_string += 'Average: ' + str(avg) + ' +- ' + str(sigma) + '  min: ' + str(Min) + '  max: ' + str(Max) + '\n\n'

dim_Bdm_confident = [entry for entry in dim_Bdm_list if entry >= confident_threshold]
dim_Bdm_efficiency = float(len(dim_Bdm_confident)) / float(len(dim_Bdm_list))
dim_Bdm_incorrect = [entry for entry in dim_Bdm_list if entry <= -1*confident_threshold]
dim_Bdm_incor_eff = float(len(dim_Bdm_incorrect)) / float(len(dim_Bdm_list))
output_string += 'Efficiency: ' + str(dim_Bdm_efficiency) + '\nFalse Classifications: ' + str(len(dim_Bdm_incorrect)) + '    Rate: ' + str(dim_Bdm_incor_eff) + '\n\n'

output_string += 'mur_Bmd_list length: ' + str(len(mur_Bmd_list)) + '\n'
avg = sum(mur_Bmd_list) / len(mur_Bmd_list)
sigma = stdDev(mur_Bmd_list)
Min = min(mur_Bmd_list)
Max = max(mur_Bmd_list)
output_string += 'Average: ' + str(avg) + ' +- ' + str(sigma) + '  min: ' + str(Min) + '  max: ' + str(Max) + '\n\n'

mur_Bmd_confident = [entry for entry in mur_Bmd_list if entry >= confident_threshold]
mur_Bmd_efficiency = float(len(mur_Bmd_confident)) / float(len(mur_Bmd_list))
mur_Bmd_incorrect = [entry for entry in mur_Bmd_list if entry <= -1*confident_threshold]
mur_Bmd_incor_eff = float(len(mur_Bmd_incorrect)) / float(len(mur_Bmd_list))

output_string += 'Efficiency: '+ str(mur_Bmd_efficiency) + '\nFalse Classifications: ' + str(len(mur_Bmd_incorrect)) + '     Rate: ' + str(mur_Bmd_incor_eff) + '\n\n'

output_string += 'dim_Bsn_list = [ ' + str(dim_Bsn_list[0])
for B in dim_Bsn_list[1:]:
    output_string += ', ' + str(B)
output_string += ']\n\n'

output_string += 'mur_Bsn_list = [ ' + str(mur_Bsn_list[0])
for B in mur_Bsn_list[1:]:
    output_string += ', ' + str(B)
output_string += ']\n\n'

output_string += 'dim_Bdm_list = [ ' + str(dim_Bdm_list[0])
for B in dim_Bdm_list[1:]:
    output_string += ', ' + str(B)
    #output_string += ', ' + str(B)
output_string += ']\n\n'

output_string += 'mur_Bmd_list = [ ' + str(mur_Bmd_list[0])
for B in mur_Bmd_list[1:]:
    output_string += ', ' + str(B)
    #output_string += ', ' + str(B)
output_string += ']\n\n'

output_string += 'dim_bad_keys = ['
for key in dim_bad_keys:
    output_string += ', ' + str(key)
output_string += ']\n\n'

output_string += 'mur_bad_keys = ['
for key in mur_bad_keys:
    output_string += ', ' + str(key)
output_string += ']\n\n'

a = []
output_string += 'Detailed View:\n\n'
for job_name in job_names:
    try:
        dim_logBsn = dim_dict[job_name]
        mur_logBsn = mur_dict[job_name]
        logB = 0
        if 'mur' in job_name:
            logB = mur_logBsn - dim_logBsn
        elif 'dim' in job_name:
            logB = dim_logBsn - mur_logBsn
        output_string += 'name: ' + job_name + ' dim_logBsn = ' + str(dim_logBsn) + ' mur_logBsn = ' + str(mur_logBsn) + ' logB = ' + str(logB) + ', '    
    except KeyError:
        a = []

out_file = open(output_dir + out_file_name, 'w')
out_file.write(output_string)
out_file.close()




