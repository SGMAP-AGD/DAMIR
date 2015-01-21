# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 15:47:31 2015

@author: leo_cdo_intern

#####################################################################
Ce script crée une table simplifiée à partir des fichiers R du DAMIR.
Ils doivent se trouver dans le dossier : read_path
Les nouveaux fichiers seront créés dans: write_path
######################################################################
"""

import pandas as pd
import os

########### Paramètres ci-dessous
prefix = 'reduced_' # prefixe à rajouter au nom de l'ancien fichier
read_path = '/home/debian/Documents/data/damir/DAMIR_R'
write_path = '/home/debian/Documents/data/damir/DAMIR_R'
########### Fin des paramètres


########### Script ci dessous
all_files = [f for f in os.listdir(read_path)
                if f[:3] == 'R20' & f[-4:] == '.CSV' & len(f) == 11]

counter = 0
for file_to_read in all_files:
    print 'Currently re-writing : ', file_to_read, ' ...'
    file_read = os.path.join(read_path, file_to_read)
    file_write = os.path.join(write_path, prefix + file_to_read)
    table = pd.read_csv(file_read, sep = ';')
    columns = table.columns
    columns_to_keep = [col_name for col_name in columns if not (('l_' + col_name) in columns) or col_name == 'cpam']
    table_reduced = table[columns_to_keep]
    table_reduced.to_csv(file_write, sep = ';')
    counter += 1
print counter, 'fichiers ont été réécrits'
#except:
#    print 'Une erreur est survenue'
########### Fin du script