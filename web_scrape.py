#importando bibliotecas

from bs4 import BeautifulSoup
import requests
import pandas as pd

#conectando ao site

URL = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(URL)

#pegando o conteúdo da pagina
soup = BeautifulSoup(page.text, 'html.parser')

#pegando a segunda aparição de <table><table> tabelas
table = soup.find_all('table')[1]

#pegando todas as th-tags da tabelas, ou seja, os titulos
world_titles = table.find_all('th')   

#looping a tabela para pegar somente o texto dos titulos (sem os <th>)
world_table_titles = [title.text.strip() for title in world_titles]

#transformando a lista em colunas de um DataFrame
df = pd.DataFrame(columns= world_table_titles)

#pegando as informações
column_data = table.find_all('tr')

#a primeira lista é vazia, entao desconsideramos ela
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    #para cada iteração, o tamanho da lista aumenta, e como a indexação de listas é [tamanho-1], usar o length(df) direto da certo
    length = len(df)
    df.loc[length] = individual_row_data

print(df)
#salvando Excel, por exemplo
#df.to_csv(Path, index= False)