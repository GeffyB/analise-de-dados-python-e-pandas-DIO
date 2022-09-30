"""
----------------------------------------------------------------------------
Aula/Projeto Analise de Dados com Python e Pandas - Geração Tech - Unimed-BH
      ------------------------------------------------------------
            Projeto 1/3 - Manipulação de Dados de População
----------------------------------------------------------------------------
___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

A planilha Gapminder é um DataBase com informações diversas sobre dados de população, contendo infos sobre continentes, países, numero de habitantes, idade, expectativa de vida, PIB, dentre outras.
A tarefa desse projeto/aula é conhecer a biblioteca Pandas em umprimeiro contato, entendendo suas funções e comandos e manipular alguns dados desse DataBase para praticar esse novo aprendizado.
____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

Sobre o código:
O código está Overcommented pela caracteristica do projeto, que é, ter um finalidade didática para conhecer as funcionalidades da Biblioteca.
Por esse mesmo motivo, o código apresenta linhas redundantes seguidas onde a função é exemplificar o comando antes de o printar no terminal
Ex.:
Linha 1: round(df["Custo"].sum(), 2)                                     
Linha 2: print(round(df["Custo"].sum(), 2))

Outro motivo disso acontecer é que o curso foi ministrado usando o Colaboratory com o Jupyter e arquivos .ipynb onde somente com a 'Linha 1' do exemplo o código fornece uma saida e nos arquivos .py, 
que foi como fiz usando o VScode, isso nao é possível sem adicionar o comando print()

O código foi feito dessa forma como um exercício pessoal para aprimorar as habilidade em Phyton!
"""

# Importando a biblioteca Pandas
import pandas as pd

# Parâmetro modificados para resolver erro no .csv | error_bad_lines = False; definindo tipo do separador: sep = ";"
df = pd.read_csv("C:\\Users\\GeffDesk\\Documents\\Bootcamp Geração Tech Unimed BH - Ciência de Dados\\Python - Códigos apresentados em aula\\Analise_de_dados_com_Python_Pandas\\AnaliseGapminder\\Gapminder.csv", error_bad_lines = False, sep = ";" )

# Visualizando as 5 primeiras linhas
print(df.head())

# Renomeando os nomes da planilha em inglês para portugues
df = df.rename(columns = {"country":"Pais", "continent":"Continente", "year":"Ano", "lifeExp":"Expectativa de vida", "pop":"Pop Total", "gdpPercap":"PIB"})
print(df.head())                                        # Sem declarar nada no () em head ele lê as 5 primeiras linhas da planilha

# Total de linhas e colunas | df.shape
print(df.shape)

# Tipos de dados de cada coluna | df.dtypes | object = string
print(df.dtypes)

# Retornar as ultimas linhas da planilha | df.tail | Sem declarar nada no () em tail ele lê as 5 ultimas linhas da planilha
print(df.tail())

# Retorna estatisticas do banco de dados | df.describe
print(df.describe())

# Como fazer um feature dos dados
print(df["Continente"].unique())                        # Lista somente os dados contidos em continente 

Oceania = df.loc[df["Continente"] == "Oceania"]         # Define os dados de Oceania como os valores localizados dentro do conjunto oceania
print(Oceania.head())

print(Oceania["Continente"].unique())

# Agrupamento de dados
print(df.groupby("Continente")["Pais"].nunique())       # Retorna a quantidade de paise por continente

# Qual a expectativa de vida média em cada pais nesses dados?
print(df.groupby("Ano")["Expectativa de vida"].mean())  # .mean define que quer a média desses dados | df["DADO"].mean() -> Retorna média; df["DADO"].sum() -> Retorna a soma





