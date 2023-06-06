"""Project pipelines."""

from typing import Dict
from kedro.pipeline import Pipeline, pipeline
from kedro.framework.project import find_pipelines
from exemplo_kedro_iris2.pipelines import (data_engineering, 
                                           feature_engineering,
                                           model_training,
                                           prediction,
                                          )

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    DE   = data_engineering.create_pipeline()
    FE   = feature_engineering.create_pipeline()
    MT   = model_training.create_pipeline()
    PD   = prediction.create_pipeline()
    
    return {
        "__default__":                   DE + FE,
        "pipeline_treinamento":          DE + FE + MT,
        "pipeline_previsao":             DE + FE + PD
    }
