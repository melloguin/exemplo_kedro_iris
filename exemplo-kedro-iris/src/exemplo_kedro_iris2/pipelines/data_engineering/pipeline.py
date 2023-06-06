"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (concatenacao_inputs,
                    limpeza_conversao_colunas
                   )


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        
        node(
            func=concatenacao_inputs,
            inputs=['sepal_data',
                    'petal_data',
                    'species_data',
                    'params:concatenacao'
                   ],
            outputs='iris_data_raw',
            name='Concatenacao_inputs'
        ),
        

        node(
            func=limpeza_conversao_colunas,
            inputs = ['iris_data_raw'
                     ],
            outputs=  'iris_data',
            name='Limpeza_conversao_colunas'
        )

    ])
