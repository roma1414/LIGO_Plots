from __future__ import division, print_function
from gwpy.timeseries import TimeSeries
from gwpy.frequencyseries import FrequencySeries
from utils import *
from scipy import signal
import noisesub as n
import cPickle, os
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

'''__all__ = ['upmult', 'resample', 'write_frame', 'subtract_cal',
           'subtract_lines']'''

def write_frame(series, filename):
    from pylal import Fr
    from gwpy.timeseries import TimeSeries

    if isinstance(series, TimeSeries):

        if series.times.value[0] % 1 != 0:
            raise ValueError('Series must start on integer second!')

        frame_dict = {}
        frame_dict['name'] = series.name
        frame_dict['data'] = series.value
        frame_dict['start'] = series.times.value[0]
        frame_dict['dx'] = series.dx.value
        frame_dict['type'] = 1
        
        print('filename = ' + str(filename))
        print('filename type = ' + str(type(filename)))

        Fr.frputvect(filename, [frame_dict])

    else:  # Assume it's a list or dict
        if isinstance(series, dict):
            series = series.items()

        start_times = [chan.times.value[0] for chan in series]

        if any([time != start_times[0] for time in start_times]):
            raise ValueError('All series must have same start time!')

        if series[0].times.value[0] % 1 != 0:
            raise ValueError('Series must start on integer second!')

        dict_list = []
        for chan in series:
            chan_dict = {}
            chan_dict['name'] = chan.name
            chan_dict['data'] = chan.value
            chan_dict['start'] = chan.times.value[0]
            chan_dict['dx'] = chan.dx.value
            chan_dict['type'] = 1
            dict_list.append(chan_dict)

        Fr.frputvect(filename, dict_list)

def plot_sensitivity(spec_1=[], title='test', spec_2=[], spec_3=[], spec_4=[], spec_5=[], spec_6=[], spec_7=[], spec_8=[], x_min=1414, x_max=1414, x_scale='log', y_min=1414, y_max=1414, y_scale='log', mode='asd', out_dir=1414, labels=['Channel 1']):

    spectra = [spec_1, spec_2, spec_3, spec_4, spec_5, spec_6, spec_7, spec_8]
    traces = len(labels)
    spectra = spectra[:traces]
    all_freqs = []
    min_freq = 0
    max_freq = 1e14
    for spec in spectra:
        if spec.frequencies[0].value > min_freq:
            min_freq = spec.frequencies[0].value
        if spec.frequencies[-1].value < max_freq:
            max_freq = spec.frequencies[-1].value
    plt.figure(figsize=(9,6))
    plt.xlabel('Frequencies')
    if mode == 'asd':
        plt.ylabel('Sensitivity Improvement Factor')
    else:
        plt.ylabel('Amp^2 / Hz^2')
    plt.title(title, fontsize = 14, y = 1.05)
    plt.grid(b=True, which='major',color='0.75',linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor',color='0.85',linestyle='--')
    plt.ticklabel_format(axis = 'y', style = 'sci', scilimits = (-2,2))
    plt.ticklabel_format(axis = 'x', style = 'sci', scilimits = (-2,2))
    ax1=plt.subplot(111)
    amps = list(spec_1.value)

    f_values = list(range(0, 8193))
    spec_1_new = np.interp(f_values, spec_1.frequencies.value, spec_1.value)
    spec_2_new = np.interp(f_values, spec_2.frequencies.value, spec_2.value)
    
    spec_final = [spec_1_new[i] / spec_2_new[i] for i in range(8193)]




    ax1.plot(f_values, spec_final, 'r', label=labels[0], zorder=1)
    ''''g', label=labels[2], zorder=3)
        amps += list(spec_3.value)
    if traces >= 4:
        ax1.plot(spec_4.frequencies.value, spec_4.value, 'k', label=labels[3], zorder=4)
        amps += list(spec_4.value)
    if traces >= 5:
        ax1.plot(spec_5.frequencies.value, spec_5.value, 'c', label=labels[4], zorder=5)
        amps += list(spec_5.value)
    if traces >= 6:
        ax1.plot(spec_6.frequencies.value, spec_6.value, 'm', label=labels[5], zorder=6)
        amps += list(spec_6.value)
    if traces >= 7:
        ax1.plot(spec_7.frequencies.value, spec_7.value, 'y', label=labels[6], zorder=7)
        amps += list(spec_7.value)
    if traces >= 8:
        ax1.plot(spec_8.frequencies.value, spec_8.value, 'burlywood', label=labels[7], zorder=8)
        amps += list(spec_8.value)'''

    legend = plt.legend(prop={'size':10})
    legend.get_frame().set_alpha(0.5)
    if x_min == 1414:
        x_min = min(spec_1.frequencies.value)
    if x_max == 1414:
        x_max = max(spec_1.frequencies.value)
    if y_min == 1414:
        y_min = min(amps)
    if y_max == 1414:
        y_max = max(amps)
    if x_scale == 'linear':
        ax1.set_xscale('linear')
    else:
        ax1.set_xscale('log')
    if y_scale == 'linear':
        ax1.set_yscale('linear')
    else:
        ax1.set_yscale('log')
    ax1.set_xlim([x_min, x_max])
    ax1.set_ylim([y_min, y_max])

    if out_dir == 1414:
        plt.savefig(title + '.png')
    else:
        if out_dir[-1] != '/':
            out_dir = out_dir + '/'
        plt.savefig(out_dir + title + '.png')
    plt.close()

def plot_spectra(spec_1=[], title='test', spec_2=[], spec_3=[], spec_4=[], spec_5=[], spec_6=[], spec_7=[], spec_8=[], x_min=1414, x_max=1414, x_scale='log', y_min=1414, y_max=1414, y_scale='log', mode='asd', out_dir=1414, labels=['Channel 1']):

    spectra = [spec_1, spec_2, spec_3, spec_4, spec_5, spec_6, spec_7, spec_8]
    traces = len(labels)
    spectra = spectra[:traces]
    all_freqs = []
    min_freq = 0
    max_freq = 1e14
    for spec in spectra:
        if spec.frequencies[0].value > min_freq:
            min_freq = spec.frequencies[0].value
        if spec.frequencies[-1].value < max_freq:
            max_freq = spec.frequencies[-1].value
    plt.figure(figsize=(9,6))
    plt.xlabel('Frequency', fontsize = 24)
    if mode == 'asd':
        plt.ylabel('ASD', fontsize = 22)
        #plt.ylabel('Amp / $\sqrt{Hz}$', fontsize = 22)
    else:
        plt.ylabel('Amp^2 / Hz')
    plt.title(title, fontsize = 24, y = 1.05)
    plt.grid(b=True, which='major',color='0.75',linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor',color='0.85',linestyle='--')
    plt.ticklabel_format(axis = 'y', style = 'sci', scilimits = (-2,2))
    plt.ticklabel_format(axis = 'x', style = 'sci', scilimits = (-2,2))
    ax1=plt.subplot(111)
    amps = list(spec_1.value)
    ax1.plot(spec_1.frequencies.value, spec_1.value, 'y', label=labels[0], zorder=1)
    if traces >= 2:
        ax1.plot(spec_2.frequencies.value, spec_2.value, 'c', label=labels[1], zorder=2)
        amps += list(spec_2.value)
    if traces >= 3:
        ax1.plot(spec_3.frequencies.value, spec_3.value, 'm', label=labels[2], zorder=3)#, linewidth=3)
        amps += list(spec_3.value)
    if traces >= 4:
        ax1.plot(spec_4.frequencies.value, spec_4.value, 'k', label=labels[3], zorder=4)#, linewidth=3)
        amps += list(spec_4.value)
    if traces >= 5:
        ax1.plot(spec_5.frequencies.value, spec_5.value, 'g', label=labels[4], zorder=5)#, linewidth=3)
        amps += list(spec_5.value)
    if traces >= 6:
        ax1.plot(spec_6.frequencies.value, spec_6.value, 'b', label=labels[5], zorder=6)#, linewidth=3)
        amps += list(spec_6.value)
    if traces >= 7:
        ax1.plot(spec_7.frequencies.value, spec_7.value, 'r', label=labels[6], zorder=7)#, linewidth=3)
        amps += list(spec_7.value)
    if traces >= 8:
        ax1.plot(spec_8.frequencies.value, spec_8.value, 'burlywood', label=labels[7], zorder=8)
        amps += list(spec_8.value)

    legend = plt.legend(prop={'size':15})
    legend.get_frame().set_alpha(0.5)
    if x_min == 1414:
        x_min = min(spec_1.frequencies.value)
    if x_max == 1414:
        x_max = max(spec_1.frequencies.value)
    if y_min == 1414:
        y_min = min(amps)
    if y_max == 1414:
        y_max = max(amps)
    if x_scale == 'linear':
        ax1.set_xscale('linear')
    else:
        ax1.set_xscale('log')
    if y_scale == 'linear':
        ax1.set_yscale('linear')
    else:
        ax1.set_yscale('log')
    ax1.set_xlim([x_min, x_max])
    ax1.set_ylim([y_min, y_max])

    if out_dir == 1414:
        plt.savefig(title + '.png')
    else:
        if out_dir[-1] != '/':
            out_dir = out_dir + '/'
        plt.savefig(out_dir + title + '.jpg')
    plt.close()

def save_time_series(time_series, out_dir=1414, frame_length=4096, frame_type='H1_HOFT_C00'):

    duration = (time_series.times[-1].value - time_series.times[0].value) + (time_series.times[1].value - time_series.times[0].value)
    if frame_length > duration:
        frame_length = duration
    
    observatory = frame_type[0]

    if out_dir == 1414:
        out_dir = ''
    else:
        if out_dir[-1] != '/':
            out_dir = out_dir + '/'
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

    epoch = float(time_series.times[0].value)
    end = epoch + duration

    while epoch < end:
        length = frame_length
        shortened = False
        if epoch + length > end:
            shortened = True
            length = end - epoch
        
        #section_data = time_series[:].crop(epoch, epoch + length)
        if shortened == False:
            section_data = time_series.crop(epoch, epoch + length)
        else:
            section_data = time_series.crop(epoch, epoch + length - 1)

        write_frame(section_data, out_dir + observatory + '-' + frame_type + '-' + str(int(epoch)) + '-' + str(int(length)) + '.gwf')

        epoch = epoch + length
        percent = (epoch - time_series.times[0].value) * 100 / duration
        print(str(percent) + ' % complete...')

def train_wf(h_data, wit_datas, fs=4096, filter_length=1, flow=100, fhigh=800):
    #wit_datas = [wit_data.value for wit_data in wit_datas]
    witnesses = []
    '''epoch = h_data.times[0].value
    duration = (h_data.times[1].value - epoch) + (h_data.times[-1].value - epoch)
    if filter_length > duration:
        filter_length = duration'''

    filter_n = fs * filter_length
    
    target = prefilter(h_data.value, flow, fhigh, fs, filt60=True)

    for wit_data in wit_datas:
        witness = prefilter(wit_data.value, flow, fhigh, fs, filt60=False)
        print('witness length = ' + str(len(witness)))
        witnesses.append(witness)
    #witnesses = prefilter(wit_datas, flow, fhigh, fs, filt60=False)

    W = n.wiener_fir(target, witnesses, filter_length)

    return W

def apply_wf_to_est(h_data, wit_data, est, W):

    '''epoch = h_data.times[0].value
    duration = (h_data.times[1].value - epoch) + (h_data.times[-1].value - epoch)

    #zBP, pBP, kBP = signal.butter(4, [flow/(fs/2), fhigh/(fs/2)], btype='bandpass', output='zpk')
    #bBP, aBP = signal.zpk2tf(zBP, pBP, kBP)

    #est = np.zeros_like(h_data)'''
    est += signal.lfilter(W, 1.0, wit_data.value)

    #est += signal.filtfilt(bBP, aBP, temp_est)
    # 0* term broadcasts to gwpy obj
    #sub = h_data.value - est

    return est

def asd_from_txt(text_file):
    the_file = open(text_file, 'r')
    the_string = the_file.read()
    the_file.close()
    the_list = the_string.split('\n')
    freqs = []
    amps = []
    for line in the_list:
        if len(line) > 0:
            line_list = line.split(' ')
            freqs.append(float(line_list[0]))
            amps.append(float(line_list[1]))

    #DF = freqs[1] - freqs[0]
    asd = FrequencySeries(amps, frequencies=freqs)#f0=freqs[0], df=DF)

    return asd

def c_asd_from_txt(text_file, fft_length=3.0, fs=4096, scale=False, dist=10.0):
    the_file = open(text_file, 'r')
    the_string = the_file.read()
    the_file.close()
    the_list = the_string.split('\n')
    df = 1.0 / fft_length    
    freqs = []
    amps = []
    N = int((fs * fft_length / 2) + 1)
    s2 = fft_length * fs
    for i in range(N):#line in the_list:
        #if len(line) > 0:
        line = the_list[i]
        line_list = line.split(' ')
        freqs.append(i*df)
        amp = (float(line_list[0])**2 + float(line_list[1])**2)**.5
        if scale == True:
            amp *= (10.0 / dist) * 2**.5 * fs**-1 * s2**-.5
        amps.append(amp)

    asd = FrequencySeries(amps, frequencies=freqs)#f0=freqs[0], df=DF)

    return asd

def time_series_from_txt(text_file, fs=4096, epoch = 111111111, name='NewTimeSeries', channel_name='H1:GDS-CALIB_STRAIN'):
    the_file = open(text_file, 'r')
    the_string = the_file.read()
    the_file.close()
    the_list = the_string.split('\n')
    hplus = []
    hcross = []
    for line in the_list:
        if len(line) > 0:
            line_list = line.split(' ')
            #if float(line_list[0]) != 0:
            hplus.append(float(line_list[0]))
            hcross.append(float(line_list[1]))
    
    data = TimeSeries(hplus, epoch=epoch, sample_rate=fs, name=name, channel=channel_name)

    return data

def downsample(data, fs):
    ratio = data.sample_rate.value / fs
    print('ratio = ' + str(ratio))
    channel_name = data.channel
    name = data.name
    epoch = data.epoch
    new_length = int(len(data) / ratio)
    print('new length = ' + str(new_length))
    #new_data = np.array(data[:new_length])#data[:new_length]
    new_data = [data[i].value for i in range(0, len(data.value), int(ratio))]
    print('new_data length = ' + str(len(new_data)))
    '''for i in range(new_length):
        new_data[i] = data[i*ratio].value
        print(str(i * 100 / new_length) + '% complete...')'''
    new_data = TimeSeries(new_data, epoch=epoch, sample_rate=fs, name=name, channel=channel_name)
    print('new_data type = ' + str(type(new_data)))
    return new_data
