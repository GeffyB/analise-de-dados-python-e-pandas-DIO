"""
----------------------------------------------------------------------------
Aula/Projeto Analise de Dados com Python e Pandas - Geração Tech - Unimed-BH
      ------------------------------------------------------------
        Projeto 3/3 - Manipulação de Dados de vendas de Produtos
----------------------------------------------------------------------------
___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

A planilha AdventureWorks é um DataBase com informações diversas de vendas e produtos, tais como data, quantidade, tipo do produto, preço, dentre outras.
A tarefa desse projeto/aula é manipular esses dados e, com isso, realizar uma analise exploratória dos mesmo.
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


# Importando as bibliotecas:
from tkinter import dialog
from turtle import title
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")                        # Definindo o estilo que vai ser usado nos gráficos
pd.set_option('float_format', '{:20.2f}'.format)     # Configurando o formato de exibição dos números para evitar que sejam em notação científica

# Criando o DataFrame | Caminho do arquivo local na máquina:
df = pd.read_excel("C:\\Users\\GeffDesk\\Documents\\Bootcamp Geração Tech Unimed BH - Ciência de Dados\\Python - Códigos apresentados em aula\\Analise_de_dados_com_Python_Pandas\\AnaliseExploratoria\\AdventureWorks.xlsx")

#Visualizando as 5 primeiras linhas:
print(df.head())

# QUantidade de linhas e colunas:
print(df.shape)

# Verificando os tipos e dados:
print(df.dtypes)

# Qual a receita total?:
print(df["Valor Venda"].sum())

# Qual o custo total?:
df["Custo"] = df["Custo Unitário"].mul(df["Quantidade"])        # Criando a coluna de custo com o formato Custo unitário * Quantidade
print(df.head(1))                                               # Imprimindo para verificar a criação da coluna Custo

# Qual o custo total geral?:
round(df["Custo"].sum(), 2)                                     # round arredonda as casas decimais, nesse caso, em 2 casas
print(round(df["Custo"].sum(), 2))                              # Imprimindo para verificar o Custo total geral

# Agora com receita e custo total, pode-se encontrar o lucro total
# Criando uma nova coluna com o lucro, que é dado por receita - custo:
df["Lucro"] = df["Valor Venda"] - df["Custo"]
print(df.head(1))

# Total Lucro:
round(df["Lucro"].sum(), 2)
print(round(df["Lucro"].sum(), 2))

# Criando uma coluna com total de dias para enviar o produto:
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]
print(df.head(1))

# Extraindo apenas os dias:
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days   # Removendo o tipo string/object dos dados obtidos na coluna tempo_envio para poder operar matemáticamente
print(df.head(1))

# Verificando o tipo de dado na coluna tempo_envio:
print(df["Tempo_envio"].dtype)

# Média do tempo de envio por Marca:
df.groupby("Marca")["Tempo_envio"].mean()
print(df.groupby("Marca")["Tempo_envio"].mean())        # Agrupa os dados por marca e traz os dados de Tempo de envio para obter a média entre eles

# Verificando se há dados faltantes
df.isnull().sum()                                       # Como se verifica se há dados ausente 
print(df.isnull().sum())                                # Imprimindo para visualização

# Agrupando por ano e marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum()      # O argumento .dt.year pegará so o ano da data da venda, sendo assim, não é preciso criar um coluna so com ano

print(df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum())

# Resetando o indes
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index
print(lucro_ano)

# Qual o total de produtos vendidos?:
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending = False)            # Agrupando por produto, pegando a coluna quantidade e somando. Exibindo de forma decrescente
print(df.groupby("Produto")["Quantidade"].sum().sort_values(ascending = False))

# Gráfico Total de produtos vendidos:
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending = True).plot.barh(title = "Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto")
plt.show()              # Removendo os () enquanto faço alteração no código para nao mostrar os graficos sempre que compilar (Pode tb so mudar p False[Vide documenação])


df.groupby(df["Data Venda"].dt.year)["Lucro"].sum().plot.bar(title = "Lucro X Ano")
plt.xlabel("Ano")
plt.ylabel("Receita")
plt.show()

df.groupby(df["Data Venda"].dt.year)["Lucro"].sum()
print(df.groupby(df["Data Venda"].dt.year)["Lucro"].sum())

# Selecionando apenas as vendas de 2009:
df_2009 = df[df["Data Venda"].dt.year == 2009]          # Criando uma variável e atribuindo a ela o valor/dados contidos em Data venda no ano 2009 no df
print(df_2009.head(5))

# Printando um gráfico do Lucro X Mês dessa vendas:
df_2009.groupby(df_2009["Data Venda"].dt.month)["Lucro"].sum().plot(title = "Lucro X Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro")
plt.show()

# Printando um gráfico do Lucro X Marca dessa vendas:
df_2009.groupby("Marca")["Lucro"].sum().plot.bar(title = "Lucro X Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation = "horizontal")                     # Rotação do eixo x como horizontal (Coloca os nomes na legenda dos dados do gráfico na posição horizontal)
plt.show()

# Printando um gráfico do Lucro X Classe dessa vendas:
df_2009.groupby("Classe")["Lucro"].sum().plot.bar(title = "Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation = "horizontal")                     # Rotação do eixo x como horizontal (Coloca os nomes na legenda dos dados do gráfico na posição horizontal)
plt.show()

# Analises estatisticas
df["Tempo_envio"].describe()
print(df["Tempo_envio"].describe())                     

"""
Leitura dos dados: 
count: quantidade de colunas
mean: média
std: desvio padrão
min: valor mínimo
max:valor máximo
Porcentagens: Quarto (25%); mediana (50%); (75%)
"""

# Gráfico de Boxplot | Mostra essa infos acima das analises estatisticas, nesse caso, em relação ao tempo de envio:
plt.boxplot(df["Tempo_envio"])
plt.show()

# Histograma:
plt.hist(df["Tempo_envio"])
plt.show()

# Tempo mínimo de envio:
df["Tempo_envio"].min()
print(df["Tempo_envio"].min())

# Tempo máximo de envio:
df["Tempo_envio"].max()
print(df["Tempo_envio"].max())

# Identificando o Outlier | Otlier: é aquele dado dicrepante que aparece fora do bloco no boxplot
df[df["Tempo_envio"] == 20]                             # 20 é o número de dias indicado no boxplot pra esse dado
print(df[df["Tempo_envio"] == 20])

# Salvando os nossos dados numa planilha (Uma vez que adicionamos colunas com dados, o arquivo tem mais infos que a planilha original)
df.to_csv("df_vendas_novo.csv", index = False)          # Pode ser salvo em outros formatos (Vide documentação), o status False no index é para não levar o index da base do arquivo

