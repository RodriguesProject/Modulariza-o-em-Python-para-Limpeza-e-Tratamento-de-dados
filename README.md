# Limpeza, Padronização e Modularização de Dados com Python

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Biblioteca-Pandas-150458)](https://pandas.pydata.org/)
[![Data Quality](https://img.shields.io/badge/Focus-Data%20Quality-brightgreen)](https://github.com/RodriguesProject)

Projeto demonstrativo de **preparação de dados cadastrais e modularização de rotinas de limpeza**. A atividade transforma operações inicialmente realizadas no notebook em funções reutilizáveis reunidas no módulo `limpeza.py`, com geração de indicadores simples para apoiar a conferência de cadastros.

> **Em uma frase:** organizar regras repetitivas de limpeza em um módulo Python reutilizável, preservando os dados originais e sinalizando registros que precisam de revisão.

## 1. Contexto e problema

Dados cadastrais podem ser digitados em formatos diferentes, conter espaços excedentes, caracteres de formatação ou informações incompletas. Essas variações dificultam filtros, cruzamentos e etapas posteriores de análise.

O conjunto de exemplo deste projeto contém situações como:

- telefones com espaços, parênteses, hífens e código internacional;
- CPFs com e sem pontuação;
- e-mails com espaços excedentes ou estrutura incompleta;
- valores textuais que indicam ausência de telefone.

O desafio foi criar um fluxo simples e reaproveitável para normalizar a representação dos campos e gerar indicadores de conferência, sem alterar silenciosamente os valores de origem ou declarar válidos dados que passaram apenas por uma verificação superficial.

## 2. Objetivo e escopo

O projeto demonstra como:

- inspecionar um conjunto pequeno de dados cadastrais;
- padronizar a representação de telefone, CPF e e-mail;
- preservar as colunas originais e criar colunas tratadas;
- aplicar verificações estruturais introdutórias;
- organizar as regras em funções e em um módulo Python;
- produzir um resumo em formato de dicionário e exportá-lo como JSON;
- exportar a base tratada em CSV.

O escopo é didático e demonstrativo. Não é um sistema de cadastro, serviço de validação oficial ou solução pronta para uso em produção.

## 3. Metodologia e fluxo de tratamento

O fluxo registrado no notebook segue estas etapas:

1. **Leitura:** carregamento do CSV com Pandas, mantendo telefone, CPF e e-mail como texto para evitar perda de zeros à esquerda.
2. **Diagnóstico:** inspeção das dimensões, tipos de dados e valores ausentes.
3. **Preservação:** cópia do DataFrame e criação de novas colunas normalizadas, sem sobrescrever os campos de origem.
4. **Limpeza de caracteres:** uso de expressão regular para manter somente dígitos em telefone e CPF.
5. **Padronização de e-mail:** remoção de espaços excedentes nas extremidades e verificação de um padrão estrutural simples.
6. **Verificações básicas:** sinalização de telefones com 10 ou 11 dígitos e CPFs com 11 dígitos após a limpeza.
7. **Modularização:** organização das funções em `limpeza.py`, para permitir importação e reutilização em outros scripts.
8. **Relatório e exportação:** consolidação dos indicadores e gravação dos resultados em CSV e JSON.

### Fluxo lógico

```text
clientes_sujos.csv
       |
       v
leitura com Pandas
       |
       v
tratar_clientes()  [limpeza.py]
       |
       +--> colunas normalizadas e indicadores
       |
       v
gerar_relatorio_clientes()
       |
       +--> clientes_tratados.csv
       |
       +--> relatorio_clientes.json
```

## 4. Tecnologias e conceitos

- **Python**
- **Pandas** — leitura, transformação e manipulação tabular
- **re (expressões regulares)** — remoção de caracteres não numéricos e verificação estrutural de e-mail
- Funções, parâmetros, retornos e reutilização de código
- Módulos e importação de funções
- CSV e JSON
- Google Colab / Jupyter Notebook

## 5. Estrutura do repositório

| Arquivo | Finalidade |
|---|---|
| `limpeza.py` | Funções reutilizáveis de limpeza, verificação e geração de resumo |
| `clientes_sujos.csv` | Base cadastral de exemplo com 8 registros |
| `Aula_Limpeza_de_dados_Funcoes_reutilzaveis_(1) (2).ipynb` | Notebook de diagnóstico, desenvolvimento, modularização e execução do fluxo |
| `pedidos_loja.csv` | Arquivo complementar da atividade |
| `pedidos_loja.json` | Arquivo complementar da atividade |
| `pedidos_loja.xlsx` | Arquivo complementar da atividade |

Os arquivos de pedidos fazem parte do material complementar da atividade; os indicadores apresentados neste README referem-se especificamente à base `clientes_sujos.csv`.

## 6. Funções disponibilizadas

### `limpar_numero(texto)`

- Retorna somente os caracteres numéricos de um valor.
- Retorna uma string vazia quando o valor é nulo.
- É utilizada para normalizar telefone e CPF, sem validar sua autenticidade.

### `email_valido(email)`

- Aplica uma expressão regular para verificar um padrão estrutural simples.
- Retorna `True` ou `False`.
- Não confirma existência, titularidade ou recebimento da caixa postal.

### `tratar_clientes(df)`

- Cria uma cópia do DataFrame recebido.
- Adiciona colunas normalizadas para telefone, CPF e e-mail.
- Cria indicadores booleanos para as verificações básicas.
- Mantém os campos originais disponíveis para comparação.

### `gerar_relatorio_clientes(df)`

- Resume o total de registros.
- Conta e-mails que passaram pela verificação estrutural.
- Conta telefones com 10 ou 11 dígitos.
- Conta CPFs com 11 dígitos após a limpeza.

## 7. Resultados observados no conjunto de exemplo

A execução registrada no notebook analisou **8 cadastros**.

| Indicador | Resultado | O que significa |
|---|---:|---|
| Cadastros analisados | 8 | Quantidade de linhas processadas |
| E-mails aprovados na verificação simplificada | 6 | Passaram pela expressão regular utilizada |
| Telefones aprovados na regra de tamanho | 6 | Apresentaram 10 ou 11 dígitos após a limpeza |
| CPFs com 11 dígitos após a limpeza | 8 | Atenderam ao critério de comprimento |

Esses resultados demonstram a execução do fluxo sobre os arquivos de exemplo. Não representam taxa de qualidade de uma base real, desempenho em produção ou validação cadastral oficial.

### Exemplos de decisões de tratamento

- Um telefone com código internacional pode resultar em 13 dígitos e não passar pela regra nacional de 10 ou 11 dígitos. Isso sinaliza necessidade de uma regra adicional, não necessariamente um telefone inválido.
- Um campo contendo o texto `sem telefone` resulta em string vazia após a extração de dígitos e deve ser revisado.
- Um CPF com 11 dígitos passa pelo critério de comprimento, mas isso **não comprova** que os dígitos verificadores sejam válidos.
- Um e-mail que passa pela expressão regular pode ainda assim não existir ou não pertencer ao titular informado.

## 8. Como executar

### Requisitos

- Python 3
- Pandas

Instale a dependência:

```bash
pip install pandas
```

### Executar o módulo

Mantenha `limpeza.py` e `clientes_sujos.csv` no mesmo diretório e execute:

```python
import json
import pandas as pd

from limpeza import tratar_clientes, gerar_relatorio_clientes

clientes_brutos = pd.read_csv(
    "clientes_sujos.csv",
    dtype={
        "telefone": "string",
        "cpf": "string",
        "email": "string",
    },
)

clientes_tratados = tratar_clientes(clientes_brutos)
relatorio = gerar_relatorio_clientes(clientes_tratados)

clientes_tratados.to_csv(
    "clientes_tratados_final.csv",
    index=False,
)

with open("relatorio_clientes.json", "w", encoding="utf-8") as arquivo:
    json.dump(relatorio, arquivo, ensure_ascii=False, indent=4)

print(relatorio)
```

O resultado esperado para o conjunto de exemplo versionado é:

```python
{
    "total_clientes": 8,
    "emails_com_formato_ok": 6,
    "telefones_com_tamanho_ok": 6,
    "cpfs_com_11_digitos": 8,
}
```

Os arquivos `clientes_tratados_final.csv` e `relatorio_clientes.json` são gerados localmente durante a execução; não precisam estar previamente presentes no repositório.

## 9. Limitações e cuidados

- **E-mail:** a expressão regular é simplificada e não verifica existência, domínio ativo, titularidade ou entrega de mensagens.
- **Telefone:** a regra de comprimento considera somente 10 ou 11 dígitos. Não normaliza códigos internacionais nem valida números em operadoras.
- **CPF:** a implementação remove pontuação e verifica 11 dígitos; não calcula dígitos verificadores nem confirma autenticidade.
- **Datas:** o notebook apresenta formatos variados em `data_cadastro`, mas o módulo atual não implementa uma rotina de padronização de datas.
- **Dados pessoais:** os arquivos são exemplos didáticos. Não utilizar dados pessoais reais ou sensíveis sem base legal, controles de acesso e medidas de proteção adequadas.
- **Produção:** antes de uso operacional, seriam necessários testes automatizados, regras de negócio formalizadas, tratamento de exceções, logs e validações mais robustas.

## 10. Próximas evoluções

- Adicionar testes automatizados para cada função e casos extremos.
- Implementar validação de CPF pelos dígitos verificadores.
- Normalizar telefones nacionais e internacionais com regras explícitas.
- Padronizar datas com formatos e tratamento de erros documentados.
- Separar leitura, transformação, validação e exportação em módulos específicos.
- Criar relatório detalhado de inconsistências por registro.
- Adicionar documentação de parâmetros, tipos e retornos das funções.

## 11. Escopo do projeto

Projeto de aprendizagem aplicada que demonstra **Data Preparation, Data Quality e modularização com Python** em uma base pequena de exemplo. O valor demonstrado está na organização do fluxo, na reutilização de funções e na distinção entre padronização e validação. Não há alegação de automação implantada em ambiente empresarial ou de impacto operacional mensurado.

---

**Portfolio focus:** Data Preparation · Data Quality · Python · Pandas · Process Automation
