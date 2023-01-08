import io
import sys
from csv import DictReader
from os import path

##
#
#   Definições iniciais (caminho de arquivos raíz, encoding de caracteres no console)
#
##

pathBase = path.dirname( __file__ )
sys.stdout = io.TextIOWrapper( sys.stdout.buffer,encoding='utf8' )

##
#
#   Obtenção dos modelos de dados iniciais
#
##

filepath = path.abspath( path.join(pathBase, "..", "dados", "0_iniciais", "Dados_de_Publicacoes.txt"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaDadosDePublicacoes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "0_iniciais",  "Instituicoes.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaInstituicoes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "0_iniciais",  "Subdisciplinas.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaSubdisciplinas = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "0_iniciais",  "RAIS_N_ESTABELECIMENTOS_2010.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2010 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "0_iniciais",  "RAIS_N_ESTABELECIMENTOS_2011.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2011 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "0_iniciais",  "RAIS_N_ESTABELECIMENTOS_2012.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2012 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "0_iniciais",  "RAIS_N_ESTABELECIMENTOS_2013.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2013 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "0_iniciais",  "RAIS_N_ESTABELECIMENTOS_2014.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2014 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "0_iniciais",  "RAIS_N_ESTABELECIMENTOS_2015.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2015 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "0_iniciais", "PIB_dos_Municípios.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaPIBdosMunicipios = list(dictReader)

##
#
#   Obtenção dos modelos de dados após tratamento de compatibilidade entre índices
#
##

filepath = path.abspath( path.join(pathBase, "..", "dados", "1_compatibilidade_de_dados", "Dados_de_Publicacoes_alterado.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaDadosDePublicacoes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "1_compatibilidade_de_dados",  "Instituicoes_alterado.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaSubdisciplinas = list(dictReader)

# NOTA: Alterar 20XX para ano selecionado (2010-2015), e alterar nome da variavel da lista resultante de forma análoga

anoOuTotal = "20XX"
nomeDoArquivo = "RAIS_N_ESTABELECIMENTOS_" + anoOuTotal + "_ALTERADO.csv"

filepath = path.abspath( path.join(pathBase, "..", "dados", "1_compatibilidade_de_dados", nomeDoArquivo))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos_20XX = list(dictReader)

##
#
#   Obtenção dos modelos de dados após a agregação de dados
#
##

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados",  "Instituicoes_alterado.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaSubdisciplinas = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "QuantificacaoDePublicacoes.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaDadosDePublicacoes = list(dictReader)

# NOTA: Alterar REGAIO para região agregada desejada (microrregioes, mesorregioes, estados) e
#       alterar 20XX para ano desejada (2010-2015), e alterar nome da variavel da lista resultante de forma análoga

regiao = "REGIAO"
anoOuTotal = "20XX"
pasta_regiao = "REGIAO".lower()
nomeDoArquivoDePIB = "PIBde" + regiao.capitalize() + ".tsv"
nomeDoArquivoEstabelecimento = "RAIS_N_ESTABELECIMENTOS_" + anoOuTotal + "_ALTERADO.tsv"

filepath = path.abspath( path.join(pathBase, "..", "dados", "1_compatibilidade_de_dados", pasta_regiao, nomeDoArquivoDePIB))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentos_20XX = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "1_compatibilidade_de_dados", pasta_regiao, nomeDoArquivoEstabelecimento))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentos_20XX = list(dictReader)

##
#
#   Obtenção dos modelos de dados após a filtragem de dados
#
##

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados",  "Instituicoes_filtrado.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaInstituicoes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "QuantificacaoDePublicacoes.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaDadosDePublicacoes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "QuantificacaoDePublicacoesPorInstituicao_Filtrado.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaDadosDePublicacoes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "QuantificacaoDePublicacoesPorInstituicaoEAno_Filtrado.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaDadosDePublicacoes = list(dictReader)

# NOTA: Alterar REGAIO para região agregada desejada (microrregioes, mesorregioes, estados) e
#       alterar 20XX para ano desejada (2010-2015), e alterar nome da variavel da lista resultante de forma análoga
    
anoOuTotal = "20XX"
regiao = "REGIAO"
pasta_regiao = "REGIAO".lower()
nomeDoArquivoDePIB = "PIBde" + regiao.capitalize() + "_filtrado.tsv"
nomeDoArquivoEstabelecimento = "RAIS_N_ESTABELECIMENTOS_" + anoOuTotal + "_FILTRADO.tsv"

filepath = path.abspath( path.join(pathBase, "..", "dados", "1_compatibilidade_de_dados", pasta_regiao, nomeDoArquivoDePIB))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentos_20XX = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "1_compatibilidade_de_dados", pasta_regiao, nomeDoArquivoEstabelecimento))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentos_20XX = list(dictReader)

##
#
#   Obtenção dos modelos de dados finais
#
##

anoOuTotal = "20XX"
regiao = "REGIAO"
pasta_regiao = "REGIAO".lower()
nomeDoArquivoDeInstituicoes = "Publicacoes_Instituicoes_" + anoOuTotal + ".tsv"
nomeDoArquivoDeIndicadores = "Indicadores_Socioeconomicos_" + anoOuTotal + ".tsv"

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", nomeDoArquivoDePIB))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaInstituicoes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", pasta_regiao, nomeDoArquivoEstabelecimento))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIndicadores = list(dictReader)
