import io
import sys
import collections
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
#
#   Agrupamento da producao academica por ano, instituicao (e sub-disciplinas)
#
##

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "Dados_de_Publicacoes_alterado.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaDadosDePublicacoes = list(dictReader)

dictContadorPublicacoes = OrderedDict()

for publicacao in listaDadosDePublicacoes :
    idDeInstituicao = publicacao[ "ID_da_instituicao" ]
    idDaSubdisciplina = publicacao[ "ID_da_subdisciplina" ]
    anoPublicacao = publicacao[ "Ano" ]

    if ( idDeInstituicao, idDaSubdisciplina, anoPublicacao ) in dictContadorPublicacoes :
        dictContadorPublicacoes[( idDeInstituicao, idDaSubdisciplina, anoPublicacao )] += 1
    else:
        dictContadorPublicacoes[( idDeInstituicao, idDaSubdisciplina, anoPublicacao ) ] = 1

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "QuantificacaoDePublicacoes.csv"))
f = open(filepath, "w")
f.write("ID_da_instituicao\tID_da_subdisciplina\tAno\tPublicacoes\n")

for chave in dictContadorPublicacoes:
    idDeInstituicao, idDaSubdisciplina, anoPublicacao = chave
    f.write(
        "{}\t{}\t{}\t{}\n".format(
            idDeInstituicao, idDaSubdisciplina, anoPublicacao, dictContadorPublicacoes[chave]
        )
    )

f.close()

##
#
#   Agrupamento de índices socio-economicas por estados, mesoregioes e microregioes
#
##

#   - Microrregioes

#       + PIB

dictPIBMicrorregiao = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais", "PIB_dos_Municípios.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaPIBdosMunicipios = list(dictReader)

    for entrada in listaPIBdosMunicipios:

        ano = entrada["Ano"]
        idMicroregiao = entrada["ID_da_microregiao"]

        nomeMicroregiao = entrada["Nome_da_microregiao"]
        valorBrutoAgropecuaria = entrada["Valor_bruto_agropecuaria"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        valorBrutoIndustria = entrada["Valor_bruto_industria"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        valorBrutoServicos = entrada["Valor_bruto_servicos"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        valorBrutoAdministracao = entrada["Valor_bruto_administracao"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        valorBrutoTotal = entrada["Valor_bruto_total"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        impostos = entrada["Impostos"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        pib = entrada["PIB"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        populacao = entrada["Populacao"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        pibPerCapita = entrada["PIB_per_capita"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')

        if ( ano, idMicroregiao ) in dictPIBMicrorregiao :
            atualizadoValorBrutoAgropecuaria = float(dictPIBMicrorregiao[( ano, idMicroregiao )]["Valor_bruto_agropecuaria"]) + float(valorBrutoAgropecuaria)
            atualizadoValorBrutoIndustria = float(dictPIBMicrorregiao[( ano, idMicroregiao )]["Valor_bruto_industria"]) + float(valorBrutoIndustria)
            atualizadoValorBrutoServicos = float(dictPIBMicrorregiao[( ano, idMicroregiao )]["Valor_bruto_servicos"]) + float(valorBrutoServicos)
            atualizadoValorBrutoAdministracao = float(dictPIBMicrorregiao[( ano, idMicroregiao )]["Valor_bruto_administracao"]) + float(valorBrutoAdministracao)
            atualizadoValorBrutoTotal = float(dictPIBMicrorregiao[( ano, idMicroregiao )]["Valor_bruto_total"]) + float(valorBrutoTotal)
            atualizadoImpostos = float(dictPIBMicrorregiao[( ano, idMicroregiao )]["Impostos"]) + float(impostos)
            atualizadoPIB = float(dictPIBMicrorregiao[( ano, idMicroregiao )]["PIB"]) + float(pib)
            atualizadoPopulacao = float(dictPIBMicrorregiao[( ano, idMicroregiao )]["Populacao"]) + float(populacao)
            atualizadoPIBperCapita = float(dictPIBMicrorregiao[( ano, idMicroregiao )]["PIB_per_capita"]) + float(pibPerCapita)
            atualizado = dict( 
                Nome_da_microregiao = nomeMicroregiao, 
                Valor_bruto_agropecuaria = atualizadoValorBrutoAgropecuaria, 
                Valor_bruto_industria = atualizadoValorBrutoIndustria, 
                Valor_bruto_servicos = atualizadoValorBrutoServicos, 
                Valor_bruto_administracao = atualizadoValorBrutoAdministracao,
                Valor_bruto_total = atualizadoValorBrutoTotal, 
                Impostos = atualizadoImpostos, 
                PIB = atualizadoPIB, 
                Populacao = atualizadoPopulacao, 
                PIB_per_capita = atualizadoPIBperCapita
             )
            dictPIBMicrorregiao[( ano, idMicroregiao )] = atualizado
        else:
            novo = dict( 
                Nome_da_microregiao = nomeMicroregiao, 
                Valor_bruto_agropecuaria = valorBrutoAgropecuaria, 
                Valor_bruto_industria = valorBrutoIndustria, 
                Valor_bruto_servicos = valorBrutoServicos, 
                Valor_bruto_administracao = valorBrutoAdministracao,
                Valor_bruto_total = valorBrutoTotal, 
                Impostos = impostos, 
                PIB = pib, 
                Populacao = populacao, 
                PIB_per_capita = pibPerCapita
             )
            dictPIBMicrorregiao[( ano, idMicroregiao )] = novo

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "microrregioes", "PIBdeMicrorregioes.tsv"))
f = open(filepath, "w", encoding='utf8')
f.write("Ano\tID_da_microregiao\tNome_da_microregiao\tValor_bruto_agropecuaria\tValor_bruto_industria\tValor_bruto_servicos\tValor_bruto_administracao\tValor_bruto_total\tImpostos\tPIB\tPopulacao\tPIB_per_capita\n")

for chave in dictPIBMicrorregiao:
    ano, idMicroregiao = chave
    f.write(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
            ano, idMicroregiao, 
            dictPIBMicrorregiao[chave]["Nome_da_microregiao"],
            dictPIBMicrorregiao[chave]["Valor_bruto_agropecuaria"],
            dictPIBMicrorregiao[chave]["Valor_bruto_industria"],
            dictPIBMicrorregiao[chave]["Valor_bruto_servicos"],
            dictPIBMicrorregiao[chave]["Valor_bruto_administracao"],
            dictPIBMicrorregiao[chave]["Valor_bruto_total"],
            dictPIBMicrorregiao[chave]["Impostos"],
            dictPIBMicrorregiao[chave]["PIB"],
            dictPIBMicrorregiao[chave]["Populacao"],
            dictPIBMicrorregiao[chave]["PIB_per_capita"]
        )
    )

f.close()

#       + Obtencao de tabela de IDs de regioes (municipios, microrregioes, mesoregioes, estados)

dictIDsGeograficos = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais", "PIB_dos_Municípios.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaPIBdosMunicipios = list(dictReader)

    for entrada in listaPIBdosMunicipios :

        idMunicipio = entrada["ID_do_municipio"]

        idMicroregiao = entrada["ID_da_microregiao"]
        nomeMicroregiao = entrada["Nome_da_microregiao"]
        idMesoregiao = entrada["ID_da_mesoregiao"]
        nomeMesoregiao = entrada["Nome_da_mesoregiao"]
        idDoEstado = entrada["ID_do_estado"]
        nomeDoEstado = entrada["Nome_do_estado"]

        if idMunicipio not in dictIDsGeograficos :
            novo = dict( 
                ID_da_microregiao = idMicroregiao, 
                Nome_da_microregiao = nomeMicroregiao, 
                ID_da_mesoregiao = idMesoregiao, 
                Nome_da_mesoregiao = nomeMesoregiao, 
                ID_do_estado = idDoEstado, 
                Nome_do_estado = nomeDoEstado
            )
            dictIDsGeograficos[ idMunicipio ] = novo

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
f = open(filepath, "w", encoding='utf8')
f.write("ID_do_municipio\tID_da_microregiao\tNome_da_microregiao\tID_da_mesoregiao\tNome_da_mesoregiao\tID_do_estado\tNome_do_estado\n")

for idMunicipio in dictIDsGeograficos:
    f.write(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
            idMunicipio,
            dictIDsGeograficos[idMunicipio]["ID_da_microregiao"],
            dictIDsGeograficos[idMunicipio]["Nome_da_microregiao"],
            dictIDsGeograficos[idMunicipio]["ID_da_mesoregiao"],
            dictIDsGeograficos[idMunicipio]["Nome_da_mesoregiao"],
            dictIDsGeograficos[idMunicipio]["ID_do_estado"],
            dictIDsGeograficos[idMunicipio]["Nome_do_estado"]
        )
    )

f.close()

#       + Estabelecimentos 2010

dictEstabelecimentos2010 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2010_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2010 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2010:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idMicrorregiao = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idMicrorregiao = ids["ID_da_microregiao"]
                    break

            if idMicrorregiao in dictEstabelecimentos2010:
                dictValores = dictEstabelecimentos2010[idMicrorregiao]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2010[idMicrorregiao]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2010[idMicrorregiao] = soma
            else:
                dictEstabelecimentos2010[idMicrorregiao] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2010_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_da_microregiao")

f.write(headers)

for idMicrorregiao in dictEstabelecimentos2010:
    row = idMicrorregiao + "\t"
    
    for val in dictEstabelecimentos2010[idMicrorregiao].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()         
            
#       + Estabelecimentos 2011

dictEstabelecimentos2011 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2011_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2011 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2011:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idMicrorregiao = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idMicrorregiao = ids["ID_da_microregiao"]
                    break

            if idMicrorregiao in dictEstabelecimentos2011:
                dictValores = dictEstabelecimentos2011[idMicrorregiao]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2011[idMicrorregiao]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2011[idMicrorregiao] = soma
            else:
                dictEstabelecimentos2011[idMicrorregiao] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2011_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_da_microregiao")

f.write(headers)

for idMicrorregiao in dictEstabelecimentos2011:
    row = idMicrorregiao + "\t"
    
    for val in dictEstabelecimentos2011[idMicrorregiao].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()    

            
#       + Estabelecimentos 2012

dictEstabelecimentos2012 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2012_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2012 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2012:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idMicrorregiao = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idMicrorregiao = ids["ID_da_microregiao"]
                    break

            if idMicrorregiao in dictEstabelecimentos2012:
                dictValores = dictEstabelecimentos2012[idMicrorregiao]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2012[idMicrorregiao]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2012[idMicrorregiao] = soma
            else:
                dictEstabelecimentos2012[idMicrorregiao] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2012_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_da_microregiao")

f.write(headers)

for idMicrorregiao in dictEstabelecimentos2012:
    row = idMicrorregiao + "\t"
    
    for val in dictEstabelecimentos2012[idMicrorregiao].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()    

#       + Estabelecimentos 2013

dictEstabelecimentos2013 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2013_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2013 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2013:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idMicrorregiao = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idMicrorregiao = ids["ID_da_microregiao"]
                    break

            if idMicrorregiao in dictEstabelecimentos2013:
                dictValores = dictEstabelecimentos2013[idMicrorregiao]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2013[idMicrorregiao]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2013[idMicrorregiao] = soma
            else:
                dictEstabelecimentos2013[idMicrorregiao] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2013_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_da_microregiao")

f.write(headers)

for idMicrorregiao in dictEstabelecimentos2013:
    row = idMicrorregiao + "\t"
    
    for val in dictEstabelecimentos2013[idMicrorregiao].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()    

#       + Estabelecimentos 2014

dictEstabelecimentos2014 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2014_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2014 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2014:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idMicrorregiao = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idMicrorregiao = ids["ID_da_microregiao"]
                    break

            if idMicrorregiao in dictEstabelecimentos2014:
                dictValores = dictEstabelecimentos2014[idMicrorregiao]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2014[idMicrorregiao]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2014[idMicrorregiao] = soma
            else:
                dictEstabelecimentos2014[idMicrorregiao] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2014_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_da_microregiao")

f.write(headers)

for idMicrorregiao in dictEstabelecimentos2014:
    row = idMicrorregiao + "\t"
    
    for val in dictEstabelecimentos2014[idMicrorregiao].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()    

#       + Estabelecimentos 2015

dictEstabelecimentos2015 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2015_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2015 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2015:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idMicrorregiao = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idMicrorregiao = ids["ID_da_microregiao"]
                    break

            if idMicrorregiao in dictEstabelecimentos2015:
                dictValores = dictEstabelecimentos2015[idMicrorregiao]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2015[idMicrorregiao]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2015[idMicrorregiao] = soma
            else:
                dictEstabelecimentos2015[idMicrorregiao] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2015_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_da_microregiao")

f.write(headers)

for idMicrorregiao in dictEstabelecimentos2015:
    row = idMicrorregiao + "\t"
    
    for val in dictEstabelecimentos2015[idMicrorregiao].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()    

#   - Mesorregioes

#       + PIB

dictPIBMesorregiao = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais", "PIB_dos_Municípios.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaPIBdosMunicipios = list(dictReader)

    for entrada in listaPIBdosMunicipios:

        ano = entrada["Ano"]
        idMesoregiao = entrada["ID_da_mesoregiao"]

        nomeMesoregiao = entrada["Nome_da_mesoregiao"]

        valorBrutoAgropecuaria = entrada["Valor_bruto_agropecuaria"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        valorBrutoIndustria = entrada["Valor_bruto_industria"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        valorBrutoServicos = entrada["Valor_bruto_servicos"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        valorBrutoAdministracao = entrada["Valor_bruto_administracao"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        valorBrutoTotal = entrada["Valor_bruto_total"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        impostos = entrada["Impostos"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        pib = entrada["PIB"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        populacao = entrada["Populacao"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        pibPerCapita = entrada["PIB_per_capita"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')

        if ( ano, idMesoregiao ) in dictPIBMesorregiao :
            atualizadoValorBrutoAgropecuaria = float(dictPIBMesorregiao[( ano, idMesoregiao )]["Valor_bruto_agropecuaria"]) + float(valorBrutoAgropecuaria)
            atualizadoValorBrutoIndustria = float(dictPIBMesorregiao[( ano, idMesoregiao )]["Valor_bruto_industria"]) + float(valorBrutoIndustria)
            atualizadoValorBrutoServicos = float(dictPIBMesorregiao[( ano, idMesoregiao )]["Valor_bruto_servicos"]) + float(valorBrutoServicos)
            atualizadoValorBrutoAdministracao = float(dictPIBMesorregiao[( ano, idMesoregiao )]["Valor_bruto_administracao"]) + float(valorBrutoAdministracao)
            atualizadoValorBrutoTotal = float(dictPIBMesorregiao[( ano, idMesoregiao )]["Valor_bruto_total"]) + float(valorBrutoTotal)
            atualizadoImpostos = float(dictPIBMesorregiao[( ano, idMesoregiao )]["Impostos"]) + float(impostos)
            atualizadoPIB = float(dictPIBMesorregiao[( ano, idMesoregiao )]["PIB"]) + float(pib)
            atualizadoPopulacao = float(dictPIBMesorregiao[( ano, idMesoregiao )]["Populacao"]) + float(populacao)
            atualizadoPIBperCapita = float(dictPIBMesorregiao[( ano, idMesoregiao )]["PIB_per_capita"]) + float(pibPerCapita)
            atualizado = dict( 
                Nome_da_mesoregiao = nomeMesoregiao, 
                Valor_bruto_agropecuaria = atualizadoValorBrutoAgropecuaria, 
                Valor_bruto_industria = atualizadoValorBrutoIndustria, 
                Valor_bruto_servicos = atualizadoValorBrutoServicos, 
                Valor_bruto_administracao = atualizadoValorBrutoAdministracao,
                Valor_bruto_total = atualizadoValorBrutoTotal, 
                Impostos = atualizadoImpostos, 
                PIB = atualizadoPIB, 
                Populacao = atualizadoPopulacao, 
                PIB_per_capita = atualizadoPIBperCapita
             )
            dictPIBMesorregiao[( ano, idMesoregiao )] = atualizado
        else:
            novo = dict( 
                Nome_da_mesoregiao = nomeMesoregiao, 
                Valor_bruto_agropecuaria = valorBrutoAgropecuaria, 
                Valor_bruto_industria = valorBrutoIndustria, 
                Valor_bruto_servicos = valorBrutoServicos, 
                Valor_bruto_administracao = valorBrutoAdministracao,
                Valor_bruto_total = valorBrutoTotal, 
                Impostos = impostos, 
                PIB = pib, 
                Populacao = populacao, 
                PIB_per_capita = pibPerCapita
             )
            dictPIBMesorregiao[( ano, idMesoregiao )] = novo

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "mesorregioes", "PIBdeMesorregioes.tsv"))
f = open(filepath, "w", encoding='utf8')
f.write("Ano\tID_da_mesoregiao\tNome_da_mesoregiao\tValor_bruto_agropecuaria\tValor_bruto_industria\tValor_bruto_servicos\tValor_bruto_administracao\tValor_bruto_total\tImpostos\tPIB\tPopulacao\tPIB_per_capita\n")

for chave in dictPIBMesorregiao:
    ano, idMesoregiao = chave
    f.write(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
            ano, idMesoregiao, 
            dictPIBMesorregiao[chave]["Nome_da_mesoregiao"],
            dictPIBMesorregiao[chave]["Valor_bruto_agropecuaria"],
            dictPIBMesorregiao[chave]["Valor_bruto_industria"],
            dictPIBMesorregiao[chave]["Valor_bruto_servicos"],
            dictPIBMesorregiao[chave]["Valor_bruto_administracao"],
            dictPIBMesorregiao[chave]["Valor_bruto_total"],
            dictPIBMesorregiao[chave]["Impostos"],
            dictPIBMesorregiao[chave]["PIB"],
            dictPIBMesorregiao[chave]["Populacao"],
            dictPIBMesorregiao[chave]["PIB_per_capita"]
        )
    )

f.close()
    
#       + Estabelecimentos 2010

dictEstabelecimentos2010 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2010_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2010 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2010:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idMesoregiao = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idMesoregiao = ids["ID_da_mesoregiao"]
                    break

            if idMesoregiao in dictEstabelecimentos2010:
                dictValores = dictEstabelecimentos2010[idMesoregiao]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2010[idMesoregiao]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2010[idMesoregiao] = soma
            else:
                dictEstabelecimentos2010[idMesoregiao] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2010_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_da_mesoregiao")

f.write(headers)

for idMicrorregiao in dictEstabelecimentos2010:
    row = idMicrorregiao + "\t"
    
    for val in dictEstabelecimentos2010[idMicrorregiao].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()   

#       + Estabelecimentos 2011

dictEstabelecimentos2011 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2011_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2011 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2011:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idMesoregiao = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idMesoregiao = ids["ID_da_mesoregiao"]
                    break

            if idMesoregiao in dictEstabelecimentos2011:
                dictValores = dictEstabelecimentos2011[idMesoregiao]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2011[idMesoregiao]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2011[idMesoregiao] = soma
            else:
                dictEstabelecimentos2011[idMesoregiao] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2011_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_da_mesoregiao")

f.write(headers)

for idMicrorregiao in dictEstabelecimentos2011:
    row = idMicrorregiao + "\t"
    
    for val in dictEstabelecimentos2011[idMicrorregiao].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()   


#       + Estabelecimentos 2012

dictEstabelecimentos2012 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2012_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2012 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2012:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idMesoregiao = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idMesoregiao = ids["ID_da_mesoregiao"]
                    break

            if idMesoregiao in dictEstabelecimentos2012:
                dictValores = dictEstabelecimentos2012[idMesoregiao]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2012[idMesoregiao]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2012[idMesoregiao] = soma
            else:
                dictEstabelecimentos2012[idMesoregiao] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2012_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_da_mesoregiao")

f.write(headers)

for idMicrorregiao in dictEstabelecimentos2012:
    row = idMicrorregiao + "\t"
    
    for val in dictEstabelecimentos2012[idMicrorregiao].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()   

#       + Estabelecimentos 2013

dictEstabelecimentos2013 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2013_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2013 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2013:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idMesoregiao = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idMesoregiao = ids["ID_da_mesoregiao"]
                    break

            if idMesoregiao in dictEstabelecimentos2013:
                dictValores = dictEstabelecimentos2013[idMesoregiao]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2013[idMesoregiao]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2013[idMesoregiao] = soma
            else:
                dictEstabelecimentos2013[idMesoregiao] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2013_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_da_mesoregiao")

f.write(headers)

for idMicrorregiao in dictEstabelecimentos2013:
    row = idMicrorregiao + "\t"
    
    for val in dictEstabelecimentos2013[idMicrorregiao].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()   

#       + Estabelecimentos 2014

dictEstabelecimentos2014 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2014_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2014 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2014:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idMesoregiao = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idMesoregiao = ids["ID_da_mesoregiao"]
                    break

            if idMesoregiao in dictEstabelecimentos2014:
                dictValores = dictEstabelecimentos2014[idMesoregiao]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2014[idMesoregiao]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2014[idMesoregiao] = soma
            else:
                dictEstabelecimentos2014[idMesoregiao] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2014_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_da_mesoregiao")

f.write(headers)

for idMicrorregiao in dictEstabelecimentos2014:
    row = idMicrorregiao + "\t"
    
    for val in dictEstabelecimentos2014[idMicrorregiao].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()   

#       + Estabelecimentos 2015

dictEstabelecimentos2015 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2015_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2015 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2015:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idMesoregiao = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idMesoregiao = ids["ID_da_mesoregiao"]
                    break

            if idMesoregiao in dictEstabelecimentos2015:
                dictValores = dictEstabelecimentos2015[idMesoregiao]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2015[idMesoregiao]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2015[idMesoregiao] = soma
            else:
                dictEstabelecimentos2015[idMesoregiao] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2015_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_da_mesoregiao")

f.write(headers)

for idMicrorregiao in dictEstabelecimentos2015:
    row = idMicrorregiao + "\t"
    
    for val in dictEstabelecimentos2015[idMicrorregiao].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()   

#   - Estados

#       + PIB

dictPIBEstados = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais", "PIB_dos_Municípios.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaPIBdosMunicipios = list(dictReader)

    for entrada in listaPIBdosMunicipios:

        ano = entrada["Ano"]
        idDoEstado = entrada["ID_do_estado"]

        nomeDoEstado = entrada["Nome_do_estado"]

        valorBrutoAgropecuaria = entrada["Valor_bruto_agropecuaria"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        valorBrutoIndustria = entrada["Valor_bruto_industria"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        valorBrutoServicos = entrada["Valor_bruto_servicos"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        valorBrutoAdministracao = entrada["Valor_bruto_administracao"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        valorBrutoTotal = entrada["Valor_bruto_total"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        impostos = entrada["Impostos"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        pib = entrada["PIB"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        populacao = entrada["Populacao"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')
        pibPerCapita = entrada["PIB_per_capita"].strip().replace('.','').replace(',','.').replace('(','').replace(')','').replace('-','0')

        if ( ano, idDoEstado ) in dictPIBEstados :
            atualizadoValorBrutoAgropecuaria = float(dictPIBEstados[( ano, idDoEstado )]["Valor_bruto_agropecuaria"]) + float(valorBrutoAgropecuaria)
            atualizadoValorBrutoIndustria = float(dictPIBEstados[( ano, idDoEstado )]["Valor_bruto_industria"]) + float(valorBrutoIndustria)
            atualizadoValorBrutoServicos = float(dictPIBEstados[( ano, idDoEstado )]["Valor_bruto_servicos"]) + float(valorBrutoServicos)
            atualizadoValorBrutoAdministracao = float(dictPIBEstados[( ano, idDoEstado )]["Valor_bruto_administracao"]) + float(valorBrutoAdministracao)
            atualizadoValorBrutoTotal = float(dictPIBEstados[( ano, idDoEstado )]["Valor_bruto_total"]) + float(valorBrutoTotal)
            atualizadoImpostos = float(dictPIBEstados[( ano, idDoEstado )]["Impostos"]) + float(impostos)
            atualizadoPIB = float(dictPIBEstados[( ano, idDoEstado )]["PIB"]) + float(pib)
            atualizadoPopulacao = float(dictPIBEstados[( ano, idDoEstado )]["Populacao"]) + float(populacao)
            atualizadoPIBperCapita = float(dictPIBEstados[( ano, idDoEstado )]["PIB_per_capita"]) + float(pibPerCapita)
            atualizado = dict( 
                Nome_do_estado = nomeDoEstado, 
                Valor_bruto_agropecuaria = atualizadoValorBrutoAgropecuaria, 
                Valor_bruto_industria = atualizadoValorBrutoIndustria, 
                Valor_bruto_servicos = atualizadoValorBrutoServicos, 
                Valor_bruto_administracao = atualizadoValorBrutoAdministracao,
                Valor_bruto_total = atualizadoValorBrutoTotal, 
                Impostos = atualizadoImpostos, 
                PIB = atualizadoPIB, 
                Populacao = atualizadoPopulacao, 
                PIB_per_capita = atualizadoPIBperCapita
             )
            dictPIBEstados[( ano, idDoEstado )] = atualizado
        else:
            novo = dict( 
                Nome_do_estado = nomeDoEstado, 
                Valor_bruto_agropecuaria = valorBrutoAgropecuaria, 
                Valor_bruto_industria = valorBrutoIndustria, 
                Valor_bruto_servicos = valorBrutoServicos, 
                Valor_bruto_administracao = valorBrutoAdministracao,
                Valor_bruto_total = valorBrutoTotal, 
                Impostos = impostos, 
                PIB = pib, 
                Populacao = populacao, 
                PIB_per_capita = pibPerCapita
             )
            dictPIBEstados[( ano, idDoEstado )] = novo

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "estados", "PIBdeEstados.tsv"))
f = open(filepath, "w", encoding='utf8')
f.write("Ano\tID_do_estado\tNome_do_estado\tValor_bruto_agropecuaria\tValor_bruto_industria\tValor_bruto_servicos\tValor_bruto_administracao\tValor_bruto_total\tImpostos\tPIB\tPopulacao\tPIB_per_capita\n")

for chave in dictPIBEstados:
    ano, idDoEstado = chave
    f.write(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
            ano, idDoEstado, 
            dictPIBEstados[chave]["Nome_do_estado"],
            dictPIBEstados[chave]["Valor_bruto_agropecuaria"],
            dictPIBEstados[chave]["Valor_bruto_industria"],
            dictPIBEstados[chave]["Valor_bruto_servicos"],
            dictPIBEstados[chave]["Valor_bruto_administracao"],
            dictPIBEstados[chave]["Valor_bruto_total"],
            dictPIBEstados[chave]["Impostos"],
            dictPIBEstados[chave]["PIB"],
            dictPIBEstados[chave]["Populacao"],
            dictPIBEstados[chave]["PIB_per_capita"]
        )
    )

f.close()

#       + Estabelecimentos 2010

dictEstabelecimentos2010 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2010_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2010 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2010:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idEstado = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idEstado = ids["ID_do_estado"]
                    break

            if idEstado in dictEstabelecimentos2010:
                dictValores = dictEstabelecimentos2010[idEstado]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2010[idEstado]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2010[idEstado] = soma
            else:
                dictEstabelecimentos2010[idEstado] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "estados", "ESTABELECIMENTOS_ESTADOS_2010_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_do_estado")

f.write(headers)

for idEstado in dictEstabelecimentos2010:
    row = idEstado + "\t"
    
    for val in dictEstabelecimentos2010[idEstado].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()   

#       + Estabelecimentos 2011

dictEstabelecimentos2011 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2011_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2011 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2011:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idEstado = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idEstado = ids["ID_do_estado"]
                    break

            if idEstado in dictEstabelecimentos2011:
                dictValores = dictEstabelecimentos2011[idEstado]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2011[idEstado]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2011[idEstado] = soma
            else:
                dictEstabelecimentos2011[idEstado] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "estados", "ESTABELECIMENTOS_ESTADOS_2011_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_do_estado")

f.write(headers)

for idEstado in dictEstabelecimentos2011:
    row = idEstado + "\t"
    
    for val in dictEstabelecimentos2011[idEstado].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()   

#       + Estabelecimentos 2012

dictEstabelecimentos2012 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2012_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2012 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2012:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idEstado = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idEstado = ids["ID_do_estado"]
                    break

            if idEstado in dictEstabelecimentos2012:
                dictValores = dictEstabelecimentos2012[idEstado]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2012[idEstado]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2012[idEstado] = soma
            else:
                dictEstabelecimentos2012[idEstado] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "estados", "ESTABELECIMENTOS_ESTADOS_2012_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_do_estado")

f.write(headers)

for idEstado in dictEstabelecimentos2012:
    row = idEstado + "\t"
    
    for val in dictEstabelecimentos2012[idEstado].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()   

#       + Estabelecimentos 2013

dictEstabelecimentos2013 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2013_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2013 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2013:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idEstado = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idEstado = ids["ID_do_estado"]
                    break

            if idEstado in dictEstabelecimentos2013:
                dictValores = dictEstabelecimentos2013[idEstado]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2013[idEstado]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2013[idEstado] = soma
            else:
                dictEstabelecimentos2013[idEstado] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "estados", "ESTABELECIMENTOS_ESTADOS_2013_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_do_estado")

f.write(headers)

for idEstado in dictEstabelecimentos2013:
    row = idEstado + "\t"
    
    for val in dictEstabelecimentos2013[idEstado].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()   

#       + Estabelecimentos 2014

dictEstabelecimentos2014 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2014_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2014 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2014:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idEstado = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idEstado = ids["ID_do_estado"]
                    break

            if idEstado in dictEstabelecimentos2014:
                dictValores = dictEstabelecimentos2014[idEstado]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2014[idEstado]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2014[idEstado] = soma
            else:
                dictEstabelecimentos2014[idEstado] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "estados", "ESTABELECIMENTOS_ESTADOS_2014_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_do_estado")

f.write(headers)

for idEstado in dictEstabelecimentos2014:
    row = idEstado + "\t"
    
    for val in dictEstabelecimentos2014[idEstado].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()   

#       + Estabelecimentos 2015

dictEstabelecimentos2015 = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIDsGeograficos = list(dictReader)

    filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "RAIS_N_ESTABELECIMENTOS_2015_ALTERADO.csv"))
    with open(filepath, 'r', encoding='utf8') as file:
        dictReader = DictReader(file)
        listaEstabelecimentos2015 = list(dictReader)

        indices = []

        for field in dictReader.fieldnames:
            indices.append(field)

        for entrada in listaEstabelecimentos2015:
            valores = {k: int(v) for k, v in entrada.items() if k not in ["ID_do_municipio"]}

            idMunicipio = entrada["ID_do_municipio"]
            idEstado = "-"

            for ids in listaIDsGeograficos :
                if ids["ID_do_municipio"] == idMunicipio:
                    idEstado = ids["ID_do_estado"]
                    break

            if idEstado in dictEstabelecimentos2015:
                dictValores = dictEstabelecimentos2015[idEstado]
                dictValores = {k: int(v) for k, v in dictValores.items()}
                
                counter = collections.Counter()
                for d in [valores, dictEstabelecimentos2015[idEstado]]: 
                    counter.update(d)
                soma = dict(counter)
                dictEstabelecimentos2015[idEstado] = soma
            else:
                dictEstabelecimentos2015[idEstado] = valores
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "estados", "ESTABELECIMENTOS_ESTADOS_2015_ALTERADO.tsv"))
f = open(filepath, "w", encoding='utf8')

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"
headers = headers.replace("ID_do_municipio","ID_do_estado")

f.write(headers)

for idEstado in dictEstabelecimentos2015:
    row = idEstado + "\t"
    
    for val in dictEstabelecimentos2015[idEstado].values():
        row += str(val) + "\t"

    row = row[:-1] + "\n"

    f.write(row)

f.close()   
