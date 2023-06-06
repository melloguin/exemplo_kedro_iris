"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (calcula_features_area
                   )


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        
        node(
            func=calcula_features_area,
            inputs=['iris_data',
                   ],
            outputs='iris_features',
            name='Calcula_features_area'
        )

    ])