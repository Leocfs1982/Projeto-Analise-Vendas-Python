# Projeto de Análise de Vendas com Python

## Sobre o projeto

Projeto desenvolvido para praticar os fundamentos de Python por meio da análise de dados fictícios de vendas.

O programa lê dados de um arquivo CSV, calcula indicadores comerciais, organiza os produtos por faturamento e apresenta um relatório no terminal.

## Tecnologias utilizadas

- Python
- CSV para armazenamento dos dados
- Biblioteca padrão `csv`
- Biblioteca padrão `pathlib`
- Visual Studio Code (VS Code)

## Funcionalidades

- Leitura de dados a partir de um arquivo CSV.
- Cálculo do faturamento por produto.
- Cálculo do faturamento total e da quantidade total vendida.
- Identificação dos produtos com maior e menor faturamento.
- Classificação dos produtos por faturamento.
- Cálculo da participação percentual de cada produto no faturamento total.
- Cálculo do faturamento médio por produto.
- Validação de linhas incompletas e valores inválidos.
- Tratamento de situações sem produtos válidos para análise.
- Formatação de valores monetários no padrão brasileiro.

## Resultados da análise

- **Faturamento total:** R$ 6.280,00
- **Quantidade total vendida:** 32 unidades
- **Produto com maior faturamento:** Monitor — R$ 3.000,00
- **Produto com menor faturamento:** Mouse — R$ 280,00
- **Faturamento médio por produto:** R$ 1.046,67

## Estrutura do projeto

- `ler_vendas.py`: código Python responsável pela análise.
- `vendas.csv`: arquivo com os dados utilizados no relatório.
- `vendas_teste.csv`: arquivo auxiliar para testar o tratamento de dados inválidos.
- `README.md`: documentação do projeto.

## Como executar

1. Instale o Python.
2. Baixe ou clone este repositório.
3. Abra a pasta do projeto no VS Code.
4. Execute o arquivo `ler_vendas.py`.

Mantenha os arquivos CSV na mesma pasta do código Python.

## Aprendizados

Durante o desenvolvimento, pratiquei leitura de arquivos CSV, variáveis, funções, estruturas condicionais, laços de repetição, ordenação de dados, cálculos, formatação de valores e tratamento de erros.

Este projeto faz parte do meu portfólio de estudos em Python e Análise de Dados, demonstrando a aplicação prática de conceitos de programação na análise de informações comerciais.