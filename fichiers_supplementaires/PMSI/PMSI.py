# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 16:12:38 2015

@author: Alexis Eidelman
"""

import os
import pandas as pd

path = 'M:/PMSI'

year = 2012
for year in range(2011, 2014):
    filename = 'mco_finess_racine_cg_' + str(year) + '.csv'
    filepath = os.path.join(path, filename)
    
    tab = pd.read_csv(filepath, sep=';')
    
    #tab.groupby(['codeGeo'])['finess'].count()
    #tab.groupby(['finess'])['codeGeo'].count()
#    print tab.groupby(['finess', 'codeGeo'])['effectif'].sum().min()
    
    # aggregation by departement
    file_loc = os.path.join(path, 'corresp_codegeo_codecom_pop.csv')
    loc = pd.read_csv(file_loc, sep=';')
    loc = loc[['code_geo', 'dep']].drop_duplicates()
    
    tab = tab.merge(loc, left_on='codeGeo', right_on='code_geo', how='left')
    
    agg = tab.groupby(['finess', 'dep', 'racine'])['effectif'].sum().reset_index()
    assert agg.groupby(['finess', 'dep'])['effectif'].sum().min() > 4
    fileout = 'mco_finess_racine_dep_' + str(year) + '.csv'
    path_out = os.path.join(path, fileout)
    agg.to_csv(path_out, sep=';', index=False)