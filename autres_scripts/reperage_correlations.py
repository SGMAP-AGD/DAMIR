# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 15:44:35 2015

@author: leo_cdo_intern

#####################################################################################################
Ce fichier contient : 
    - Un script de réduction de table, en supprimant les colonnes pouvant être déduites d'autres colonnes,
        qui génère par ailleurs des prédicteurs capables de reconstituer la base initiale
    - Un script qui permet de sauvegarder les prédicteurs ainsi créés (TODO)
    - Un script permettant de reconstruire la base initiale, ou seullement certaines variables (ou seulement... : TODO)
    
Il est destiné à être utilise sur les variables categorielles
#####################################################################################################
"""

from DAMIR_CONFIG import DAMIR_P as path
from os.path import join
import pandas as pd
from itertools import combinations



# TODO : Créer une nouvelle fonction pour les implications
# TODO : enlever tous les apply : all(smaller_table.groupby(list_of_columns)[variable_to_predict].nunique() == 1)
def check_all_implications(table, list_of_columns): 
    '''Checks if variable_to_predict is predicted by list_of_columns'''
    implicates = [x for x in list(table.columns) if (not x in list_of_columns)]
    for x in [0.00005, 0.0002, 0.001, 0.01, 0.1, 1]:
        new_len = int(len(table) * x)

        if new_len > 0:
            smaller_table = table[implicates + list_of_columns].iloc[:new_len]
            is_unique = smaller_table.groupby(list_of_columns).apply(lambda x: x[implicates].apply(lambda y: y.nunique() == 1)).apply(all)

            implicates = list(is_unique.index[is_unique])        
            if len(implicates) == 0:
                return []
    return implicates
   

def get_all_predictions(table, list_of_columns, implications):
    return table[list_of_columns + implications].groupby(list_of_columns, as_index = False).apply(lambda x: x.iloc[0])


def recreate_original_table(new_table, list_of_predictors):
    '''Recreate full table with list'''
    for i in [len(list_of_predictors) - x - 1 for x in range(len(list_of_predictors))]:
        prediction = list_of_predictions[i]        
        print 'Adding :', [x for x in prediction['table'].columns if not(x in prediction['predictors'])], 'predicted by', prediction['predictors']
        new_table = new_table.merge(prediction['table'], on = prediction['predictors'], how = 'left')
    return new_table


def minimize(table, max_nb_predictors, columns_to_analyse = None):
    print 'Reformating table for exploration ...'
    new_table = table.copy()
    if columns_to_analyse == None:
        columns_to_analyse = list(new_table.columns)
    
    nunique_by_col = new_table[columns_to_analyse].apply(lambda x: x.nunique())
    nunique_by_col.sort(ascending = False)
    columns = list(nunique_by_col.index)
    new_table = new_table[columns]

    ind = list(new_table.index)
    shuffle(ind)
    new_table = new_table.loc[ind]
    
    list_of_predictions = []
    for nb_predictors in range(1,min(len(columns_to_analyse), max_nb_predictors + 1)):
        print '\nCurrently testing', nb_predictors, 'predictors'
        all_combinations = combinations([x for x in columns_to_analyse if x in new_table.columns], nb_predictors)
        all_combinations_len = sum([1 for x in all_combinations])
        
        # Open status bar
        num_bar = 20        
        cases_tested = 0
        bar_status = 0
        print '[',
                
        for list_of_columns in combinations([x for x in columns_to_analyse if x in new_table.columns], nb_predictors):
            # Fill status bar            
            for i in range(bar_status, int(num_bar * cases_tested /all_combinations_len)):
                print '=',
            bar_status = int(num_bar * cases_tested /all_combinations_len)
            cases_tested += 1
            
            if all([x in new_table.columns for x in list_of_columns]) and (nb_predictors < new_table.shape[1]): # On vérifie que la combinaison de variables est bien dans new_table et que cette combinaison n'englobe pas la table entière
#                print 'currently checking implications of', list_of_columns
                all_implications = check_all_implications(new_table, list(list_of_columns))
                if len(all_implications) != 0:
#                    print list_of_columns, '    >>> predicts', all_implications
                    prediction = dict()
                    prediction['predictors'] = list_of_columns
                    prediction['predicted'] = all_implications
                    prediction_tab = get_all_predictions(table, list(list_of_columns), all_implications)
                    prediction_tab.index = range(len(prediction_tab))
                    prediction['table'] = prediction_tab
                    list_of_predictions += [prediction]
                    new_table.drop(all_implications, axis = 1, inplace = True)
            
        # Close status bar
        print ']'
    new_table[[x for x in new_table.columns if not(x in columns_to_analyse)]] = table[[x for x in new_table.columns if not(x in columns_to_analyse)]]                  
    return [new_table, list_of_predictions]

def print_predictions(list_of_predictions):
    if len(list_of_predictions) == 0:
        print 'no predictions ...'
    else:
        for prediction in list_of_predictions:
            print prediction['predictors'], 'predicts', prediction['predicted']

if __name__ == '__main__':

    table = pd.read_csv(join(path, 'P_DSEXP_2012.csv'), sep = ';', nrows = 5000000)
    columns_to_analyse = ['SERIE', 'exe_spe', 'REM_TAU']
    skip_columns = ['FLT_ACT_COG', 'FLT_ACT_NBR', 'FLT_ACT_QTE', 'FLT_DEP_MNT', 'FLT_PAI_MNT', 'FLT_REM_MNT', 'Unnamed: 55',
                    'PRS_ACT_COG', 'PRS_ACT_NBR', 'PRS_ACT_QTE', 'PRS_DEP_MNT', 'PRS_PAI_MNT', 'PRS_REM_MNT', 'PRS_REM_BSE']
    columns_to_analyse = [col for col in table.columns if not(col in skip_columns)]
    nombre_max_predicteurs = 2
    [new_table, list_of_predictions] = minimize(table, nombre_max_predicteurs, columns_to_analyse = columns_to_analyse)#columns_to_analyse)

       
#def check_implication(table, list_of_columns, variable_to_predict): 
#    '''Checks if variable_to_predict is predicted by list_of_columns'''
#    for x in [0.0002, 0.001, 0.01, 0.1, 1]:
##        print 'currently testing with ratio : ', x
#        smaller_table = table.iloc[:int(len(table) * x)]
#        implicates = all(smaller_table.groupby(list_of_columns)[variable_to_predict].nunique() == 1)
#        if not implicates:
#            return False
#    return True

#def get_prediction(table, list_of_columns, variable_to_predict):
#    return table[list_of_columns + [variable_to_predict]].groupby(list_of_columns, as_index = False).apply(lambda x: x.iloc[0])