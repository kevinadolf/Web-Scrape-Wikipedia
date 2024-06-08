### Descrições

**Português:**
Este script realiza um Web Scraping em uma página da Wikipedia que lista as maiores empresas dos Estados Unidos por receita. Utilizando as bibliotecas `BeautifulSoup` e `requests`, o script acessa a página, extrai a tabela com as informações das empresas e organiza os dados em um DataFrame do `pandas`. O resultado pode ser salvo em um arquivo CSV para análise posterior.

**Inglês:**
This script performs Web Scraping on a Wikipedia page that lists the largest companies in the United States by revenue. Using the `BeautifulSoup` and `requests` libraries, the script accesses the page, extracts the table with company information, and organizes the data into a `pandas` DataFrame. The result can be saved to a CSV file for further analysis.

### README

**Português:**

# Web Scraping de Maiores Empresas dos EUA por Receita

Este projeto contém um script em Python que realiza Web Scraping em uma página da Wikipedia para obter uma lista das maiores empresas dos Estados Unidos por receita.

## Requisitos

- Python 3.x
- Bibliotecas: `beautifulsoup4`, `requests`, `pandas`

Você pode instalar as bibliotecas necessárias usando pip:

```bash
pip install beautifulsoup4 requests pandas
```

## Como Usar

1. Clone este repositório para sua máquina local.
2. Execute o script `web_scrape.py`.

O script irá acessar a página da Wikipedia, extrair a tabela com as informações das empresas e salvar os dados em um DataFrame do pandas.

## Exemplo de Saída

A saída do script será um DataFrame com as seguintes colunas:

- Rank
- Name
- Industry
- Revenue (USD millions)
- Profit (USD millions)
- Employees
- Headquarters

## Salvando os Dados

Você pode salvar os dados extraídos em um arquivo CSV descomentando a linha correspondente no script:

```python
df.to_csv('maiores_empresas_eua.csv', index=False)
```

## Contribuição

Sinta-se à vontade para fazer um fork deste repositório e enviar pull requests. Feedbacks e sugestões são bem-vindos!

**Inglês:**

# Web Scraping Largest US Companies by Revenue

This project contains a Python script that performs Web Scraping on a Wikipedia page to obtain a list of the largest companies in the United States by revenue.

## Requirements

- Python 3.x
- Libraries: `beautifulsoup4`, `requests`, `pandas`

You can install the required libraries using pip:

```bash
pip install beautifulsoup4 requests pandas
```

## How to Use

1. Clone this repository to your local machine.
2. Run the `web_scrape.py` script.

The script will access the Wikipedia page, extract the table with company information, and save the data into a pandas DataFrame.

## Example Output

The script's output will be a DataFrame with the following columns:

- Rank
- Name
- Industry
- Revenue (USD millions)
- Profit (USD millions)
- Employees
- Headquarters

## Saving the Data

You can save the extracted data to a CSV file by uncommenting the corresponding line in the script:

```python
df.to_csv('largest_us_companies.csv', index=False)
```

## Contribution

Feel free to fork this repository and submit pull requests. Feedback and suggestions are welcome!
