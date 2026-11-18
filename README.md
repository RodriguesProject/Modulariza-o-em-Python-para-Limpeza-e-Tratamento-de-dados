# Limpeza e Tratamento de Dados com Python

Projeto demonstrativo de preparação de dados cadastrais e organização de um fluxo reutilizável de limpeza com Python. O trabalho parte de arquivos de exemplo com inconsistências de formatação e transforma regras aplicadas manualmente em funções reutilizáveis, reunidas em um módulo.

> **Objetivo do projeto:** demonstrar fundamentos de qualidade de dados, funções, modularização e geração de indicadores simples para apoiar a conferência de cadastros.

## Problema abordado

Bases operacionais podem reunir informações digitadas em formatos diferentes ou incompletos. Neste projeto, os arquivos de exemplo apresentam situações como:

- telefones com pontuação, espaços, código do país ou texto indicativo de ausência;
- CPFs com e sem pontuação;
- e-mails com espaços excedentes ou estrutura incompleta;
- datas registradas em formatos diferentes.

Sem padronização, essas variações dificultam filtros, validações e o uso posterior dos dados.

## Metodologia

O notebook documenta o desenvolvimento em etapas:

1. **Leitura e diagnóstico:** carregamento dos arquivos CSV e inspeção de dimensões, tipos de dados e valores ausentes.
2. **Preservação dos dados originais:** criação de colunas tratadas, mantendo os campos de origem para comparação.
3. **Padronização:** remoção de caracteres não numéricos de telefone e CPF e retirada de espaços excedentes dos e-mails.
4. **Validação básica:** verificação simplificada da estrutura dos e-mails e da quantidade de dígitos dos telefones e CPFs.
5. **Modularização:** organização das regras em funções reutilizáveis no módulo `limpeza.py`.
6. **Relatório e exportação:** geração de indicadores de conferência e gravação da base tratada em CSV e do resumo em JSON.

## Tecnologias e conceitos

- Python
- Pandas
- Expressões regulares (`re`)
- Funções, parâmetros e retornos
- Módulos e importação de código
- Leitura e gravação de CSV e JSON
- Google Colab / Jupyter Notebook

## Resultados observados no conjunto de exemplo

A execução documentada no notebook analisou **8 registros de clientes** e produziu os seguintes indicadores:

| Indicador | Resultado |
|---|---:|
| Cadastros analisados | 8 |
| E-mails aprovados na verificação simplificada de formato | 6 |
| Telefones aprovados na regra de tamanho (10 ou 11 dígitos) | 6 |
| CPFs com 11 dígitos após a limpeza | 8 |

Esses números descrevem somente os arquivos de exemplo deste repositório. Não representam desempenho de produção nem validação cadastral oficial.

## Regras e limitações importantes

As verificações são intencionalmente introdutórias e não substituem validações completas:

- **E-mail:** a expressão regular verifica um padrão estrutural simples; não confirma existência, titularidade ou recebimento da caixa postal.
- **Telefone:** a regra registrada no notebook considera válidos números com 10 ou 11 dígitos. Um número com código internacional pode ser sinalizado para revisão, mesmo contendo um telefone utilizável.
- **CPF:** a implementação verifica a presença de 11 dígitos após a remoção da pontuação; não calcula os dígitos verificadores nem confirma a validade do documento.
- **Dados ausentes ou inválidos:** o objetivo é sinalizar situações para análise, não inventar ou completar informações.

## Estrutura do repositório

- `Aula_Limpeza_de_dados_Funcoes_reutilzaveis_(1) (2).ipynb` — notebook com diagnóstico, desenvolvimento das funções, modularização e execução do fluxo.
- `limpeza.py` — funções reutilizáveis de limpeza e validação básica.
- `clientes_sujos.csv` — conjunto de exemplo para tratamento cadastral.
- `pedidos_loja.csv`, `pedidos_loja.json`, `pedidos_loja.xlsx` — arquivos de exemplo utilizados na atividade.

## Como executar

1. Clone ou baixe este repositório.
2. Instale as dependências:

   ```bash
   pip install pandas
   ```

3. Abra o notebook no Google Colab ou em um ambiente Jupyter.
4. Para utilizar o módulo em outro script Python, mantenha `limpeza.py` no mesmo diretório e importe as funções:

   ```python
   import pandas as pd
   from limpeza import tratar_clientes

   clientes = pd.read_csv(
       "clientes_sujos.csv",
       dtype={
           "telefone": "string",
           "cpf": "string",
           "email": "string"
       }
   )

   clientes_tratados = tratar_clientes(clientes)
   print(clientes_tratados.head())
   ```

## Possíveis evoluções

- adicionar testes automatizados para cada regra;
- validar CPF pelos dígitos verificadores;
- normalizar telefones nacionais e internacionais com regras explícitas;
- registrar erros e exceções em relatório de qualidade;
- separar leitura, transformação, relatório e exportação em módulos próprios;
- ampliar a validação de datas e campos obrigatórios.

## Escopo e transparência

Este é um projeto de aprendizagem aplicada e demonstração técnica. Os resultados apresentados correspondem à execução registrada no notebook e aos arquivos de exemplo. As validações são básicas e não devem ser utilizadas isoladamente em processos cadastrais reais.

---

**Foco do portfólio:** Data Preparation · Data Quality · Python · Pandas · Process Automation
