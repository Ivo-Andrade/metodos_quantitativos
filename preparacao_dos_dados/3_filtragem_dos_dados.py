import io
import os
import sys
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
#   Filtragem da quantificacao da producao academica
#
##

##
#   Contagem de publicacoes por instituicoes (total, e por ano)
##

#   Criacao das tabelas para analise

dictContadorPublicacoesPorInstituicao = OrderedDict()
dictContadorPublicacoesPorInstituicaoEAno = OrderedDict()

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "QuantificacaoDePublicacoes.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaQuantificacaoPublicacoes = list(dictReader)

    for entrada in listaQuantificacaoPublicacoes :
        idDeInstituicao = entrada["ID_da_instituicao"]
        anoPublicacao = entrada["Ano"]
        quantidadePublicacoes = int(entrada["Publicacoes"])

        if ( idDeInstituicao ) in dictContadorPublicacoesPorInstituicao :
            dictContadorPublicacoesPorInstituicao[( idDeInstituicao )] += quantidadePublicacoes
        else:
            dictContadorPublicacoesPorInstituicao[( idDeInstituicao ) ] = quantidadePublicacoes

        if ( idDeInstituicao, anoPublicacao ) in dictContadorPublicacoesPorInstituicaoEAno :
            dictContadorPublicacoesPorInstituicaoEAno[( idDeInstituicao, anoPublicacao )] += quantidadePublicacoes
        else:
            dictContadorPublicacoesPorInstituicaoEAno[( idDeInstituicao, anoPublicacao ) ] = quantidadePublicacoes

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "QuantificacaoDePublicacoesPorInstituicao.tsv"))
f = open(filepath, "w")
f.write("ID_da_instituicao\tPublicacoes\n")

for chave in dictContadorPublicacoesPorInstituicao:
    idDeInstituicao = chave
    f.write(
        "{}\t{}\n".format(
            idDeInstituicao, dictContadorPublicacoesPorInstituicao[chave]
        )
    )

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "QuantificacaoDePublicacoesPorInstituicaoEAno.tsv"))
f = open(filepath, "w")
f.write("ID_da_instituicao\tAno\tPublicacoes\n")

for chave in dictContadorPublicacoesPorInstituicaoEAno:
    idDeInstituicao, anoPublicacao = chave
    f.write(
        "{}\t{}\t{}\n".format(
            idDeInstituicao, anoPublicacao, dictContadorPublicacoesPorInstituicaoEAno[chave]
        )
    )

f.close()

# NOTA: Ordenamos os resultados de QuantificacaoDePublicacoesPorInstituicao.tsv e 
# QuantificacaoDePublicacoesPorInstituicaoEAno.tsv via Google Docs, e os salvamos nos arquivos 
# QuantificacaoDePublicacoesPorInstituicao_Ordenado.tsv e QuantificacaoDePublicacoesPorInstituicaoEAno_Ordenado.tsv, respectivamente

#   Filtro de publicacoes minimas de uma dada instituicao em um dado ano

conjuntoIdDeInstituicoesBarradasPorFiltro1 = set()

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "QuantificacaoDePublicacoesPorInstituicaoEAno.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaPublicacoesAnuaisPorInstituicao = list(dictReader)

    for entrada in listaPublicacoesAnuaisPorInstituicao:
        if int(entrada["Publicacoes"]) < 10 :
            conjuntoIdDeInstituicoesBarradasPorFiltro1.add( entrada["ID_da_instituicao"] )

#   Filtro de publicacoes minimas de uma dada instituicao

conjuntoIdDeInstituicoesBarradasPorFiltro2 = set()

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "QuantificacaoDePublicacoesPorInstituicao.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaPublicacoesPorInstituicao = list(dictReader)

    for entrada in listaPublicacoesPorInstituicao:
        if int(entrada["Publicacoes"]) < 100 :
            conjuntoIdDeInstituicoesBarradasPorFiltro2.add( entrada["ID_da_instituicao"] )

conjuntoIdDeInstituicoesBarradasPorFiltros = conjuntoIdDeInstituicoesBarradasPorFiltro1.union(conjuntoIdDeInstituicoesBarradasPorFiltro2)

#   Utilizacao dos filtros para atualizacao das tabelas

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "QuantificacaoDePublicacoes.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaQuantidadesDePublicacoes = list(dictReader)

    for entrada in listaQuantidadesDePublicacoes:
        if entrada["ID_da_instituicao"] not in conjuntoIdDeInstituicoesBarradasPorFiltros:
            entradaFiltrada.append(entrada)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "QuantificacaoDePublicacoes_Filtrado.tsv"))
f = open(filepath, "w")
f.write("ID_da_instituicao\tID_da_disciplina\tAno\tPublicacoes\n")

for item in entradaFiltrada:
    f.write(
        "{}\t{}\t{}\t{}\n".format(
            item["ID_da_instituicao"], 
            item["ID_da_disciplina"], 
            item["Ano"], 
            item["Publicacoes"]
        )
    )

f.close()

##
#
#   Filtragem nos outros modelos definidadas pelas instituicoes selecionadas (e respectivas localidades)
#
##

#   Obtencao da lista de IDs de instituicoes

conjuntoDeIDsDeInstituicoes = set()

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "QuantificacaoDePublicacoes_filtrado.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaQuantidadePublicacoes_filtrado = list(dictReader)

    for entrada in listaQuantidadePublicacoes_filtrado :
        if entrada["ID_da_instituicao"] not in conjuntoDeIDsDeInstituicoes :
            conjuntoDeIDsDeInstituicoes.add( entrada["ID_da_instituicao"] )

#   Obtencao de IDs dos respectivos municipios destas instituicoes
#   Filtragem da lista de instituicoes

entradaFiltrada = []
conjuntoDeIDsDeMunicipios = set()

filepath = path.abspath( path.join(pathBase, "..", "dados", "1_compatibilidade_de_dados", "Instituicoes_alterado.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaInstituicoes = list(dictReader)

    for instituicao in listaInstituicoes :
        if instituicao["ID_da_instituicao"] in conjuntoDeIDsDeInstituicoes:
            conjuntoDeIDsDeMunicipios.add( instituicao["ID_do_municipio"] )
            entradaFiltrada.append( instituicao )

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "Instituicoes_filtrado.tsv"))
f = open(filepath, "w")
f.write("ID_da_instituicao\tNome_da_instituicao\tID_do_estado\tID_da_mesoregiao\tID_da_microregiao\tID_do_municipio\n")

for item in entradaFiltrada:
    f.write(
        "{}\t{}\t{}\t{}\t{}\t{}\n".format(
            item["ID_da_instituicao"], 
            item["Nome_da_instituicao"], 
            item["ID_do_estado"], 
            item["ID_da_mesoregiao"],
            item["ID_da_microregiao"],
            item["ID_do_municipio"]
        )
    )

f.close()

#   Obtencao de IDs de microrregioes, mesorregioes e estados

conjuntoDeIDsDeMicrorregioes = set()
conjuntoDeIDsDeMesorregioes = set()
conjuntoDeIDsDeEstados = set()

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "IDsGeograficos.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIdGeograficos = list(dictReader)

    for municipio in listaIdGeograficos :
        if municipio["ID_do_municipio"] in conjuntoDeIDsDeMunicipios:
            conjuntoDeIDsDeMicrorregioes.add( municipio["ID_da_microregiao"] )
            conjuntoDeIDsDeMesorregioes.add( municipio["ID_da_mesoregiao"] )
            conjuntoDeIDsDeEstados.add( municipio["ID_do_estado"] )

#   Filtragem dos outros modelos com base na lista de municipios filtrados

#   - Microrregioes

#   + PIB

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "microrregioes", "PIBdeMicrorregioes.tsv"))
with open(filepath, 'r', encoding='utf-8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaDePIBdeMicrorregioes = list(dictReader)

    for pib in listaDePIBdeMicrorregioes :
        if pib["ID_da_microregiao"] in conjuntoDeIDsDeMicrorregioes :
            entradaFiltrada.append( pib )

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "microrregioes") )
if not os.path.exists(filepath):
    os.makedirs(filepath)
    
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "microrregioes", "PIBdeMicrorregioes_filtrado.tsv") )
f = open(filepath, "w", encoding='utf-8')
f.write("Ano\tID_da_microregiao\tNome_da_microregiao\tValor_bruto_agropecuaria\tValor_bruto_industria\tValor_bruto_servicos\tValor_bruto_administracao\tValor_bruto_total\tImpostos\tPIB\tPopulacao\tPIB_per_capita\n")

for item in entradaFiltrada:
    f.write(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
            item["Ano"], 
            item["ID_da_microregiao"], 
            item["Nome_da_microregiao"], 
            item["Valor_bruto_agropecuaria"], 
            item["Valor_bruto_industria"], 
            item["Valor_bruto_servicos"], 
            item["Valor_bruto_administracao"], 
            item["Valor_bruto_total"], 
            item["Impostos"], 
            item["PIB"], 
            item["Populacao"], 
            item["PIB_per_capita"]
        )
    )

f.close()

#   + Estabelecimentos 2010

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2010_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2010 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for microrregiao in listaEstabelecimentosMicrorregioes2010 :
        if microrregiao["ID_da_microregiao"] in conjuntoDeIDsDeMicrorregioes :
            entradaFiltrada.append( microrregiao )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2010_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 

#   + Estabelecimentos 2011

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2011_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2011 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for microrregiao in listaEstabelecimentosMicrorregioes2011 :
        if microrregiao["ID_da_microregiao"] in conjuntoDeIDsDeMicrorregioes :
            entradaFiltrada.append( microrregiao )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2011_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 

#   + Estabelecimentos 2012

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2012_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2012 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for microrregiao in listaEstabelecimentosMicrorregioes2012 :
        if microrregiao["ID_da_microregiao"] in conjuntoDeIDsDeMicrorregioes :
            entradaFiltrada.append( microrregiao )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2012_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 

#   + Estabelecimentos 2013

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2013_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2013 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for microrregiao in listaEstabelecimentosMicrorregioes2013 :
        if microrregiao["ID_da_microregiao"] in conjuntoDeIDsDeMicrorregioes :
            entradaFiltrada.append( microrregiao )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2013_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 

#   + Estabelecimentos 2014

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2014_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2014 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for microrregiao in listaEstabelecimentosMicrorregioes2014 :
        if microrregiao["ID_da_microregiao"] in conjuntoDeIDsDeMicrorregioes :
            entradaFiltrada.append( microrregiao )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2014_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 

#   + Estabelecimentos 2015

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2015_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2015 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for microrregiao in listaEstabelecimentosMicrorregioes2015 :
        if microrregiao["ID_da_microregiao"] in conjuntoDeIDsDeMicrorregioes :
            entradaFiltrada.append( microrregiao )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2015_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 

#   - Mesorregioes

#   + PIB

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "mesorregioes", "PIBdeMesorregioes.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaDePIBdeMesorregioes = list(dictReader)

    for pib in listaDePIBdeMesorregioes :
        if pib["ID_da_mesoregiao"] in conjuntoDeIDsDeMesorregioes :
            entradaFiltrada.append( pib )
    
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "mesorregioes") )
if not os.path.exists(filepath):
    os.makedirs(filepath)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "mesorregioes", "PIBdeMesorregioes_filtrado.tsv") )
f = open(filepath, "w")
f.write("Ano\tID_da_mesoregiao\tNome_da_mesoregiao\tValor_bruto_agropecuaria\tValor_bruto_industria\tValor_bruto_servicos\tValor_bruto_administracao\tValor_bruto_total\tImpostos\tPIB\tPopulacao\tPIB_per_capita\n")

for item in entradaFiltrada:
    f.write(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
            item["Ano"], 
            item["ID_da_mesoregiao"], 
            item["Nome_da_mesoregiao"], 
            item["Valor_bruto_agropecuaria"], 
            item["Valor_bruto_industria"], 
            item["Valor_bruto_servicos"], 
            item["Valor_bruto_administracao"], 
            item["Valor_bruto_total"], 
            item["Impostos"], 
            item["PIB"], 
            item["Populacao"], 
            item["PIB_per_capita"]
        )
    )

f.close()

#   + Estabelecimentos 2010

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2010_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2010 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for mesorregiao in listaEstabelecimentosMesorregioes2010 :
        if mesorregiao["ID_da_mesoregiao"] in conjuntoDeIDsDeMesorregioes :
            entradaFiltrada.append( mesorregiao )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2010_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 

#   + Estabelecimentos 2011

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2011_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2011 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for mesorregiao in listaEstabelecimentosMesorregioes2011 :
        if mesorregiao["ID_da_mesoregiao"] in conjuntoDeIDsDeMesorregioes :
            entradaFiltrada.append( mesorregiao )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2011_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 

#   + Estabelecimentos 2012

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2012_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2012 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for mesorregiao in listaEstabelecimentosMesorregioes2012 :
        if mesorregiao["ID_da_mesoregiao"] in conjuntoDeIDsDeMesorregioes :
            entradaFiltrada.append( mesorregiao )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2012_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 

#   + Estabelecimentos 2013

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2013_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2013 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for mesorregiao in listaEstabelecimentosMesorregioes2013 :
        if mesorregiao["ID_da_mesoregiao"] in conjuntoDeIDsDeMesorregioes :
            entradaFiltrada.append( mesorregiao )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2013_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 

#   + Estabelecimentos 2014

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2014_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2014 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for mesorregiao in listaEstabelecimentosMesorregioes2014 :
        if mesorregiao["ID_da_mesoregiao"] in conjuntoDeIDsDeMesorregioes :
            entradaFiltrada.append( mesorregiao )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2014_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 

#   + Estabelecimentos 2015

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2015_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2015 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for mesorregiao in listaEstabelecimentosMesorregioes2015 :
        if mesorregiao["ID_da_mesoregiao"] in conjuntoDeIDsDeMesorregioes :
            entradaFiltrada.append( mesorregiao )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2015_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 

#   - Estados

#   + PIB

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "estados", "PIBdeEstados.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaDePIBdeEstados = list(dictReader)

    for pib in listaDePIBdeEstados :
        if pib["ID_do_estado"] in conjuntoDeIDsDeEstados :
            entradaFiltrada.append( pib )

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "estados") )
if not os.path.exists(filepath):
    os.makedirs(filepath)
    
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "estados", "PIBdeEstados_filtrado.tsv") )
f = open(filepath, "w")
f.write("Ano\tID_do_estado\tNome_do_estado\tValor_bruto_agropecuaria\tValor_bruto_industria\tValor_bruto_servicos\tValor_bruto_administracao\tValor_bruto_total\tImpostos\tPIB\tPopulacao\tPIB_per_capita\n")

for item in entradaFiltrada:
    f.write(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
            item["Ano"], 
            item["ID_do_estado"], 
            item["Nome_do_estado"], 
            item["Valor_bruto_agropecuaria"], 
            item["Valor_bruto_industria"], 
            item["Valor_bruto_servicos"], 
            item["Valor_bruto_administracao"], 
            item["Valor_bruto_total"], 
            item["Impostos"], 
            item["PIB"], 
            item["Populacao"], 
            item["PIB_per_capita"]
        )
    )

f.close()

#   + Estabelecimentos 2010

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "estados", "ESTABELECIMENTOS_ESTADOS_2010_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2010 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for estado in listaEstabelecimentosEstados2010 :
        if estado["ID_do_estado"] in conjuntoDeIDsDeEstados :
            entradaFiltrada.append( estado )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "estados", "ESTABELECIMENTOS_ESTADOS_2010_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 

#   + Estabelecimentos 2011

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "estados", "ESTABELECIMENTOS_ESTADOS_2011_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2011 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for estado in listaEstabelecimentosEstados2011 :
        if estado["ID_do_estado"] in conjuntoDeIDsDeEstados :
            entradaFiltrada.append( estado )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "estados", "ESTABELECIMENTOS_ESTADOS_2011_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 

#   + Estabelecimentos 2012

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "estados", "ESTABELECIMENTOS_ESTADOS_2012_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2012 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for estado in listaEstabelecimentosEstados2012 :
        if estado["ID_do_estado"] in conjuntoDeIDsDeEstados :
            entradaFiltrada.append( estado )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "estados", "ESTABELECIMENTOS_ESTADOS_2012_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 

#   + Estabelecimentos 2013

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "estados", "ESTABELECIMENTOS_ESTADOS_2013_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2013 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for estado in listaEstabelecimentosEstados2013 :
        if estado["ID_do_estado"] in conjuntoDeIDsDeEstados :
            entradaFiltrada.append( estado )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "estados", "ESTABELECIMENTOS_ESTADOS_2013_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 

#   + Estabelecimentos 2014

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "estados", "ESTABELECIMENTOS_ESTADOS_2014_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2014 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for estado in listaEstabelecimentosEstados2014 :
        if estado["ID_do_estado"] in conjuntoDeIDsDeEstados :
            entradaFiltrada.append( estado )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "estados", "ESTABELECIMENTOS_ESTADOS_2014_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 

#   + Estabelecimentos 2015

entradaFiltrada = []

filepath = path.abspath( path.join(pathBase, "..", "dados", "2_agregacao_de_dados", "estados", "ESTABELECIMENTOS_ESTADOS_2015_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2015 = list(dictReader)

    indices = []

    for field in dictReader.fieldnames:
        indices.append( field )

    for estado in listaEstabelecimentosEstados2015 :
        if estado["ID_do_estado"] in conjuntoDeIDsDeEstados :
            entradaFiltrada.append( estado )
       
filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "estados", "ESTABELECIMENTOS_ESTADOS_2015_FILTRADO.tsv"))
f = open(filepath, "w")

headers = ""
for index in indices:
    headers += index + "\t"
headers = headers[:-1] + "\n"

f.write(headers)

for entrada in entradaFiltrada:
    row = ""

    for indice in entrada.values():
        row += indice + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close() 