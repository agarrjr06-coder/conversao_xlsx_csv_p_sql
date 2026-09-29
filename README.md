# Conversão de Excel para CSV

Projeto em Python para automatizar a conversão de planilhas Excel (`.xlsx`) em arquivos CSV prontos para uso em fluxos de dados, ferramentas de BI ou posterior importação em bancos relacionais.

## Objetivo

Reduzir o trabalho manual em rotinas recorrentes de preparação de dados, padronizando a geração de arquivos CSV a partir de planilhas Excel.

O projeto foi inspirado em uma necessidade operacional real: atualizar uma base em Excel e gerar uma versão CSV com nome fixo, adequada para ser consumida por outras etapas do processo.

## O que o script faz

- lê um arquivo `.xlsx` com Pandas;
- permite informar arquivo de entrada e pasta de saída;
- cria automaticamente a pasta de destino quando necessário;
- converte a planilha para CSV sem incluir o índice do DataFrame;
- utiliza codificação `utf-8-sig`, facilitando a abertura no Excel;
- permite substituir automaticamente um arquivo CSV já existente;
- informa quantidade de linhas processadas e tempo de execução.

## Tecnologias

- Python
- Pandas
- OpenPyXL
- Pathlib

## Estrutura do projeto

```text
conversao_xlsx_csv_p_sql/
├── src/
│   └── excel_to_csv.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Como executar

1. Clone o repositório.
2. Crie e ative um ambiente virtual, se desejar.
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute informando o arquivo Excel e a pasta de saída:

```bash
python src/excel_to_csv.py "data/input/base.xlsx" "data/output"
```

Opcionalmente, você pode definir o nome do CSV:

```bash
python src/excel_to_csv.py "data/input/base.xlsx" "data/output" --output-name faturamento_atualizado.csv
```

## Exemplo de fluxo

```text
Excel (.xlsx)
     ↓
Leitura com Pandas / OpenPyXL
     ↓
DataFrame
     ↓
Conversão e padronização
     ↓
CSV UTF-8
     ↓
BI / ETL / carga posterior em banco de dados
```

## Observação

Este repositório cobre a etapa de **Excel → CSV**. A carga em banco de dados não é executada por este script; o CSV gerado pode ser utilizado posteriormente em processos de importação para MySQL, PostgreSQL ou outras plataformas.

## Aprendizados aplicados

- automação de tarefas repetitivas;
- leitura e escrita de arquivos com Pandas;
- organização de projeto Python;
- parametrização de caminhos;
- preparação de dados para etapas posteriores de ETL e análise.
