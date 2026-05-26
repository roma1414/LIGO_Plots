from __future__ import division
from optparse import OptionParser
from gwpy.detector import Channel
from gwpy.detector import ChannelList
from gwpy.timeseries import TimeSeries
#from gwpy.spectrum import Spectrum
from gwpy.frequencyseries import FrequencySeries
#from gwpy.plotter import TimeSeriesPlot
#from gwpy.plotter import SpectrumPlot
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

results_dir = '/home/vincent.roma/public_html/SMEE/results_noise/sch_review/'

data = []
a = 0
num_bins = 20
out_dir = '/home/vincent.roma/public_html/SMEE/plots/'
file_name = 'noise_sch_review.png'

for i in range(1000):
    try:
        new_file = open(results_dir + 'run_' + str(i+1) + '_B.txt')
        new_string = new_file.read()
        line_list = new_string.split()
        data.append(float(line_list[0]))
    except:
        a += 0

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

def make_plot(num_bins, x_min, x_max):
    bins = plt.hist(data, num_bins, (x_min, x_max))
    plt.xlim([x_min, x_max])
    plt.title('1000 runs on Noise')
    plt.ylabel('Occurences')
    plt.xlabel('logBsn')
    plt.savefig(out_dir + file_name)
    plt.close()

data = [x for x in data if x <= 325]
N = len(data)
mean = sum(data) / N
std_dev = stdDev(data)
x_min = mean - 6 * std_dev
x_max = mean + 6 * std_dev
MIN = min(data)
MAX = max(data)

make_plot(num_bins, x_min, x_max)

print('Number of data points = ' + str(N))
print('mean = ' + str(mean))
print('std_dev = ' + str(std_dev))
print('min = ' + str(MIN))
print('max = ' + str(MAX))
#data = sorted(data)
#print('data = ')
#print(data)
