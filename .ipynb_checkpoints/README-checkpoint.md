## Boas Vindas
Seja muito bem vindo(a) ao tutorial de implementação do framework Kedro!

Acesse o notebook "Passo a passo - projeto iris kedro.ipynb" na raiz do repositório.

Nesse notebook iremos executar o passo a passo de todas as operações executadas no projeto exemplo utilizando a base iris.

O projeto foi concebido seguindo etapas comumente empregadas na implementacao de um projeto de classificacao em produção. Funções habitualmente utilizadas nesse tipo de processo foram desenvolvidas, de forma a tornar o projeto reaproveitável como template para projetos futuros.

O detalhamento da lógica de modularização adotada está presente no artigo referência:
https://medium.com/@gdmello.nunes/kedro-construindo-projetos-de-ci%C3%AAncia-de-dados-modulares-prontos-para-produ%C3%A7%C3%A3o-72c30d1c9993

As seções do notebook irão se dividir conforme os pipelines modulares implementados no projeto, de forma que observemos os processos realizados em cada etapa:
* data_engineering
* feature_engineering
* machine_learning
* deploy_model