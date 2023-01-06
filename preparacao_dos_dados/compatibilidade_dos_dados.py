import io
import sys
import re
import unidecode  # requer instalacao (via 'pip install unidecode')
from csv import DictReader
from csv import DictWriter
from os import path

##
#
#   Definicoes iniciais (caminho de arquivos raiz, encoding de caracteres no console)
#
##

pathBase = path.dirname( __file__ )
sys.stdout = io.TextIOWrapper( sys.stdout.buffer,encoding='utf8' )

##
#
#   Alteracao de nomenclatura dos indices
#
##

# NOTA: Este passo foi realizado manualmente nos arquivos dos modelos de dados, conforme as definições do modelo de mapeamento na Figura 1 do relatório 
# de entrega

##
#
#   Compatibilidade entre os indices
#
##

##
#   ID_de_instituicao
##

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais", "Dados_de_Publicacoes.txt"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaDadosDePublicacoes = list(dictReader)

for dadoDePublicacao in listaDadosDePublicacoes:
    pattern = re.compile('(-\S*)$')
    dadoDePublicacao["ID_da_instituicao"] = pattern.sub('',dadoDePublicacao["ID_da_instituicao"])

indices = [ 
    "ID_do_autor", "ID_da_instituicao", "Ano", "Jornal", "ID_da_subdisciplina", 
    "No_de_autores_da_publicacao", "Peso_de_autoria", "Peso_de_indexacao_do_jornal", "Peso_total" ]

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "Dados_de_Publicacoes_alterado.csv") )
with open(filepath, 'w', newline='') as csvFile:
    writer = DictWriter(csvFile, fieldnames=indices)
    writer.writeheader()
    writer.writerows(listaDadosDePublicacoes)

## 
#   Nome_do_municipio
##

# NOTA: Foi realizada a retirada manual dos valores totais calculados nos modelos de estabelecimentos, uma vez que não são necessarios serem mantidos nos 
# arquivos, assim reservando estes para armazenar apenas os registros de dados

#   Lista dos PIB Municipais, utilizada para ligar nome do municipio ao ID respectivo 

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais", "PIB_dos_Municípios.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaPIBdosMunicipios = list(dictReader)

#   Lista dos estabelecimentos do ano de 2010, utilizada inicialmente para a criação de uma lista de traducao de nome de municipio para seu respectivo ID

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2015.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2015 = list(dictReader)

#   Criacao de correlação entre ID do estado e sua respectiva sigla utilizada nos modelos de estabelecimentos 

idDoEstadoRO = dict(idDoEstado = 11, sigla = "Ro")
idDoEstadoAC = dict(idDoEstado = 12, sigla = "Ac")
idDoEstadoAM = dict(idDoEstado = 13, sigla = "Am")
idDoEstadoRR = dict(idDoEstado = 14, sigla = "Rr")
idDoEstadoPA = dict(idDoEstado = 15, sigla = "Pa")
idDoEstadoAP = dict(idDoEstado = 16, sigla = "Ap")
idDoEstadoTO = dict(idDoEstado = 17, sigla = "To")
idDoEstadoMA = dict(idDoEstado = 21, sigla = "Ma")
idDoEstadoPI = dict(idDoEstado = 22, sigla = "Pi")
idDoEstadoCE = dict(idDoEstado = 23, sigla = "Ce")
idDoEstadoRN = dict(idDoEstado = 24, sigla = "Rn")
idDoEstadoPB = dict(idDoEstado = 25, sigla = "Pb")
idDoEstadoPE = dict(idDoEstado = 26, sigla = "Pe")
idDoEstadoAL = dict(idDoEstado = 27, sigla = "Al")
idDoEstadoSE = dict(idDoEstado = 28, sigla = "Se")
idDoEstadoBA = dict(idDoEstado = 29, sigla = "Ba")
idDoEstadoMG = dict(idDoEstado = 31, sigla = "Mg")
idDoEstadoES = dict(idDoEstado = 32, sigla = "Es")
idDoEstadoRJ = dict(idDoEstado = 33, sigla = "Rj")
idDoEstadoSP = dict(idDoEstado = 35, sigla = "Sp")
idDoEstadoPR = dict(idDoEstado = 41, sigla = "Pr")
idDoEstadoSC = dict(idDoEstado = 42, sigla = "Sc")
idDoEstadoRS = dict(idDoEstado = 43, sigla = "Rs")
idDoEstadoMS = dict(idDoEstado = 50, sigla = "Ms")
idDoEstadoMT = dict(idDoEstado = 51, sigla = "Mt")
idDoEstadoGO = dict(idDoEstado = 52, sigla = "Go")
idDoEstadoDF = dict(idDoEstado = 53, sigla = "Df")

listaDosIdsDosEstados = [
    idDoEstadoRO, idDoEstadoAC, idDoEstadoAM, idDoEstadoRR, idDoEstadoPA, 
    idDoEstadoAP, idDoEstadoTO, idDoEstadoMA, idDoEstadoPI, idDoEstadoCE, 
    idDoEstadoRN, idDoEstadoPB, idDoEstadoPE, idDoEstadoAL, idDoEstadoSE, 
    idDoEstadoBA, idDoEstadoMG, idDoEstadoES, idDoEstadoRJ, idDoEstadoSP, 
    idDoEstadoPR, idDoEstadoSC, idDoEstadoRS, idDoEstadoMS, idDoEstadoMT, 
    idDoEstadoGO, idDoEstadoDF ]

#   Criacao de lista da traducao para ser aplicada nos modelos de estabelecimento

listaTraducaoNomeParaId = []

for dadosEstabelecimentos2015 in listaEstabelecimentos2015 :
    
    traducao = dict( nome = dadosEstabelecimentos2015["Nome_do_municipio"], id = "NOT_FOUND" )

    print(dadosEstabelecimentos2015["Nome_do_municipio"])
    
    regexEstadoMunicipio = re.search(r"(\S{2})-(.*)", dadosEstabelecimentos2015["Nome_do_municipio"])
    siglaDoEstado = regexEstadoMunicipio.group(1)
    nomeDoMunicipio = unidecode.unidecode(regexEstadoMunicipio.group(2)).lower()

    idDoEstado = ""

    for estado in listaDosIdsDosEstados :
        if estado["sigla"] == siglaDoEstado :
            idDoEstado = int(estado["idDoEstado"])
            break
    
    for municipioPIB in listaPIBdosMunicipios:
        nomeMunicipioPIB = unidecode.unidecode(municipioPIB["Nome_do_municipio"]).replace('\'',' ').lower()
        idMunicipioPIB = int(municipioPIB["ID_do_estado"])
        if nomeMunicipioPIB == nomeDoMunicipio and idMunicipioPIB == idDoEstado :
            traducao["id"] = municipioPIB["ID_do_municipio"]
            break

    listaTraducaoNomeParaId.append( traducao )

indices = [ "nome", "id" ]

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "municipios.csv") )
with open(filepath, 'w+', newline='') as csvFile:
    writer = DictWriter(csvFile, fieldnames=indices)
    writer.writeheader()
    writer.writerows(listaTraducaoNomeParaId)
    
#   Substituicao dos nomes de cidades pelos seus respectivos ID nos modelos de estabelecimentos 

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados",  "municipios.csv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file)
    listaMunicipios = list(dictReader)

#       Estabelecimentos 2010

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2010.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2010 = list(dictReader)
    indicesEstabelecimentos2010 = dictReader.fieldnames

for estabelecimento2010 in listaEstabelecimentos2010 :

    idDoMunicipio = ""

    for municipio in listaMunicipios :
        if municipio["nome"] == estabelecimento2010["Nome_do_municipio"] :
            idDoMunicipio = municipio["id"]
            break
    
    estabelecimento2010["Nome_do_municipio"] = idDoMunicipio

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2010_ALTERADO.csv") )
with open(filepath, 'w+', newline='', encoding='utf8') as csvFile:
    writer = DictWriter(csvFile, fieldnames=indicesEstabelecimentos2010)
    writer.writeheader()
    writer.writerows(listaEstabelecimentos2010)

#       Estabelecimentos 2011

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2011.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2011 = list(dictReader)
    indicesEstabelecimentos2011 = dictReader.fieldnames

for estabelecimento2011 in listaEstabelecimentos2011 :

    idDoMunicipio = ""

    for municipio in listaMunicipios :
        if municipio["nome"] == estabelecimento2011["Nome_do_municipio"] :
            idDoMunicipio = municipio["id"]
            break
    
    estabelecimento2011["Nome_do_municipio"] = idDoMunicipio

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2011_ALTERADO.csv") )
with open(filepath, 'w+', newline='', encoding='utf8') as csvFile:
    writer = DictWriter(csvFile, fieldnames=indicesEstabelecimentos2011)
    writer.writeheader()
    writer.writerows(listaEstabelecimentos2011)

#       Estabelecimentos 2012

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2012.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2012 = list(dictReader)
    indicesEstabelecimentos2012 = dictReader.fieldnames

for estabelecimento2012 in listaEstabelecimentos2012 :

    idDoMunicipio = ""

    for municipio in listaMunicipios :
        if municipio["nome"] == estabelecimento2012["Nome_do_municipio"] :
            idDoMunicipio = municipio["id"]
            break
    
    estabelecimento2012["Nome_do_municipio"] = idDoMunicipio

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2012_ALTERADO.csv") )
with open(filepath, 'w+', newline='', encoding='utf8') as csvFile:
    writer = DictWriter(csvFile, fieldnames=indicesEstabelecimentos2012)
    writer.writeheader()
    writer.writerows(listaEstabelecimentos2012)

#       Estabelecimentos 2013

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2013.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2013 = list(dictReader)
    indicesEstabelecimentos2013 = dictReader.fieldnames

for estabelecimento2013 in listaEstabelecimentos2013 :

    idDoMunicipio = ""

    for municipio in listaMunicipios :
        if municipio["nome"] == estabelecimento2013["Nome_do_municipio"] :
            idDoMunicipio = municipio["id"]
            break
    
    estabelecimento2013["Nome_do_municipio"] = idDoMunicipio

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2013_ALTERADO.csv") )
with open(filepath, 'w+', newline='', encoding='utf8') as csvFile:
    writer = DictWriter(csvFile, fieldnames=indicesEstabelecimentos2013)
    writer.writeheader()
    writer.writerows(listaEstabelecimentos2013)

#       Estabelecimentos 2014

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2014.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2014 = list(dictReader)
    indicesEstabelecimentos2014 = dictReader.fieldnames

for estabelecimento2014 in listaEstabelecimentos2014 :

    idDoMunicipio = ""

    for municipio in listaMunicipios :
        if municipio["nome"] == estabelecimento2014["Nome_do_municipio"] :
            idDoMunicipio = municipio["id"]
            break
    
    estabelecimento2014["Nome_do_municipio"] = idDoMunicipio

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2014_ALTERADO.csv") )
with open(filepath, 'w+', newline='', encoding='utf8') as csvFile:
    writer = DictWriter(csvFile, fieldnames=indicesEstabelecimentos2014)
    writer.writeheader()
    writer.writerows(listaEstabelecimentos2014)

#       Estabelecimentos 2015

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2015.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2015 = list(dictReader)
    indicesEstabelecimentos2015 = dictReader.fieldnames

for estabelecimento2015 in listaEstabelecimentos2015 :

    idDoMunicipio = ""

    for municipio in listaMunicipios :
        if municipio["nome"] == estabelecimento2015["Nome_do_municipio"] :
            idDoMunicipio = municipio["id"]
            break
    
    estabelecimento2015["Nome_do_municipio"] = idDoMunicipio

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2015_ALTERADO.csv") )
with open(filepath, 'w+', newline='', encoding='utf8') as csvFile:
    writer = DictWriter(csvFile, fieldnames=indicesEstabelecimentos2015)
    writer.writeheader()
    writer.writerows(listaEstabelecimentos2015)

# NOTA: Apos a criacao dos modelos alterados, modificamos a nomenclatura do indice "Nome_do_municipio" para "ID_do_municipio" para refletir as 
# alteracoes feitas

#   Remocao de coluna redundante "Nome_de_municipio" do modelo de instituicoes

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "Instituicoes.txt"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')

    filepath2 = path.abspath( path.join(pathBase, "..", "dados", "alterados",  "Instituicoes_alterado.tsv"))
    with open(filepath2, 'w+', newline='', encoding='utf8') as file2 :
        indices = [ "ID_da_instituicao", "Nome_da_instituicao", "ID_do_estado", "ID_da_mesoregiao", "ID_da_microregiao", "ID_do_municipio" ]
        dictWriter = DictWriter( file2, fieldnames=indices, delimiter='\t')
        dictWriter.writeheader()

        for line in dictReader:
            del line['Nome_do_municipio']
            dictWriter.writerow(line)
