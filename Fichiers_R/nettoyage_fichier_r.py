# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 15:47:31 2015

@author: leo_cdo_intern

#####################################################################################################
Ce script supprime les colonnes doublons du fichier R du DAMIR contenus dans : read_path
Les nouveaux fichiers seront créés dans: write_path
ATTENTION : Le dossier pointé dans la variable read_path, ne doit contenir que des fichiers R du DAMIR ou
            des fichers générés par ce script
#####################################################################################################
"""

########### Paramètres ci-dessous
prefix = 'reduced_' # prefixe à rajouter au nom de l'ancien fichier
read_path = '/home/debian/Documents/data/damir/DAMIR_R'
write_path = '/home/debian/Documents/data/damir/DAMIR_R'
########### Fin des paramètres

########### Script ci dessous
import pandas as pd
from os import listdir
from os.path import isfile, join

all_files = [ f for f in listdir(read_path) if isfile(join(read_path,f)) ]
all_files = [f for f in all_files if not(prefix in f)]
try:
    if (all([(f.find('.CSV') >= 0) and f[0] == 'R'])):
        counter = 0
        for file_to_read in all_files:
            print 'Currently re-writing : ', file_to_read, ' ...'
            file_read = join(read_path, file_to_read)
            file_write = join(write_path, prefix + file_to_read)
            table = pd.read_csv(file_read, sep = ';')
            columns = table.columns
            columns_to_keep = [col_name for col_name in columns if not (('l_' + col_name) in columns) or col_name == 'cpam']
            table_reduced = table[columns_to_keep]
            table_reduced.to_csv(file_write, sep = ';')
            counter += 1
        print counter, 'fichiers ont été réécrits'
    else :
        print 'Les fichiers dans le dossier "read_path" ne sont pas des fichiers R_DAMIR'
except:
    print 'Une erreur est survenue'    
########### Fin du script