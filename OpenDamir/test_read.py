# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 15:36:52 2015

@author: Alexis Eidelman
"""

import os
import pandas as pd

path = 'D:\data\health\Damir\OpenDamir'

for year in range(2009, 2014):
    file_name = os.path.join(path, 'P_DSEXP_' + str(year) + '.csv')
    print pd.read_csv(file_name, sep=';', nrows=10)
