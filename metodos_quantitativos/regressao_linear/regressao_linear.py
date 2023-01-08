import pandas as pd                     # Requer instalacao (via 'pip install wheel' e 'pip install pandas')
import matplotlib.pyplot as plt         # Requer instalacao (via 'pip install matplotlib')
from sklearn import linear_model        # Requer instalacao (via 'pip install scikit-learn')
from csv import DictReader
from os import path

##
#
#   Definicoes iniciais (caminho de arquivos raíz, encoding de caracteres no console)
#
##

# Aplicar conforme necessário

# pathBase = path.dirname( __file__ )
pathBase = path.dirname( "c:\\Users\\ivo_a\\Documents\\EACH\\2022-2\\MQA\\TrabalhoFinal\\metodos_quantitativos\\regressao_linear\\regressao_linear.py" )
# sys.stdout = io.TextIOWrapper( sys.stdout.buffer,encoding='utf8' )

##
#
#   Obtenção dos modelos
#
##

anoOuTotal = "2010"
nomeDoArquivoDeInstituicoes = "Publicacoes_Instituicoes_" + anoOuTotal + ".tsv"
nomeDoArquivoDeIndicadores = "Indicadores_Socioeconomicos_" + anoOuTotal + ".tsv"

filepath = path.abspath( path.join(pathBase, "..", "..", "dados", "4_final", "instituicoes", nomeDoArquivoDeInstituicoes))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaInstituicoes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "..", "dados", "4_final", "regioes", "mesorregioes", nomeDoArquivoDeIndicadores))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIndicadoresMesorregioes = list(dictReader)

##
#
#   Regressão Linear
#
##

#   Calculo da produção acadêmica em cada região

for mesorregiao in listaIndicadoresMesorregioes :
    mesorregiao["Publicacoes"] = 0

for instituicao in listaInstituicoes :
    idMesorregiao = int(instituicao["ID_da_mesoregiao"])
    for mesorregiao in listaIndicadoresMesorregioes :
        if idMesorregiao == int(mesorregiao["ID_da_mesoregiao"]) :
            mesorregiao["Publicacoes"] += int(instituicao["Total_Publicacoes"])
            break


listaIndicadoresMesorregioesRanqueada = sorted(
    listaIndicadoresMesorregioes, key=lambda d: d["Publicacoes"], reverse=True
)

#   Regressao Linear

#   + Publicações sobre o valor do PIB

dataframeMesorregioes = pd.DataFrame(listaIndicadoresMesorregioesRanqueada)
dataframeMesorregioes['PIB'] = pd.to_numeric(dataframeMesorregioes['PIB'])
dataframeMesorregioes['Publicacoes'] = pd.to_numeric(dataframeMesorregioes['Publicacoes'])

regressao = linear_model.LinearRegression()

regressao.fit( 
    dataframeMesorregioes[["Publicacoes"]], 
    dataframeMesorregioes.PIB
)

plt.scatter( dataframeMesorregioes.Publicacoes, dataframeMesorregioes.PIB )
plt.xlabel( "Publicações" )
plt.ylabel( "PIB" )
plt.plot( dataframeMesorregioes.Publicacoes, regressao.predict(dataframeMesorregioes[["Publicacoes"]]), color="red")

plt.scatter( dataframeMesorregioes.Publicacoes, dataframeMesorregioes.PIB )
plt.plot( dataframeMesorregioes.Publicacoes, regressao.predict(dataframeMesorregioes[["Publicacoes"]]), color="red")
plt.xlabel( "Publicações" )
plt.ylabel( "PIB" )
plt.xlim([0,1000])
plt.ylim([0,(2*(10**8))])

#   + Publicações sobre o valor do PIB per capita

dataframeMesorregioes = pd.DataFrame(listaIndicadoresMesorregioesRanqueada)
dataframeMesorregioes['PIB_per_capita'] = pd.to_numeric(dataframeMesorregioes['PIB_per_capita'])
dataframeMesorregioes['Publicacoes'] = pd.to_numeric(dataframeMesorregioes['Publicacoes'])

regressao = linear_model.LinearRegression()

regressao.fit( 
    dataframeMesorregioes[["Publicacoes"]], 
    dataframeMesorregioes.PIB_per_capita
)

plt.scatter( dataframeMesorregioes.Publicacoes, dataframeMesorregioes.PIB_per_capita )
plt.xlabel( "Publicações" )
plt.ylabel( "PIB_per_capita" )
plt.plot( dataframeMesorregioes.Publicacoes, regressao.predict(dataframeMesorregioes[["Publicacoes"]]), color="red")

#   + Publicações sobre o valor da população

dataframeMesorregioes = pd.DataFrame(listaIndicadoresMesorregioesRanqueada)
dataframeMesorregioes['Populacao'] = pd.to_numeric(dataframeMesorregioes['Populacao'])
dataframeMesorregioes['Publicacoes'] = pd.to_numeric(dataframeMesorregioes['Publicacoes'])

regressao = linear_model.LinearRegression()

regressao.fit( 
    dataframeMesorregioes[["Publicacoes"]], 
    dataframeMesorregioes.Populacao
)

plt.scatter( dataframeMesorregioes.Publicacoes, dataframeMesorregioes.Populacao )
plt.xlabel( "Publicações" )
plt.ylabel( "Populacao" )
plt.plot( dataframeMesorregioes.Publicacoes, regressao.predict(dataframeMesorregioes[["Publicacoes"]]), color="red")