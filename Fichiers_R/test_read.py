# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 15:36:52 2015

@author: Alexis Eidelman
"""

import os
import pandas as pd

path = 'D:/data/health/Damir/Fichier R/remove_lab'

# TODO: faire bien mieux sur les dates.
for year in range(2010, 2015):
    for month in ['0' + str(x) for x in range(1,10)] + ['10', '11', '12']:
        file_name = os.path.join(path, 'R' + str(year) + month + '.CSV')
        table = pd.read_csv(file_name, sep=';')
        print year, month, table[['rec_mon', 'dep_mon', 'rem_mon', 'act_dnb']].sum()/1e6
        print (table['rec_mon'].sum()/table['act_dnb'].sum())