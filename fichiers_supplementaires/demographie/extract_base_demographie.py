# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 10:25:02 2015

@author: leo_cdo_intern

#####################################################################################################
Ce script crée un CSV unique à partir du fichier :
    Estimation de population par département, sexe et âge quinquennal - Années 1975 à 2014 
    
    Disponible sur :
    http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=estim-pop
    http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/estim-pop/estim-pop-dep-sexe-aq-1975-2014.xls
#####################################################################################################
"""

########### Paramètres ci-dessous
write_path = '/home/debian/Documents/data/damir'
file_to_extract = 'pop_par_dep_par_an.xls'
return_csv_name = 'pop_par_dep_par_an_regroupe.csv'
csv_sep = ';'

an_debut = 2009
an_fin = 2014
########### Fin des paramètres


########### Script ci dessous
from DAMIR_CONFIG import demographie_1_path as read_path
import pandas as pd
from os.path import join

try:    
    table_globale = pd.DataFrame()
    for annee in range(2009, an_fin + 1):
        file_to_read = join(read_path, file_to_extract)
        table = pd.read_excel(file_to_read, header = 0, skip_footer = 4, skiprows = 4, index_col = None, sheetname = str(annee))
        
        table.drop(table.columns[2:23], axis = 1, inplace = True) #Suprimer les colonnes hommes + femme 
        table.drop([x for x in table.columns if 'Total' in x], axis = 1, inplace = True) # Supprimer les colonnes total homme et total femmes
        columns = ['dep', 'l_dep'] + ['h_' + str(i*5) + '_' + str((i+1)*5 - 1) for i in range(19)] + ['h_95_inf'] + ['f_' + str(i*5) + '_' + str((i+1)*5 - 1) for i in range(19)] + ['f_95_inf']
        table.columns = columns
        table['annee'] = str(annee)
        columns = list(table.columns[:2]) + list([table.columns[-1]]) + list(table.columns[2:-1])
        table = table[columns]
        table = table[table.l_dep.notnull()]
        table_globale = table_globale.append(table)
        

 
    table_globale = pd.melt(table_globale, id_vars = ['dep', 'l_dep', 'annee'])
    table_globale['sexe'] = table_globale['variable'].apply(lambda x: x[0])
    table_globale['age_max_cat'] = table_globale['variable'].str.split('_').apply(lambda x: x[-1])
    table_globale.drop('variable', axis = 1, inplace = True)
    
    columns = list(table_globale.columns[:3]) + list(table_globale.columns[4:]) + [table_globale.columns[3]]
    table_globale = table_globale[columns]
    table_globale.sort(['l_dep', 'annee'], inplace = True)
    
    file_to_write = join(write_path, return_csv_name)
    table_globale.to_csv(file_to_write, sep = csv_sep, index = False)
    
    print 'Le nouveau fichier a été créé dans :', write_path
except:
    print 'Une erreur est survenue'
########### Fin du script