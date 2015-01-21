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
import os
import pandas as pd


def remove_redondant_columns(read_path, write_path, keep_label_more_than_num=False):
    assert read_path != write_path

    fichiers_R = [f for f in os.listdir(read_path)
                  if f[:3] == 'R20' and f[-4:] == '.CSV' and len(f) == 11]

    for file_to_read in fichiers_R:
        print 'Currently re-writing : ', file_to_read, ' ...'
        file_read = os.path.join(read_path, file_to_read)
        file_write = os.path.join(write_path, file_to_read)
        table = pd.read_csv(file_read, sep=';')
        table.rename(columns={'SERIE': 'serie'}, inplace=True)
        cols = table.columns
        cols_with_label = [col for col in cols if 'l_' + col in cols]
        labels = ['l_' + col for col in cols_with_label]
        if keep_label_more_than_num:
            table_reduced = table.drop(cols_with_label, axis=1)
        else:
            table_reduced = table.drop(labels, axis=1)
        table_reduced.to_csv(file_write, sep=';')


if __name__ == '__main__':
    read_path = 'D:/data/health/Damir/fichier R'
    write_path = 'D:/data/health/Damir/fichier R/remove_lab'
    remove_redondant_columns(read_path, write_path, keep_label_more_than_num=False)