"""
----------------------------------------------------------------------------
Aula/Projeto Analise de Dados com Python e Pandas - Geração Tech - Unimed-BH
      ------------------------------------------------------------
          Projeto 2/3 - Manipulação de Dados de Rede de Lojas
----------------------------------------------------------------------------
___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

As planilhas usadas nesse projeto são um DataBase com informações diversas sobre uma rede de lojas em diversos estados/cidades.
Cada rede de lojas por cidade contem uma serie de informações sobre as vendas, preços, custo de operação, tempo de envio, dentre outras.
A tarefa desse projeto/aula é aplicar os conhecimentos de forma que seja capaz manipular e comparar esses dados entre as diversas lojas.
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

# Importando a biblioteca
import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos arquivos
df1 = pd.read_excel("C:\\Users\\GeffDesk\\Documents\\Bootcamp Geração Tech Unimed BH - Ciência de Dados\\Python - Códigos apresentados em aula\Analise_de_dados_com_Python_Pandas\\AnaliseLojas\\Aracaju.xlsx")   # Se der erro de leitura/carregamento usar engine="openpyxl"
df2 = pd.read_excel("C:\\Users\\GeffDesk\\Documents\\Bootcamp Geração Tech Unimed BH - Ciência de Dados\\Python - Códigos apresentados em aula\Analise_de_dados_com_Python_Pandas\\AnaliseLojas\\Fortaleza.xlsx") # Se der erro de leitura/carregamento usar engine="openpyxl"
df3 = pd.read_excel("C:\\Users\\GeffDesk\\Documents\\Bootcamp Geração Tech Unimed BH - Ciência de Dados\\Python - Códigos apresentados em aula\Analise_de_dados_com_Python_Pandas\\AnaliseLojas\\Natal.xlsx")     # Se der erro de leitura/carregamento usar engine="openpyxl"
df4 = pd.read_excel("C:\\Users\\GeffDesk\\Documents\\Bootcamp Geração Tech Unimed BH - Ciência de Dados\\Python - Códigos apresentados em aula\Analise_de_dados_com_Python_Pandas\\AnaliseLojas\\Recife.xlsx")    # Se der erro de leitura/carregamento usar engine="openpyxl"
df5 = pd.read_excel("C:\\Users\\GeffDesk\\Documents\\Bootcamp Geração Tech Unimed BH - Ciência de Dados\\Python - Códigos apresentados em aula\Analise_de_dados_com_Python_Pandas\\AnaliseLojas\\Salvador.xlsx")  # Se der erro de leitura/carregamento usar engine="openpyxl"

"""
É possível ainda modificar dados da planilha ao carregar indicando parâmetro após o nome do arquivo.
Ex.: sheet name = X, onde X indica a aba que você deseja ler em caso de arquivos com multiabas
     skiprows = None, onde pode-se indicar a partir de qual linha deve começar a leitura do arquivo
É possível acessar todos esse parametros na documentação do pandas
""" 

# Juntando todos os arquivos (colocando um abaixo do outro)
df = pd.concat([df1, df2, df3, df4, df5])

# Exibindo as 5 primeiras linhas e em seguida as 5 ultimas
print(df.head())
print(df.tail())

# Exibindo as 5 primeiras linhas de uma das planilhas em específico, nesse caso a df4
print(df4.head())

# Exibindo uma amostra qualquer com 5 itens desses dados | Como é uma amostra aleatória, cada vez que for compilado gerará dados novos arbitrarios
(print(df.sample(5)))

# Verificando o tipo de dado de cada coluna
print(df.dtypes)                                       # Lembrando que o tipo object é equivalente ao tipo string no Python

# ALterando o tipo de dado de uma coluna | Nesse caso, o item LojaID é um int mas não vai ser feita operações então será convertido em object
df["LojaID"] = df["LojaID"].astype("object")
print(df.dtypes)

# Tratando valores faltantes

# Consultando linhas com valores faltantes
print(df.isnull().sum())

"""
Nas minhas planilhas, não foram reconhecidos valores nulos, esse ultimo print retorna:
--------------------
     Cidade    0
     Data      0
     Vendas    0
     LojaID    0
     Qtde      0
--------------------
Mas, segue alguns exemplos caso alguns desses valores retornem um número, que indica a existencia de linhas com valores nulos/faltantes

"""
# Substituindo pela média | Seguindo o exemplo que Vendas retornou um número diferente de 0, indicando haver linhas nulas
print(df["Vendas"].mean())                                  # Print com comando .mean que retorna a média do valor requerido, nesse caso o valor de Vendas
df["Vendas"].fillna(df["Vendas"].mean(), inplace = True)    # Esse comando basicamente diz para preencher em memória os valores vazios/nulos pela média (mean) dos valores Vendas

# Substituindo os valores nulos por zero
df["Vendas"].fillna(0, inplace = True)                      # Esse comando é semelhante ao de cima, exceto que é passado o valor(0) para o parametro .fillna

# Apagando as linhas com valores nulos
df.dropna(inplace = True)                                   

"""
 Caso exista mais de um dado com valores nulos, é possível indicar qual apagar adicionando o comando:
 subset=["o que quero apagar"], inplace = True | Ex.: df.dropna(subset["Vendas"], inplace = True)
"""

# Removendo linhas que estejam com valores faltantes em todas as colunas
df.dropna(how = "all", inplace = True)

# Criando novas colunas de dados | Nesse exemplo, a coluna receita que será o produto das vendas pela quantidade
df["Receita"] = df["Vendas"].mul(df["Qtde"])                
print(df.head())

#Retornando a maior e menor receita, respectivamente
print(df["Receita"].max())
print(df["Receita"].min())

# Criar um ranking de dados com base em uma coluna | nesse exemplo, top 3 maiores receitas | funciona para as maiores e menores so mudar o .nlargest para .nsmallest
print(df.nlargest(3, "Receita"))
print(df.nsmallest(3, "Receita"))

# Agrupamento por cidade 
print(df.groupby("Cidade")["Receita"].sum())                # Agrupa os dados de cidade somando as receitas

# Ordenando o conjunto de dados
print(df.sort_values("Receita", ascending = False).head(10))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Manipulando dados usando as datas

# Transformando a coluna de data em tipo inteiro (Para simular como transformar em conjunto de data casoa planilha venha como inteiro)
df["Data"] = df["Data"].astype("int64")

# Verificando o tipo de dados de cada coluna
print(df.dtypes)

# Transformando coluna de data em data
df["Data"] = pd.to_datetime(df["Data"])                     # Comando da biblioteca do pandas para converter para datahora
print(df.dtypes)

# Agrupamento por ano
df.groupby(df["Data"].dt.year)["Receita"].sum ()              # Comando que pede agrupas por ano a soma das receitas
print(df.groupby(df["Data"].dt.year)["Receita"].sum())

# Criando uma nova coluna com o ano
df["Ano_Venda"] = df["Data"].dt.year
print(df.sample(5))

# Extraindo o mês e o dia da venda
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)         #Poderia ser feito um linha para cada dado separadamente também
print(df.sample(5))

# Retornando a data mais antiga
df["Data"].min()                                            # Mesmo método min usado anteriormente em outras exibições de valor e receita
print(df["Data"].min())

# Calculando a diferença de dias | Como não ha duas colunas de data, é preciso pegar a data e subtrair da data mínima
df["diferenca_dias"] = df["Data"] - df["Data"].min()
print(df.sample(5))

# Criando uma coluna com trimestre
df["trimestre_venda"] = df["Data"].dt.quarter               # Operando 1/4 da data (.dt.quarter) que para o ano que tem 12 meses ( 12/4 = 3 = trimestre )
print(df.sample(5))

# Filtrando as vendas de 2019 do mÊs de março | Subconjunto de dados
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]
print(vendas_marco_19)
print(vendas_marco_19.sample(20))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Visualização de dados

#Conhecendo o método .value_counts
df["LojaID"].value_counts(ascending = False)                # Mostra quantas linhas existem com dados específicos, nesse exemplo, a saída 1036  117 indica que a loja 1036 aparece em 117 linhas
print(df["LojaID"].value_counts(ascending = False))

# Gráfico de barras
df["LojaID"].value_counts(ascending = False).plot.bar()
plt.show()

# Grafico de barras horizontais
df["LojaID"].value_counts(ascending = False).plot.barh()    # Para mostrar os valores do menor para o maior, troca-se o False por True no ascending
plt.show()                                                  # Para o Jupyter notebook, o grafico sempre vai ter infos x,y acima do grafico; para remover só colocar ; ao final do plotbar()

# Gráfico de pizza | para o agrupamento Data/Receita
df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()
plt.show()

# Total de vendas por cidade
df["Cidade"].value_counts()                                                          # Comando para fazer a conta das vendas por cidade
print(df["Cidade"].value_counts())

# Adicionando um título e alterando o nome dos eixos para criar o gráfico Vendas/Cidade personalizado
df["Cidade"].value_counts().plot.bar(title ="Total de vendas por cidade")
plt.xlabel("Cidade")                                                                 # Adicionando 'valores' ao parametro Rótulo do eixo X
plt.ylabel("Total de Vendas")                                                        # Adicionando 'valores' ao parametro Rótulo do eixo Y
plt.show()

# Alterando a cor
df["Cidade"].value_counts().plot.bar(title ="Total de vendas por cidade", color = "red")
plt.xlabel("Cidade")                                                                 # Adicionando 'valores' ao parametro Rótulo do eixo X
plt.ylabel("Total de Vendas")                                                        # Adicionando 'valores' ao parametro Rótulo do eixo Y
plt.show()

# Alterando estilo do matlabplotlib
plt.style.use("ggplot")                                                              #matplotlib.org há uma lista com o nome e imagem dos estilos pra uso
df.groupby(df["mes_venda"])["Qtde"].sum().plot(title ="Total de vendas por cidade", color = "red")
plt.xlabel("Mês")                                                                 
plt.ylabel("Total de Produtos Vendidos")  
plt.legend()                                        
plt.show()

print(df.groupby(df["mes_venda"])["Qtde"].sum())

# Selecionando apenas as vendas de 2019
df_2019 = df[df["Ano_Venda"] == 2019]
print(df_2019)

# Total de produtos vendidos por mês em 2019
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")               # Marker é o tipo de marcador do gráfico, pode ser alterado vide documentação
plt.xlabel("Mês")                                                                 
plt.ylabel("Total de Produtos Vendidos")  
plt.legend()                                        
plt.show()

# Grafico de Histograma
plt.hist(df["Qtde"], color = "magenta")                                              #matplotlib.org há uma lista com as cores que podem ser usadas
plt.show()

# Plotando um gráfico de inspeção
plt.scatter(x = df_2019["dia_venda"], y = df_2019["Receita"])
plt.show()

# Salvando as imagens dos gráficos em png
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
plt.title("Quantidade de produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total de produtos vendidos")
plt.legend()
plt.savefig("grafico QTDE x MES.png")
plt.show()
