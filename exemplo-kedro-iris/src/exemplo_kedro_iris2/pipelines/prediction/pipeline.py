"""
This is a boilerplate pipeline 'prediction'
generated using Kedro 0.18.9
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (divide_treino_teste,
                    realiza_classificacoes
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
            func=realiza_classificacoes,
            inputs=['knn_classifier',
                    'svm_classifier',
                    'df_test',
                    'X_test',
                    'Y_test'
                   ],
            outputs='df_predicoes',
            name='Realiza_classificacoes'
        )

    ])