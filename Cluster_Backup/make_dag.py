import os
import numpy as np
import random

PI = 3.14159265359

cat = 'neu'
ifos = ['H1', 'L1', 'V1']
mode = 'sasi'

Cat = cat.capitalize()
ncatcols = '8' # 16 for murphy, 128 for Dim, 9 for Neu, 15? for Sch
nPCs = '8'

if cat == 'sch' and (mode == 'cat' or mode == 'nonc'):
    ncatcols = '26'
    nPCs = '5' # 10 or 12
elif cat == 'neu' and (mode == 'cat' or mode == 'nonc'):
    ncatcols = '20'
    nPCs = '5'
elif cat == 'sch' and mode == 'gmode':
    ncatcols = '12'#'5'
    nPCs = '8'
elif cat == 'neu' and mode == 'gmode':
    ncatcols = '10'
    nPCs = '5'
elif cat == 'sch' and mode == 'sasi':
    ncatcols = '12'
    nPCs = '8'
elif cat == 'neu' and mode == 'sasi':
    ncatcols = '6'
    nPCs = '5'

dag_dir = '/home/vincent.roma/public_html/SMEE/dags/' + mode + '/' + cat + '_aLigo_1/'
out_dir = '/home/vincent.roma/public_html/SMEE/recoloring_results/' + mode + '/' + cat + '_aLigo/'
fLow = '30'

distances = ['2', '5', '10', '20', '30', '40', '50']
if (mode == 'cat' or mode == 'nonc'):
    PC_path = '/home/vincent.roma/public_html/SMEE/spec_PCs/' + cat + '_spec.dat' #neu: Neu_complex_PCs.dat
elif cat == 'sch':
    PC_path = '/home/vincent.roma/public_html/SMEE/spec_PCs/' + mode + '/' + 'neu_spec.dat'
elif cat == 'neu':
    PC_path = '/home/vincent.roma/public_html/SMEE/spec_PCs/' + 'no_' + mode + '/' + 'neu_spec.dat'
#nPCs = '9' #6 for Dim, 9 for Mur, 9? for Neu, 6? for Sch

H1_cache = '/home/vincent.roma/public_html/SMEE/caches/LHO_recolored_aLigo_10_7_15_4096.cache'#'LALSimAdLIGO'
L1_cache = '/home/vincent.roma/public_html/SMEE/caches/LLO_recolored_aLigo_10_7_15_4096.cache'
V1_cache = '/home/vincent.roma/public_html/SMEE/caches/LHO_recolored_aVirgo_10_7_15_v2_4096.cache'
E1_cache = '/home/vincent.roma/public_html/SMEE/caches/LHO_recolored_ET_D_10_7_15_4096.cache'
E2_cache = '/home/vincent.roma/public_html/SMEE/caches/LLO_recolored_ET_D_10_7_15_4096.cache'
E3_cache = '/home/vincent.roma/public_html/SMEE/caches/LHO_recolored_ET_D_10_7_15_v2_4096.cache'
I1_cache = '/home/vincent.roma/public_html/SMEE/caches/LHO_recolored_voyager_10_7_15_v5_4096.cache'
J1_cache = '/home/vincent.roma/public_html/SMEE/caches/LHO_recolored_kagra_10_7_15_v3_4096.cache'
K1_cache = '/home/vincent.roma/public_html/SMEE/caches/LHO_recolored_kagra_10_7_15_v3_4096.cache'

condor_out_dir = dag_dir#/local/user/vincent.roma/'
times = ['1128213017', '1128230297', '1128247577', '1128264857', '1128282137']#['1128214077', '1128221657', '1128230297', '1128238937', '1128247577', '1128256217', '1128264857', '1128273497', '1128282137', '1128290777']#9 times:['1128212834', '1128213734', '1128214634', '1128241634', '1128242534', '1128243434', '1128270434', '1128271334', '1128272234']
waveform_dir = '/home/vincent.roma/public_html/SMEE/time_series/'
H1_channel = 'H1:GDS-CALIB_STRAIN'#'H1:SIM-STRAIN'
L1_channel = 'L1:GDS-CALIB_STRAIN'
V1_channel = 'H1:GDS-CALIB_STRAIN'
E1_channel = 'H1:GDS-CALIB_STRAIN'
E2_channel = 'L1:GDS-CALIB_STRAIN'
E3_channel = 'H1:GDS-CALIB_STRAIN'
I1_channel = 'H1:GDS-CALIB_STRAIN'
J1_channel = 'H1:GDS-CALIB_STRAIN'
K1_channel = 'H1:GDS-CALIB_STRAIN'

sky_locations = [[0, 0], [PI/2, 0], [PI, 0], [3*PI/4, 0], [0, .999*PI/2], [0, -.999*PI/2]]
orientations = [0, PI/3, 2*PI/3]

dim_waveforms = ['Dimmelmeier2008Rapid_s11a1o09ls.txt', 'Dimmelmeier2008Rapid_s11a1o09shen.txt', 'Dimmelmeier2008Rapid_s11a1o13ls.txt', 'Dimmelmeier2008Rapid_s11a1o13shen.txt', 'Dimmelmeier2008Rapid_s11a2o05shen.txt', 'Dimmelmeier2008Rapid_s11a2o07ls.txt', 'Dimmelmeier2008Rapid_s11a2o07shen.txt', 'Dimmelmeier2008Rapid_s11a2o09ls.txt', 'Dimmelmeier2008Rapid_s11a2o09shen.txt', 'Dimmelmeier2008Rapid_s11a2o13ls.txt', 'Dimmelmeier2008Rapid_s11a2o13shen.txt', 'Dimmelmeier2008Rapid_s11a2o15ls.txt', 'Dimmelmeier2008Rapid_s11a2o15shen.txt', 'Dimmelmeier2008Rapid_s11a3o05ls.txt', 'Dimmelmeier2008Rapid_s11a3o05shen.txt', 'Dimmelmeier2008Rapid_s11a3o07ls.txt', 'Dimmelmeier2008Rapid_s11a3o07shen.txt', 'Dimmelmeier2008Rapid_s11a3o09ls.txt', 'Dimmelmeier2008Rapid_s11a3o09shen.txt', 'Dimmelmeier2008Rapid_s11a3o12ls.txt', 'Dimmelmeier2008Rapid_s11a3o12shen.txt', 'Dimmelmeier2008Rapid_s11a3o13ls.txt', 'Dimmelmeier2008Rapid_s11a3o13shen.txt', 'Dimmelmeier2008Rapid_s11a3o15ls.txt', 'Dimmelmeier2008Rapid_s11a3o15shen.txt', 'Dimmelmeier2008Rapid_s15a1o07ls.txt', 'Dimmelmeier2008Rapid_s15a1o07shen.txt', 'Dimmelmeier2008Rapid_s15a1o09ls.txt', 'Dimmelmeier2008Rapid_s15a1o09shen.txt', 'Dimmelmeier2008Rapid_s15a1o13ls.txt', 'Dimmelmeier2008Rapid_s15a1o13shen.txt', 'Dimmelmeier2008Rapid_s15a2o05ls.txt', 'Dimmelmeier2008Rapid_s15a2o05shen.txt', 'Dimmelmeier2008Rapid_s15a2o07ls.txt', 'Dimmelmeier2008Rapid_s15a2o07shen.txt', 'Dimmelmeier2008Rapid_s15a2o09ls.txt', 'Dimmelmeier2008Rapid_s15a2o09shen.txt', 'Dimmelmeier2008Rapid_s15a2o13ls.txt', 'Dimmelmeier2008Rapid_s15a2o13shen.txt', 'Dimmelmeier2008Rapid_s15a2o15ls.txt', 'Dimmelmeier2008Rapid_s15a2o15shen.txt', 'Dimmelmeier2008Rapid_s15a3o05ls.txt', 'Dimmelmeier2008Rapid_s15a3o05shen.txt', 'Dimmelmeier2008Rapid_s15a3o07ls.txt', 'Dimmelmeier2008Rapid_s15a3o07shen.txt', 'Dimmelmeier2008Rapid_s15a3o09ls.txt', 'Dimmelmeier2008Rapid_s15a3o09shen.txt', 'Dimmelmeier2008Rapid_s15a3o12ls.txt', 'Dimmelmeier2008Rapid_s15a3o12shen.txt', 'Dimmelmeier2008Rapid_s15a3o13ls.txt', 'Dimmelmeier2008Rapid_s15a3o13shen.txt', 'Dimmelmeier2008Rapid_s15a3o15ls.txt', 'Dimmelmeier2008Rapid_s15a3o15shen.txt', 'Dimmelmeier2008Rapid_s20a1o07shen.txt', 'Dimmelmeier2008Rapid_s20a1o09ls.txt', 'Dimmelmeier2008Rapid_s20a1o09shen.txt', 'Dimmelmeier2008Rapid_s20a1o13ls.txt', 'Dimmelmeier2008Rapid_s20a1o13shen.txt', 'Dimmelmeier2008Rapid_s20a2o05ls.txt', 'Dimmelmeier2008Rapid_s20a2o05shen.txt', 'Dimmelmeier2008Rapid_s20a2o07ls.txt', 'Dimmelmeier2008Rapid_s20a2o07shen.txt', 'Dimmelmeier2008Rapid_s20a2o09ls.txt', 'Dimmelmeier2008Rapid_s20a2o09shen.txt', 'Dimmelmeier2008Rapid_s20a2o13ls.txt', 'Dimmelmeier2008Rapid_s20a2o13shen.txt', 'Dimmelmeier2008Rapid_s20a2o15ls.txt', 'Dimmelmeier2008Rapid_s20a2o15shen.txt', 'Dimmelmeier2008Rapid_s20a3o05ls.txt', 'Dimmelmeier2008Rapid_s20a3o05shen.txt', 'Dimmelmeier2008Rapid_s20a3o07ls.txt', 'Dimmelmeier2008Rapid_s20a3o07shen.txt', 'Dimmelmeier2008Rapid_s20a3o09ls.txt', 'Dimmelmeier2008Rapid_s20a3o09shen.txt', 'Dimmelmeier2008Rapid_s20a3o12ls.txt', 'Dimmelmeier2008Rapid_s20a3o12shen.txt', 'Dimmelmeier2008Rapid_s20a3o13ls.txt', 'Dimmelmeier2008Rapid_s20a3o13shen.txt', 'Dimmelmeier2008Rapid_s20a3o15ls.txt', 'Dimmelmeier2008Rapid_s20a3o15shen.txt', 'Dimmelmeier2008Rapid_s40a1o05shen.txt', 'Dimmelmeier2008Rapid_s40a1o07ls.txt', 'Dimmelmeier2008Rapid_s40a1o07shen.txt', 'Dimmelmeier2008Rapid_s40a1o09ls.txt', 'Dimmelmeier2008Rapid_s40a1o09shen.txt', 'Dimmelmeier2008Rapid_s40a1o13ls.txt', 'Dimmelmeier2008Rapid_s40a1o13shen.txt', 'Dimmelmeier2008Rapid_s40a2o05ls.txt', 'Dimmelmeier2008Rapid_s40a2o05shen.txt', 'Dimmelmeier2008Rapid_s40a2o07ls.txt', 'Dimmelmeier2008Rapid_s40a2o07shen.txt', 'Dimmelmeier2008Rapid_s40a2o09ls.txt', 'Dimmelmeier2008Rapid_s40a2o09shen.txt', 'Dimmelmeier2008Rapid_s40a2o13ls.txt', 'Dimmelmeier2008Rapid_s40a2o13shen.txt', 'Dimmelmeier2008Rapid_s40a2o15ls.txt', 'Dimmelmeier2008Rapid_s40a2o15shen.txt', 'Dimmelmeier2008Rapid_s40a3o05ls.txt', 'Dimmelmeier2008Rapid_s40a3o05shen.txt', 'Dimmelmeier2008Rapid_s40a3o07ls.txt', 'Dimmelmeier2008Rapid_s40a3o07shen.txt', 'Dimmelmeier2008Rapid_s40a3o09ls.txt', 'Dimmelmeier2008Rapid_s40a3o09shen.txt', 'Dimmelmeier2008Rapid_s40a3o12ls.txt', 'Dimmelmeier2008Rapid_s40a3o12shen.txt', 'Dimmelmeier2008Rapid_s40a3o13ls.txt', 'Dimmelmeier2008Rapid_s40a3o13shen.txt', 'Dimmelmeier2008Rapid_s40a3o15ls.txt', 'Dimmelmeier2008Rapid_s40a3o15shen.txt', 'Dimmelmeier2008Slow_s11a1o01ls.txt', 'Dimmelmeier2008Slow_s11a1o01shen.txt', 'Dimmelmeier2008Slow_s11a1o05ls.txt', 'Dimmelmeier2008Slow_s11a1o05shen.txt', 'Dimmelmeier2008Slow_s11a1o07ls.txt', 'Dimmelmeier2008Slow_s11a1o07shen.txt', 'Dimmelmeier2008Slow_s11a2o05ls.txt', 'Dimmelmeier2008Slow_s15a1o01ls.txt', 'Dimmelmeier2008Slow_s15a1o01shen.txt', 'Dimmelmeier2008Slow_s15a1o05ls.txt', 'Dimmelmeier2008Slow_s15a1o05shen.txt', 'Dimmelmeier2008Slow_s20a1o01ls.txt', 'Dimmelmeier2008Slow_s20a1o01shen.txt', 'Dimmelmeier2008Slow_s20a1o05ls.txt', 'Dimmelmeier2008Slow_s20a1o05shen.txt', 'Dimmelmeier2008Slow_s20a1o07ls.txt', 'Dimmelmeier2008Slow_s40a1o01ls.txt', 'Dimmelmeier2008Slow_s40a1o01shen.txt', 'Dimmelmeier2008Slow_s40a1o05ls.txt']

if mode == 'cat':
    sch_waveforms = ['Scheidegger2010_R2E1AC.txt', 'Scheidegger2010_R3E1DB.txt', 'Scheidegger2010_R3STAC.txt', 'Scheidegger2010_R4STAC.txt']
    sch_hrss = [3.812242e-23, 1.062948e-22, 1.386351e-22, 1.775823e-22]
elif mode == 'nonc':
    sch_waveforms = ['Scheidegger2010_R3E1AC.txt', 'Scheidegger2010_R4E1FC_L.txt']
    sch_hrss = [1.039807e-22, 2.126505e-22]
elif mode == 'gmode':
    #sch_waveforms = ["cross_Andresen2016_s11.txt", "cross_Andresen2016_s20.txt", "cross_Kuroda2016_sfhx.txt"]
    sch_waveforms = ["Kuroda2016_sfhx.txt"]
    #sch_hrss = [3.685189e-24, 8.988371e-24, 3.097083e-23]
    sch_hrss = [3.843638e-23]
elif mode == 'sasi':
    #sch_waveforms = ["cross_Andresen2016_s27.txt", "plus_Kuroda2016_sfhx.txt", "cross_Yakunin2017_C15.txt"]
    sch_waveforms = ["Andresen2016_s20s.txt"]
    sch_hrss = [1.644993e-23]

if mode == 'cat':
    neu_waveforms = ['Andresen2016_s20.txt', 'Kuroda2016_tm1.txt', 'Yakunin2017_C15.txt', 'Powell2018_s18.txt']
    neu_hrss = [9.144592e-24, 2.247211e-23, 7.354958e-23, 3.141536e-23]
elif mode == 'nonc':
    neu_waveforms = ['Andresen2016_s20s.txt', 'Kuroda2016_sfhx.txt']
    neu_hrss = [1.644993e-23, 3.843638e-23]
elif mode == 'gmode':
    #neu_waveforms = ["cross_Mueller2012_L15-3.txt", "cross_Mueller2012_N20-2.txt", "cross_Yakunin2017_C15.txt"]
    neu_waveforms = ["Mueller2012_L15-3.txt"]
    #neu_hrss = [1.157763e-23, 6.693082e-24, 7.451071e-23]
    neu_hrss = [1.015760e-23]
elif mode == 'sasi':
    #neu_waveforms = ["plus_Andresen2016_s11.txt", "cross_Andresen2016_s11.txt", "plus_Kuroda2016_tm1.txt"]
    neu_waveforms = ["Powell2018_s18.txt"]
    neu_hrss = [3.141536e-23]

mur_waveforms = ['Murphy2009_12_1.8.txt', 'Murphy2009_12_2.2.txt', 'Murphy2009_12_2.8.txt', 'Murphy2009_12_3.2.txt', 'Murphy2009_15_3.2.txt', 'Murphy2009_15_3.4.txt', 'Murphy2009_15_3.7.txt', 'Murphy2009_15_4.0.txt', 'Murphy2009_20_3.2.txt', 'Murphy2009_20_3.4.txt', 'Murphy2009_20_3.6.txt', 'Murphy2009_20_3.8.txt', 'Murphy2009_40_6.0.txt', 'Murphy2009_40_10.0.txt', 'Murphy2009_40_12.0.txt', 'Murphy2009_40_13.0.txt']

catalogs = [sch_waveforms, neu_waveforms]

#randomseed = str(random.randint(1, 99))
#dataseed = str(random.randint(1, 99))
#executable = /home/vincent.roma/src/lalsuite/lalapps/src/inspiral/posterior/lalinference_nest
#executable = /home/vincent.roma/public_html/SMEE/new_SMEE_repo/SMEE/lalsuite/lalinference/src/lalinference_burst
sub_string = '''executable = /home/vincent.roma/public_html/SMEE/new_SMEE_repo/SMEE/lalsuite/lalinference/src/lalinference_burst

universe = vanilla
Arguments = "--psdlength 12 --nlive 250 --nmcmc 250 --srate 4096 --seglen 3.0 --trigtime $(trigtime) --approx PrincipalCompSpec --spectrogram --progress --padding 1.0 --outfile $(outfile) --dt 1.0 --inj-ra $(ra) --ra $(ra) --inj-dec $(dec) --dec $(dec) --inj-psi $(psi) --psi $(psi) --fixsky --loghrssMin $(loghrssmin) --loghrssMax $(loghrssmax) --randomseed $(randomseed) --dataseed $(dataseed) '''
#sub_string = sub_string + randomseed + ' --dataseed ' + dataseed + ' '
#--loghrssMin -52.96 --loghrssMax -46.05

if not os.path.exists(dag_dir):
    os.makedirs(dag_dir)
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
    
if 'H1' in ifos:
    sub_string += '--ifo H1 --H1-cache ' + H1_cache + ' --H1-channel ' + H1_channel + ' --H1-flow ' + fLow + ' '
if 'L1' in ifos:
    sub_string += '--ifo L1 --L1-cache ' + L1_cache + ' --L1-channel ' + L1_channel + ' --L1-flow ' + fLow + ' '
if 'V1' in ifos:
    sub_string += '--ifo V1 --V1-cache ' + V1_cache + ' --V1-channel ' + V1_channel + ' --V1-flow ' + fLow + ' '
if 'E1' in ifos:
    sub_string += '--ifo E1 --E1-cache ' + E1_cache + ' --E1-channel ' + E1_channel + ' --E1-flow ' + fLow + ' '
if 'E2' in ifos:
    sub_string += '--ifo E2 --E2-cache ' + E2_cache + ' --E2-channel ' + E2_channel + ' --E2-flow ' + fLow + ' '
if 'E3' in ifos:
    sub_string += '--ifo E3 --E3-cache ' + E3_cache + ' --E3-channel ' + E3_channel + ' --E3-flow ' + fLow + ' '
if 'I1' in ifos:
    sub_string += '--ifo I1 --I1-cache ' + I1_cache + ' --I1-channel ' + I1_channel + ' --I1-flow ' + fLow + ' '
if 'J1' in ifos:
    sub_string += '--ifo J1 --J1-cache ' + J1_cache + ' --J1-channel ' + J1_channel + ' --J1-flow ' + fLow + ' '
if 'K1' in ifos:
    sub_string += '--ifo K1 --K1-cache ' + K1_cache + ' --K1-channel ' + K1_channel + ' --K1-flow ' + fLow + ' '

sub_string += '--rawwaveform $(inj) --psdstart $(psdstart) --nPCs ' + nPCs + ' --ncatrows 12415 --ncatcols ' + ncatcols + ' --PCfile_pluspol ' + PC_path
# --ncatrows 60840
sub_string += ''' --inj_dist_kpc $(dist) "
notification = never

request_memory = 4000
output = '''

sub_string += condor_out_dir + '''job_output_$(ID).txt
error = ''' + condor_out_dir + '''error_$(ID).txt
log = ''' + condor_out_dir + '''nest.log
accounting_group = ligo.dev.o3.burst.sn_pe.any
accounting_group_user = vincent.roma
getenv = True

queue

'''

dag_string = ''
time_active = 0

for time in times:
    for dist in distances:
        for sky_location in sky_locations:
            for orientation in orientations:
                for catalog in catalogs:
                    cat = ''
                    '''if 'Dim' in catalog[0] or 'Sch' in catalog[0]:
                        cat = 'dim'
                    elif 'Mur' in catalog[0] or 'And' in catalog[0] or 'Mue' in catalog[0] or 'Kur' in catalog[0]:
                        cat = 'mur'''
                    if catalogs.index(catalog) == 0:
                        cat = 'dim'
                    else:
                        cat = 'mur'
                    for waveform in catalog:
                        #random_add = np.random.randint(-300, 301)
                        randomseed = str(random.randint(1, 99))
                        dataseed = str(random.randint(1, 99))
                        time_active = int(time)# + random_add
                        psdstart = str(time_active - 13)
                        dist_mod = dist.replace('.', 'pt')
                        dist_float = float(dist)
                        num = str(catalog.index(waveform) + 1)
                        time_num = str(times.index(time) + 1)
                        sky_num = str(sky_locations.index(sky_location) + 1)
                        psi_num = str(orientations.index(orientation) + 1)
                        ra = str(sky_location[0])
                        dec = str(sky_location[1])
                        psi = str(orientation)
                        loghrssmin = '-52.9594571389'
                        loghrssmax = '-37.5'
                        if cat == 'dim':
                            real_hrss = sch_hrss[catalog.index(waveform)]
                            #loghrssmin = str(np.log(.2 * (10.0 / dist_float) * real_hrss))#str(np.log(.2 * (10.0 / dist_float) * hrss_min_sch))
                            #loghrssmax = str(np.log(8 * (10.0 / dist_float) * real_hrss))#str(np.log(8 * (10.0 / dist_float) * hrss_max_sch))
                        elif cat == 'mur':
                            real_hrss = neu_hrss[catalog.index(waveform)]
                            #loghrssmin = str(np.log(.2 * (10.0 / dist_float) * real_hrss))#str(np.log(.2 * (10.0 / dist_float) * hrss_min_neu))
                            #loghrssmax = str(np.log(8 * (10.0 / dist_float) * real_hrss))#str(np.log(8 * (10.0 / dist_float) * hrss_max_neu))
                        job_name = cat + '_inj' + num + '_t' + time_num + '_s' + sky_num + '_p' + psi_num + '_' + dist_mod + 'kpc'

                        section_string = 'JOB ' + job_name + ' dim.sub\n' + 'RETRY ' + job_name + ' 1\n' + 'VARS ' + job_name + ' ID="' + job_name + '" outfile="' + out_dir + job_name + '" inj="' + waveform_dir + waveform + '" trigtime="' + time + '" psdstart="' + psdstart + '" randomseed="' + randomseed + '" dataseed="' + dataseed + '" dist="' + dist + '" loghrssmin="' + loghrssmin + '" loghrssmax="' + loghrssmax + '" ra="' + ra + '" dec="' + dec + '" psi="' + psi + '"\n\n'

                        dag_string += section_string
                
sub_file = open(dag_dir + 'dim.sub', 'w')
sub_file.write(sub_string)
sub_file.close()

dag_file = open(dag_dir + 'dim.dag', 'w')
dag_file.write(dag_string)
dag_file.close()
