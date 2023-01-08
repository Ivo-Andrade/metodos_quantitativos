import random
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

anoOuTotal = "Total"
nomeDoArquivoDeInstituicoes = "Publicacoes_Instituicoes_" + anoOuTotal + ".tsv"
nomeDoArquivoDeIndicadores = "Indicadores_Socioeconomicos_" + anoOuTotal + ".tsv"

filepath = path.abspath( path.join(pathBase, "..", "..", "dados", "4_final", "instituicoes", nomeDoArquivoDeInstituicoes))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaInstituicoes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "..", "dados", "4_final", "regioes", "microrregioes", nomeDoArquivoDeIndicadores))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIndicadoresMicrorregioes = list(dictReader)

##
#
#   Regressão Linear
#
##

#   Calculo da produção acadêmica em cada região

for microrregiao in listaIndicadoresMicrorregioes :
    microrregiao["Publicacoes"] = 0

for instituicao in listaInstituicoes :
    idMicrorregiao = int(instituicao["ID_da_microregiao"])
    for microrregiao in listaIndicadoresMicrorregioes :
        if idMicrorregiao == int(microrregiao["ID_da_microregiao"]) :
            microrregiao["Publicacoes"] += int(instituicao["Total_Publicacoes"])
            break


listaIndicadoresMicrorregioesRanqueada = sorted(
    listaIndicadoresMicrorregioes, key=lambda d: d["Publicacoes"], reverse=True
)

#   Regressao Linear

#   + Publicações, população e total de estabelecimentos, sobre o PIB per capita

dataframeMicrorregioes = pd.DataFrame(listaIndicadoresMicrorregioesRanqueada)
dataframeMicrorregioes['PIB_per_capita'] = pd.to_numeric(dataframeMicrorregioes['PIB_per_capita'])
dataframeMicrorregioes['Publicacoes'] = pd.to_numeric(dataframeMicrorregioes['Publicacoes'])
dataframeMicrorregioes['Populacao'] = pd.to_numeric(dataframeMicrorregioes['Populacao'])
dataframeMicrorregioes['Total_de_estabelecimentos'] = pd.to_numeric(dataframeMicrorregioes['Total_de_estabelecimentos'])

regressao = linear_model.LinearRegression()

regressao.fit( 
    dataframeMicrorregioes[["Publicacoes", "Populacao", "Total_de_estabelecimentos"]], 
    dataframeMicrorregioes.PIB_per_capita
)

coeficiente = regressao.coef_
intercepto = regressao.intercept_

# print( 
#     "Coeficientes: {} (Publicacoes), {} (Populacao), {} (Total_de_estabelecimentos)"
#     .format(
#         coeficiente[0],
#         coeficiente[1],
#         coeficiente[2]
#     )
# )
# print("Intercepto: {}".format(intercepto))

for i in range(10) :
    indiceAleatorio = random.randrange( len(listaIndicadoresMicrorregioesRanqueada) )
    microrregiao = listaIndicadoresMicrorregioesRanqueada[indiceAleatorio]

    nomeMicrorregiao = microrregiao["nome_da_microrregiao"]

    publicacoes = float(microrregiao["Publicacoes"])
    populacao = float(microrregiao["Populacao"])
    totalEstabelecimentos = float(microrregiao["Total_de_estabelecimentos"])

    estimativaPIBperCapita = (
        coeficiente[0] * publicacoes
        + coeficiente[1] * populacao
        + coeficiente[2] * totalEstabelecimentos
        + intercepto
    )

    pibPerCapita = microrregiao["PIB_per_capita"]

    print( "------------")
    print( "Microrregião: {}".format(nomeMicrorregiao))
    print( "Valor estimado: {}".format(estimativaPIBperCapita) )
    print( "Valor real: {}".format(pibPerCapita) )
