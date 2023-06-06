"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 0.18.7
"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


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
def dataframes_treino_teste(X_train: np.ndarray,
                            X_test:  np.ndarray,
                            Y_train: np.ndarray,
                            Y_test:  np.ndarray,
                            feature_list:  list,
                            target:         str,
                           ) -> [pd.DataFrame, pd.DataFrame]:
    
    """
    Armazena valores de X_train e Y_train em dataframe de treinamento (df_train) e valores de X_test e Y_test em dataframe de teste (df_test)

    Args:
    X_train(np.ndarray): array com features para treinamento do modelo
    X_test(np.ndarray):  array com features para predição
    Y_train(np.ndarray): array com rótulos para treinamento do modelo
    Y_test(np.ndarray):  array com rótulos para validação da predição

    Returns:
    df_train(pd.DataFrame): contém instâncias (features e rótulos) para treinamento
    df_test(pd.DataFrame):  contém instâncias (features e rótulos) para teste
    """

    # Trata valores  
    df_train = pd.DataFrame({target:Y_train.ravel()})
    df_test  = pd.DataFrame({target:Y_test.ravel()})


    for f in range(len(feature_list)):
        df_train[feature_list[f]] = X_train[:,f]
        df_test[feature_list[f]]  = X_test[:,f]


    return [df_train, df_test]



##################################################
def treinamento_knn_svm(X_train: np.ndarray,
                        Y_train: np.ndarray,
                        k_neighbors: int,
                       ):
    
    """
    Treina classificadores KNN e SVM

    Args:
    X_train(np.ndarray): array com features para treinamento do modelo
    Y_train(np.ndarray): array com rótulos para treinamento do modelo

    Returns:
    knn_classifier(pkl): classificador KNN treinado
    svm_classifier(pkl): classificador SVM treinado
    """

    # Treina classificador KNN
    knn_classifier = KNeighborsClassifier(k_neighbors)
    knn_classifier.fit(X_train,Y_train.ravel())

    # Treina classificador SVM
    svm_classifier = SVC()
    svm_classifier.fit(X_train,Y_train.ravel())

    return [knn_classifier, svm_classifier]