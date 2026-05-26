# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from bs_plotmaker_lib import *
         
all_locations = ['BS', 'ITMX', 'ITMY', 'ETMX', 'ETMY', 'HAM1', 'HAM2', 'HAM6']
ST1_locations = ['BS', 'ITMX', 'ITMY', 'ETMX', 'ETMY', 'HAM2', 'HAM6']
ST2_locations = ['BS', 'ITMX', 'ITMY', 'ETMX', 'ETMY']

make_plot(all_locations, 'slope', 'HPI')
make_plot(all_locations, 'p_value', 'HPI')
make_plot(ST1_locations, 'slope', 'ST1')
make_plot(ST1_locations, 'p_value', 'ST1')
make_plot(ST2_locations, 'slope', 'ST2')
make_plot(ST2_locations, 'p_value', 'ST2')