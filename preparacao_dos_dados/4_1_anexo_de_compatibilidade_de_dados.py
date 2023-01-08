import io
import os
import sys
import copy
from csv import DictReader
from os import path
from collections import OrderedDict

##
#
#   Definicoes iniciais (caminho de arquivos raíz, encoding de caracteres no console)
#
##

pathBase = path.dirname( __file__ )
sys.stdout = io.TextIOWrapper( sys.stdout.buffer,encoding='utf8' )

##
#   Correção dos IDs de microrregião e mesoregião das instituições
##

nomeDoArquivoDeInstituicoes = "Publicacoes_Instituicoes_2010.tsv"

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", nomeDoArquivoDeInstituicoes))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaInstituicoes2010 = list(dictReader)

    indices = []
    for field in dictReader.fieldnames:
        indices.append( field )

for instituicao in listaInstituicoes2010:

    idDeMicrorregiao = instituicao["ID_da_microregiao"]
    idDeMesorregiao = instituicao["ID_da_mesoregiao"]

    if len( idDeMicrorregiao ) == 6:
        novoIdDeMicrorregiao = idDeMicrorregiao[:2] + idDeMicrorregiao[-3:]
        instituicao["ID_da_microregiao"] = novoIdDeMicrorregiao
    if len( idDeMesorregiao ) == 6:
        novoIdDeMesorregiao = idDeMesorregiao[:2] + idDeMesorregiao[-2:]
        instituicao["ID_da_mesoregiao"] = novoIdDeMesorregiao


filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", nomeDoArquivoDeInstituicoes))
f = open(filepath, "w", encoding='utf-8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for instituicao in listaInstituicoes2010 :
    row = ""
    
    for val in instituicao.values() :
        row += str(val) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

nomeDoArquivoDeInstituicoes = "Publicacoes_Instituicoes_2011.tsv"

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", nomeDoArquivoDeInstituicoes))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaInstituicoes2011 = list(dictReader)

    indices = []
    for field in dictReader.fieldnames:
        indices.append( field )

for instituicao in listaInstituicoes2011:

    idDeMicrorregiao = instituicao["ID_da_microregiao"]
    idDeMesorregiao = instituicao["ID_da_mesoregiao"]

    if len( idDeMicrorregiao ) == 6:
        novoIdDeMicrorregiao = idDeMicrorregiao[:2] + idDeMicrorregiao[-3:]
        instituicao["ID_da_microregiao"] = novoIdDeMicrorregiao
    if len( idDeMesorregiao ) == 6:
        novoIdDeMesorregiao = idDeMesorregiao[:2] + idDeMesorregiao[-2:]
        instituicao["ID_da_mesoregiao"] = novoIdDeMesorregiao


filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", nomeDoArquivoDeInstituicoes))
f = open(filepath, "w", encoding='utf-8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for instituicao in listaInstituicoes2011 :
    row = ""
    
    for val in instituicao.values() :
        row += str(val) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

nomeDoArquivoDeInstituicoes = "Publicacoes_Instituicoes_2012.tsv"

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", nomeDoArquivoDeInstituicoes))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaInstituicoes2012 = list(dictReader)

    indices = []
    for field in dictReader.fieldnames:
        indices.append( field )

for instituicao in listaInstituicoes2012:

    idDeMicrorregiao = instituicao["ID_da_microregiao"]
    idDeMesorregiao = instituicao["ID_da_mesoregiao"]

    if len( idDeMicrorregiao ) == 6:
        novoIdDeMicrorregiao = idDeMicrorregiao[:2] + idDeMicrorregiao[-3:]
        instituicao["ID_da_microregiao"] = novoIdDeMicrorregiao
    if len( idDeMesorregiao ) == 6:
        novoIdDeMesorregiao = idDeMesorregiao[:2] + idDeMesorregiao[-2:]
        instituicao["ID_da_mesoregiao"] = novoIdDeMesorregiao


filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", nomeDoArquivoDeInstituicoes))
f = open(filepath, "w", encoding='utf-8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for instituicao in listaInstituicoes2012 :
    row = ""
    
    for val in instituicao.values() :
        row += str(val) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

nomeDoArquivoDeInstituicoes = "Publicacoes_Instituicoes_2013.tsv"

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", nomeDoArquivoDeInstituicoes))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaInstituicoes2013 = list(dictReader)

    indices = []
    for field in dictReader.fieldnames:
        indices.append( field )

for instituicao in listaInstituicoes2013:

    idDeMicrorregiao = instituicao["ID_da_microregiao"]
    idDeMesorregiao = instituicao["ID_da_mesoregiao"]

    if len( idDeMicrorregiao ) == 6:
        novoIdDeMicrorregiao = idDeMicrorregiao[:2] + idDeMicrorregiao[-3:]
        instituicao["ID_da_microregiao"] = novoIdDeMicrorregiao
    if len( idDeMesorregiao ) == 6:
        novoIdDeMesorregiao = idDeMesorregiao[:2] + idDeMesorregiao[-2:]
        instituicao["ID_da_mesoregiao"] = novoIdDeMesorregiao


filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", nomeDoArquivoDeInstituicoes))
f = open(filepath, "w", encoding='utf-8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for instituicao in listaInstituicoes2013 :
    row = ""
    
    for val in instituicao.values() :
        row += str(val) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

nomeDoArquivoDeInstituicoes = "Publicacoes_Instituicoes_2014.tsv"

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", nomeDoArquivoDeInstituicoes))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaInstituicoes2014 = list(dictReader)

    indices = []
    for field in dictReader.fieldnames:
        indices.append( field )

for instituicao in listaInstituicoes2014:

    idDeMicrorregiao = instituicao["ID_da_microregiao"]
    idDeMesorregiao = instituicao["ID_da_mesoregiao"]

    if len( idDeMicrorregiao ) == 6:
        novoIdDeMicrorregiao = idDeMicrorregiao[:2] + idDeMicrorregiao[-3:]
        instituicao["ID_da_microregiao"] = novoIdDeMicrorregiao
    if len( idDeMesorregiao ) == 6:
        novoIdDeMesorregiao = idDeMesorregiao[:2] + idDeMesorregiao[-2:]
        instituicao["ID_da_mesoregiao"] = novoIdDeMesorregiao


filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", nomeDoArquivoDeInstituicoes))
f = open(filepath, "w", encoding='utf-8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for instituicao in listaInstituicoes2014 :
    row = ""
    
    for val in instituicao.values() :
        row += str(val) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

nomeDoArquivoDeInstituicoes = "Publicacoes_Instituicoes_2015.tsv"

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", nomeDoArquivoDeInstituicoes))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaInstituicoes2015 = list(dictReader)

    indices = []
    for field in dictReader.fieldnames:
        indices.append( field )

for instituicao in listaInstituicoes2015:

    idDeMicrorregiao = instituicao["ID_da_microregiao"]
    idDeMesorregiao = instituicao["ID_da_mesoregiao"]

    if len( idDeMicrorregiao ) == 6:
        novoIdDeMicrorregiao = idDeMicrorregiao[:2] + idDeMicrorregiao[-3:]
        instituicao["ID_da_microregiao"] = novoIdDeMicrorregiao
    if len( idDeMesorregiao ) == 6:
        novoIdDeMesorregiao = idDeMesorregiao[:2] + idDeMesorregiao[-2:]
        instituicao["ID_da_mesoregiao"] = novoIdDeMesorregiao


filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", nomeDoArquivoDeInstituicoes))
f = open(filepath, "w", encoding='utf-8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for instituicao in listaInstituicoes2015 :
    row = ""
    
    for val in instituicao.values() :
        row += str(val) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

nomeDoArquivoDeInstituicoes = "Publicacoes_Instituicoes_Total.tsv"

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", nomeDoArquivoDeInstituicoes))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaInstituicoesTotal = list(dictReader)

    indices = []
    for field in dictReader.fieldnames:
        indices.append( field )

for instituicao in listaInstituicoesTotal:

    idDeMicrorregiao = instituicao["ID_da_microregiao"]
    idDeMesorregiao = instituicao["ID_da_mesoregiao"]

    if len( idDeMicrorregiao ) == 6:
        novoIdDeMicrorregiao = idDeMicrorregiao[:2] + idDeMicrorregiao[-3:]
        instituicao["ID_da_microregiao"] = novoIdDeMicrorregiao
    if len( idDeMesorregiao ) == 6:
        novoIdDeMesorregiao = idDeMesorregiao[:2] + idDeMesorregiao[-2:]
        instituicao["ID_da_mesoregiao"] = novoIdDeMesorregiao


filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", nomeDoArquivoDeInstituicoes))
f = open(filepath, "w", encoding='utf-8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for instituicao in listaInstituicoesTotal :
    row = ""
    
    for val in instituicao.values() :
        row += str(val) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

