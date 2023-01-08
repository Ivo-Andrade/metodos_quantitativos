import pandas as pd                                     # Requer instalacao (via 'pip install wheel' e 'pip install pandas')
import matplotlib.pyplot as plt                         # Requer instalacao (via 'pip install seaborn')
import seaborn as sns                                   # Requer instalacao (via 'pip install matplotlib')
from sklearn import preprocessing                       # Requer instalacao (via 'pip install scikit-learn')
from sklearn.preprocessing import StandardScaler        # Requer instalacao (via 'pip install scikit-learn')
from sklearn.decomposition import PCA                   # Requer instalacao (via 'pip install scikit-learn')
from factor_analyzer import FactorAnalyzer              # Requer instalacao (via 'pip install factor_analyzer')
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

anoOuTotal = "2015"
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

indicadoresMicrorregioes = pd.read_csv(
    filepath_or_buffer= listaIndicadoresMicrorregioes,
    delimiter='\t'
)

##
#
#   Análise Fatorial
#
##

scale_indicadores = preprocessing.scale(
    X = listaIndicadoresMicrorregioes
)

scale_indicadores = pd.DataFrame(
    data = scale_indicadores
)

scale_indicadores.corr()

sns.heatmap(
    data = scale_indicadores.corr(),
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20,220,n=200),
    square=True
)