# Aplicação

## Projeto de exemplo: pré-processamento de dados de base de Telecom

No exemplo presente em `churn_preprocessing.py` temos uma aplicação de todos os conceitos apresentados nesta introdução à linguagem Python. Nele, fazemos o pré-processamento de uma base de dados de Telecom pra indicar se um dado cliente vai ou não manter o serviço.

<br/>

Ressalta-se, contudo, que esta é uma representação apenas para fins didáticos, podendo er considerado um _toy problem_. Costumeiramente em Engenharia e Ciência de Dados lida-se com bases bem maiores e problemas mais complexos.

## Configuração
- Python version: 3.8

## Configuração do ambiente de desenvolvimento

Os seguintes comandos devem ser executados via linha de comando.

1. Criação do ambiente virtual
```shell-session
virtualenv -p 3.8 .virtualenv
```
2. Inicialização do ambiente virtual
```shell-session
source .virtualenv/bin/activate
```
3. Instalação das dependências
```shell-session
pip install -r requirements.txt
```

## Execução

Para ver este exemplo em funcionamento, rode:

```bash
python3 churn_preprocessing.py
```

Ao final, da execução, você notará os 4 arquivos gerados entre bases de treinamento e teste e variáveis alvo (`churned`) correspondentes.
