import numpy as np                  # Requer instalacao (via 'pip install numpy')
import pandas as pd                 # Requer instalacao (via 'pip install wheel' e 'pip install pandas')
import statsmodels.api as sm        # Requer instalacao (via 'pip install statsmodel')
import matplotlib.pyplot as plt     # Requer instalacao (via 'pip install matplotlib')
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from csv import DictReader
from os import path

##
#
#   Definicoes iniciais (caminho de arquivos raíz, encoding de caracteres no console)
#
##

# Aplicar conforme necessário

# pathBase = path.dirname( __file__ )
pathBase = path.dirname( "c:\\Users\\ivo_a\\Documents\\EACH\\2022-2\\MQA\\TrabalhoFinal\\metodos_quantitativos\\ANOVA\\anova.py" )
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
#   Análise de Variância (ANOVA)
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

publicacoes = []
for microrregiao in listaIndicadoresMicrorregioesRanqueada :
    publicacoes.append( microrregiao["Publicacoes"] )

desvio = np.std( publicacoes )
media = np.mean( publicacoes )

for microrregiao in listaIndicadoresMicrorregioesRanqueada :

    publicacoes = microrregiao["Publicacoes"]
    
    if publicacoes < ( media ) :
        microrregiao["Nivel_de_publicacao_academico"] = "BAIXO"
    elif publicacoes < ( media + ( 0.5 * desvio ) ) :
        microrregiao["Nivel_de_publicacao_academico"] = "MEDIO"
    elif publicacoes < ( media + desvio ) :
        microrregiao["Nivel_de_publicacao_academico"] = "ALTO"
    elif publicacoes >= ( media + desvio ) :
        microrregiao["Nivel_de_publicacao_academico"] = "ALTISSIMO"

#   Aplicacao de ANOVA

dataframeMicrorregioes = pd.DataFrame(listaIndicadoresMicrorregioesRanqueada)
dataframeMicrorregioes['PIB'] = pd.to_numeric(dataframeMicrorregioes['PIB'])

model = ols('PIB ~ Nivel_de_publicacao_academico',
            data = dataframeMicrorregioes).fit()
                
anova_result = sm.stats.anova_lm(model, type=2)

# print (anova_result)

tukey = pairwise_tukeyhsd(endog=dataframeMicrorregioes["PIB"], 
                          groups=dataframeMicrorregioes["Nivel_de_publicacao_academico"], 
                          alpha=0.05) 

tukey.plot_simultaneous()
plt.vlines(x=49.57,ymin=-0.5,ymax=4.5, color="red")

tukey.summary()