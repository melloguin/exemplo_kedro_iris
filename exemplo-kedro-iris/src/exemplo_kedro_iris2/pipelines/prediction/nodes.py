"""
This is a boilerplate pipeline 'prediction'
generated using Kedro 0.18.9
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


##################################################
def divide_treino_teste(iris_features:   pd.DataFrame,
                        feature_list:    list,
                        target:          str,
                       ) -> [np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    
    """
    Divide dataset de features em vetores X e Y de treino e teste

    Args:
    iris_features(pd.DataFrame): dataframe de features

    Returns:
    X_train(np.ndarray): array com features para treinamento do modelo
    X_test(np.ndarray):  array com features para predição
    Y_train(np.ndarray): array com rótulos para treinamento do modelo
    Y_test(np.ndarray):  array com rótulos para validação da predição
    
    """

    # Converte dataframes para arrays
    X = iris_features[feature_list].values
    Y = iris_features[[target]].values

    # Divide dataframes em treino e teste
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, stratify = Y, test_size=0.33, random_state=42)

    
    # Avalia balanceamento de classes em dataset de treino e teste
    unique, counts = np.unique(Y_train, return_counts=True)
    print('distribuição treino',dict(zip(unique,counts)))

    unique, counts = np.unique(Y_test, return_counts=True)
    print('distribuição treino',dict(zip(unique,counts)))

    
    return [X_train, X_test, Y_train, Y_test]



##################################################
def realiza_classificacoes(knn_classifier,
                           svm_classifier,
                           df_test: pd.DataFrame,
                           X_test:  np.ndarray,
                           Y_test:  np.ndarray,
                          ) -> pd.DataFrame:
    
    """
    Carrega classificadores KNN e SVM pré treinados e realiza classificações sobre valores de X_test

    Args:
    knn_classifier(pkl):   classificador KNN treinado
    svm_classifier(pkl):   classificador SVM treinado
    df_test(pd.DataFrame): contém instâncias (features e rótulos) para teste
    X_test(np.ndarray):    array com features para predição
    Y_test(np.ndarray):    array com rótulos para validação da predição

    Returns:
    df_predicoes(pd.DataFrame): dataframe com predições de SVM e KNN, features utilizadas e rótulos verdadeiros
    
    """

    ### Realiza predições e printa score de acurácia
    knn_pred = knn_classifier.predict(X_test)
    print('Acurácia KNN:', accuracy_score(Y_test, knn_pred))

    svm_pred = svm_classifier.predict(X_test)
    print('Acurácia SVM:', accuracy_score(Y_test, svm_pred))

    ### Adiciona predições a dataset
    df_predicoes = df_test.copy()
    
    df_predicoes['knn_species'] = knn_pred
    df_predicoes['svm_species'] = svm_pred
    
    return df_predicoes