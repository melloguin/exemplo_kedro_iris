"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.18.7
"""

import pandas as pd

##################################################
def calcula_features_area(iris_data:   pd.DataFrame,
                         ) -> pd.DataFrame:
    
    """
    Calcula features de área da sépala e área da pétala no dataframe iris_data

    Args:
    iris_data(pd.DataFrame): dataframe original

    Returns:
    iris_features(pd.DataFrame): dataframe contendo as features calculadas
    """
    
    iris_features = iris_data.copy()

    iris_features['sepal_area'] = iris_features['sepal_length'] * iris_features['sepal_width']
    iris_features['petal_area'] = iris_features['petal_length'] * iris_features['petal_width']

    return iris_features