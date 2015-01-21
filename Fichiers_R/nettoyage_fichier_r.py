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

from DAMIR_CONFIG import nettoyage_fichier_R_1_path as read_path
import os
import pandas as pd


def remove_redondant_columns(read_path, write_path, drop=None, keep_label_more_than_num=False):
    assert read_path != write_path

    fichiers_R = [f for f in os.listdir(read_path)
                  if f[:3] == 'R20' and f[-4:] == '.CSV' and len(f) == 11]

    for file_to_read in fichiers_R:
        print 'Currently re-writing : ', file_to_read, ' ...'
        file_read = os.path.join(read_path, file_to_read)
        file_write = os.path.join(write_path, file_to_read)
        table = pd.read_csv(file_read, sep=';')
        if drop is not None:
            table.drop(drop, axis=1, inplace=True)
        table.rename(columns={'SERIE': 'serie'}, inplace=True)
        cols = table.columns
        cols_with_label = [col for col in cols if 'l_' + col in cols]
        labels = ['l_' + col for col in cols_with_label]
        if keep_label_more_than_num:
            table_reduced = table.drop(cols_with_label, axis=1)
        else:
            table_reduced = table.drop(labels, axis=1)
        table_reduced.to_csv(file_write, sep=';')


def var_is_aggregation_of_an_other(read_path, var1, var2):
    ''' renvoie un dictionnaire avec pour chaque département
        la liste des CPAM qu'il contient '''
    fichier_R = [f for f in os.listdir(read_path)
                 if f[:3] == 'R20' and f[-4:] == '.CSV' and len(f) == 11][0]
    file_read = os.path.join(read_path, fichier_R)
    tab = pd.read_csv(file_read, sep=';')
    cpam_by_dep = tab[[var1, var2]].drop_duplicates([var1, var2])
    assert cpam_by_dep[var2].value_counts().max() == 1
    print 'on a bien ' + var2 + ' dans ' + var1
    file_name = os.path.join(read_path, 'cpam_by_dep.csv')
    cpam_by_dep.to_csv(file_name, index=False)


def to_one_file(path):
    fichiers_R = [f for f in os.listdir(path)
                  if f[:3] == 'R20' and f[-4:] == '.CSV' and len(f) == 11]

    outfile = os.path.join(path, 'Fichier_R.csv')
    output = pd.DataFrame()
    # TODO: faire le dump directement plutôt que de tout charger
    for file_to_read in fichiers_R[:2]:
        table = pd.read_csv(os.path.join(path, file_to_read), sep=';')
        output = output.append(table)

    output.to_csv(outfile)



if __name__ == '__main__':
    write_path = 'D:/data/health/Damir/fichier R/remove_lab'
    remove_redondant_columns(read_path, write_path, keep_label_more_than_num=False)
    var_is_aggregation_of_an_other(write_path, 'dpt', 'cpam')
    var_is_aggregation_of_an_other(write_path, 'region', 'cpam')
    var_is_aggregation_of_an_other(write_path, 'region', 'dpt')

