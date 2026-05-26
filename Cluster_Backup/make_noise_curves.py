from py_help import *

out_dir = '/home/vincent.roma/public_html/SMEE/ASDs/'
Aplus_cache = '/home/vincent.roma/public_html/SMEE/caches/rec_A+.cache'
voyager_cache = '/home/vincent.roma/public_html/SMEE/caches/rec_voyager.cache'
ET_D_cache = '/home/vincent.roma/public_html/SMEE/caches/rec_ET_D.cache'
CE_cache = '/home/vincent.roma/public_html/SMEE/caches/rec_CE.cache'
kagra_cache = '/home/vincent.roma/public_html/SMEE/caches/rec_kagra.cache'
aVirgo_cache = '/home/vincent.roma/public_html/SMEE/caches/rec_aVirgo.cache'

O1_time = TimeSeries.fetch('L1:GDS-CALIB_STRAIN', 1128254417, 1128255417)
O1_asd = O1_time.asd(8, 4)
#del O1_time
Aplus_time = TimeSeries.read(Aplus_cache, 'L1:GDS-CALIB_STRAIN')
Aplus_asd = Aplus_time.asd(8, 4)
#del Aplus_time
voyager_time = TimeSeries.read(voyager_cache, 'H1:GDS-CALIB_STRAIN')
voyager_asd = voyager_time.asd(8, 4)
#del voyager_1_time
ET_D_time = TimeSeries.read(ET_D_cache, 'L1:GDS-CALIB_STRAIN')
ET_D_asd = ET_D_time.asd(8, 4)
#del ET_D_time
CE_time = TimeSeries.read(CE_cache, 'L1:GDS-CALIB_STRAIN')
CE_asd = CE_time.asd(8, 4)
#del CE_time
kagra_time = TimeSeries.read(kagra_cache, 'H1:GDS-CALIB_STRAIN')
kagra_asd = kagra_time.asd(8, 4)
#del kagra_time
aVirgo_time = TimeSeries.read(aVirgo_cache, 'H1:GDS-CALIB_STRAIN')
aVirgo_asd = aVirgo_time.asd(8, 4)
#del CE_time

plot_spectra(spec_1=O1_asd, title='Recolored Noise Curves', spec_2=kagra_asd, spec_3=aVirgo_asd, spec_4=Aplus_asd, spec_5=voyager_asd, spec_6=ET_D_asd, spec_7=CE_asd, x_min=30, x_max=2048, out_dir=out_dir, labels=['O1 LLO (Not Recolored)', 'Kagra', 'aVirgo', 'A+', 'Voyager', 'Einstein Telescope', 'Cosmic Explorer'], y_min=1e-25, y_max=1e-20)

