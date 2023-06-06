"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.7
"""

import pandas as pd

##################################################
def concatenacao_inputs(sepal_data:   pd.DataFrame,
                        petal_data:   pd.DataFrame,
                        species_data: pd.DataFrame,
                        concatenacao: str,
                       ) -> pd.DataFrame:
    
    """
    Unifica dataframes sepal_data, petal_data e species_data em um dataframe único (iris_data)

    Args:
    sepal_data(pd.DataFrame):   dataframe contendo as informações de sépala
    petal_data(pd.DataFrame):   dataframe contendo as informações de pétala
    species_data(pd.DataFrame): dataframe contendo os rótulos de espécie de flor

    Returns:
    iris_data(pd.DataFrame): dataframe contendo todas as informações
    """
    
    iris_data = sepal_data[['example','sepal_length','sepal_width']].merge(petal_data[['example','petal_length','petal_width']], 
                                                                           on = 'example', 
                                                                           how = 'left'
                                                                   ).merge(species_data[['example','species']], 
                                                                           on = 'example', 
                                                                           how = 'left'
                                                                   )

    return iris_data



##################################################
def limpeza_conversao_colunas(iris_data: pd.DataFrame
                             ) -> pd.DataFrame:
    
    """
    Trata valores de iris_data, removendo caracteres indesejados e convertendo colunas para float
    (estavam como string) devido aos caracteres indesejados

    Args:
    iris_data(pd.DataFrame): contém informações sem tratamento

    Returns:
    iris_data(pd.DataFrame): contém informações tratadas comtipo ajustado
    """

    # Trata valores  
    iris_data['sepal_length'] = iris_data['sepal_length'].replace({'a- ':'', ',':'.'},regex=True)
    iris_data['sepal_width']  = iris_data['sepal_width'].replace({',,':'.',',':'.'},regex=True)
    iris_data['petal_length'] = iris_data['petal_length'].replace({',':'.'},regex=True)
    iris_data['petal_width']  = iris_data['petal_width'].replace({',':'.'},regex=True)

    # Converte colunas
    iris_data['sepal_length'] = iris_data['sepal_length'].astype(float)
    iris_data['sepal_width']  = iris_data['sepal_width' ].astype(float)
    iris_data['petal_length'] = iris_data['petal_length'].astype(float)
    iris_data['petal_width']  = iris_data['petal_width' ].astype(float)

    # Check consistência tratamentos
    print('iris_data tratada. valores nulos por coluna:')
    print(iris_data.isna().sum())

    return iris_data
