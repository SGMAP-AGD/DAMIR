# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 12:23:53 2015

@author: leo_cdo_intern
#####################################################################################################
Ce script crée un CSV  à partir du fichier :
    http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=infra-population-11
    
    Disponible sur :
    http://www.insee.fr/fr/themes/detail.asp?reg_id=99&ref_id=infra-population-11
    http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/rp2011/infracommunal/infra-population-11/infra-population-2011.zip
#####################################################################################################
"""

########### Paramètres ci-dessous
write_path = '/home/debian/Documents/data/damir'
file_to_extract = 'base-ic-evol-struct-pop-2011.xls'
return_csv_name_emploi = 'professions_par_departement.csv'
return_csv_name_situ_adm = 'situation_administrative_par_departement.csv'
csv_sep = ';'
########### Fin des paramètres

########### Script ci dessous
from DAMIR_CONFIG import cat_soc_prof_1_path as read_path
import pandas as pd
from os.path import join

#Lecture de la table d'origine
print '\nlecture de la table d origine...'
file_to_read = join(read_path, file_to_extract)
table = pd.read_excel(file_to_read, skiprows = 5, header = 0, index_col = None, sheetname = 'IRIS')
columns_to_keep = ['DEP'] + [col for col in table.columns[62:] if col != 'C11_F15P']
table = table[columns_to_keep]
table[table.columns[1:]] = table[table.columns[1:]].applymap(lambda x: int(round(x)))
grouped_table = table.groupby('DEP', as_index = False).sum()

#Table des situations administratives
print 'Ecriture des nouvelles tables...'
table_situation = grouped_table.iloc[:, [0] + range(17,22)]
file_to_write = join(write_path, return_csv_name_situ_adm)
table_situation.to_csv(file_to_write, sep = csv_sep, index = False)
#Read-me : Descriptif des variables
f = open(join(write_path, return_csv_name_situ_adm[:-4] + '_readme.txt'), 'w')
list_strings = ['P11_POP_FR : Pop Français en 2011 (princ)\n', 
                'P11_POP_ETR : Pop Etrangers en 2011 (princ)\n',
                'P11_POP_IMM : Pop Immigrés en 2011 (princ) \n',
                'P11_PMEN : Pop ménages en 2011 (princ)\n',
                'P11_PHORMEN : Pop hors ménages en 2011 (princ) \n']

to_write = ''.join(list_strings)
f.write(to_write)
f.close()
print 'Table des situations administratives ecrite (1/2)'

#Table de l'emploi
table_emploi = grouped_table.iloc[:, :-5]
table_emploi = pd.melt(table_emploi, id_vars = 'DEP')
table_emploi['sexe'] = table_emploi.variable.str.contains('H')
table_emploi.loc[table_emploi['sexe'], 'sexe'] = 'h'
table_emploi.loc[table_emploi['sexe'] == False, 'sexe'] = 'f'
table_emploi['categorie'] = table_emploi.variable.str.split('_').apply(lambda x : x[-1])
table_emploi.drop('variable', axis = 1, inplace = True)
columns = [table_emploi.columns[0]] + list(table_emploi.columns[2:]) + [table_emploi.columns[1]]
table_emploi = table_emploi[columns]
table_emploi.sort('DEP', inplace = True)
file_to_write = join(write_path, return_csv_name_emploi)
table_emploi.to_csv(file_to_write, sep = csv_sep, index = False)
#Read-me : Descriptif des variables
f = open(join(write_path, return_csv_name_emploi[:-4] + '_readme.txt'), 'w')
list_strings = ['value : population de 15 ans ou plus en 2011 \n',
                'CS1 : Agriculteurs exploitants\n',
                'CS2 : Artisans, Comm., Chefs entr.\n',
                'CS3 : Cadres, Prof. intel. sup.\n',
                'CS4 : Prof. intermédiaires\n',
                'CS5 : Employés\n',
                'CS6 : Ouvriers\n',
                'CS7 : Retraités\n',
                'CS8 : Autres\n']
to_write = ''.join(list_strings)
f.write(to_write)
f.close()
print 'Table des emplois ecrite (2/2)'
print 'FIN'
########### Fin du script
