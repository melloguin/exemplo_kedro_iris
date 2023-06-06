"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (divide_treino_teste,
                    dataframes_treino_teste,
                    treinamento_knn_svm
                   )


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        
        node(
            func=divide_treino_teste,
            inputs=['iris_features',
                    'params:feature_list',
                    'params:target'
                   ],
            outputs=['X_train', 
                     'X_test', 
                     'Y_train', 
                     'Y_test'
                    ],
            name='Divide_treino_teste'
        ),
        

        node(
            func=dataframes_treino_teste,
            inputs = ['X_train', 
                      'X_test', 
                      'Y_train', 
                      'Y_test',
                      'params:feature_list',
                      'params:target'
                     ],
            outputs= ['df_train',
                      'df_test'
                     ],
            name='Dataframes_treino_teste'
        ),
        

        node(
            func=treinamento_knn_svm,
            inputs = ['X_train', 
                      'Y_train', 
                      'params:k_neighbors'
                     ],
            outputs= ['knn_classifier', 
                      'svm_classifier', 
                     ],
            name='Treinamento_knn_svm'
        )

    ])