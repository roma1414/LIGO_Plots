from __future__ import division
from py_help import *

dist = 50.0
fs = 4096.0
ant = .44
name = 'Spectra_50kpc'
asd_path = '/home/vincent.roma/public_html/SMEE/asds/'
time_path = '/home/vincent.roma/public_html/SMEE/time_series/'
plot_path = '/home/vincent.roma/public_html/SMEE/plots/'

#t_O1 = TimeSeries.fetch('L1:GDS-CALIB_STRAIN', 1129003217, 1129010417)
#asd_O1 = t_O1.asd(3, 1.5)
#del t_O1

asd_aLigo = asd_from_txt(asd_path + 'aLigo_4096.txt')
asd_Aplus = asd_from_txt(asd_path + 'A+_4096.txt')
asd_voyager = asd_from_txt(asd_path + 'voyager_4096.txt')
asd_ET_D = asd_from_txt(asd_path + 'ET_D_4096.txt')
asd_CE = asd_from_txt(asd_path + 'CE_4096.txt')

'''t_and = time_series_from_txt(time_path + 'Andresen2016_s20.txt')
for i in range(len(t_and.value)):
    t_and.value[i] = t_and.value[i] * (10.0 / dist)
asd_and = t_and.asd(3, 1.5)
t_sch = time_series_from_txt(time_path + 'Scheidegger2010_R3E2AC.txt')
for i in range(len(t_sch.value)):
    t_sch.value[i] = t_sch.value[i] * (10.0 / dist)
asd_sch = t_sch.asd(3, 1.5)'''


andr = np.loadtxt(time_path + 'Andresen2016_s20.txt')
and_hplus = andr[:,0]# * (10 / dist) * ant
and_hcross = andr[:,1]# * (10 / dist) * ant
sch = np.loadtxt(time_path + 'Scheidegger2010_R3E2AC.txt')
sch_hplus = sch[:,0]# * (10 / dist) * ant
sch_hcross = sch[:,1]# * (10 / dist) * ant

template_and = (and_hplus + and_hcross*1.j)
template_sch = (sch_hplus + sch_hcross*1.j) 

datafreq_and = np.fft.fftfreq(template_and.size)*fs
datafreq_sch = np.fft.fftfreq(template_sch.size)*fs

df_and = np.abs(datafreq_and[1] - datafreq_and[0])
df_sch = np.abs(datafreq_sch[1] - datafreq_sch[0])

dwindow_and = signal.tukey(template_and.size, alpha=1./8) 
dwindow_sch = signal.tukey(template_sch.size, alpha=1./8)

template_fft_and = np.fft.fft(template_and*dwindow_and) / fs
template_fft_sch = np.fft.fft(template_sch*dwindow_sch) / fs

template_f_and = np.absolute(template_fft_and)*np.sqrt(np.abs(datafreq_and))
template_f_sch = np.absolute(template_fft_sch)*np.sqrt(np.abs(datafreq_sch))

and_length = (len(datafreq_and) - 1) / 2
sch_length = (len(datafreq_sch) - 1) / 2
and_freqs = np.array([datafreq_and[i] for i in range(int(and_length))])
sch_freqs = np.array([datafreq_sch[i] for i in range(int(sch_length))])
and_amps = np.array([template_f_and[i] * (10.0 / dist) * ant for i in range(int(and_length))])
sch_amps = np.array([template_f_sch[i] * (10.0 / dist) * ant for i in range(int(sch_length))])

asd_and = FrequencySeries(and_amps, frequencies=and_freqs)#, f0=datafreq_and[0], df=df_and)
asd_sch = FrequencySeries(sch_amps, frequencies=sch_freqs)#, f0=datafreq_sch[0], df=df_sch)

plot_spectra(spec_1=asd_and, title=name, spec_2=asd_sch, spec_3=asd_aLigo, spec_4=asd_Aplus, spec_5=asd_voyager, spec_6=asd_ET_D, spec_7=asd_CE, x_min=30, x_max=2048, x_scale='log', y_min=4e-26, y_max=4e-23, y_scale='log', mode='asd', out_dir=plot_path, labels=['s20', 'R3E2AC', 'Advanced Ligo', 'A+', 'Voyager', 'Einstein Telescope', 'Cosmic Explorer'])
