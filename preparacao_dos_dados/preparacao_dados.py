import io
import sys
import csv
from os import path

pathBase = path.dirname( __file__ )
sys.stdout = io.TextIOWrapper( sys.stdout.buffer,encoding='utf8' )

##
#
#   Obtenção da tabelas iniciais
#
##

# filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais", "Dados_de_Publicacoes.txt"))
# with open(filepath, encoding='utf8') as entrada:
#     reader = csv.reader(entrada, delimiter='\t')
#     headersPublicacoes = next(reader)
#     dataPublicacoes = list(reader)

# filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "Instituicoes.txt"))
# with open(filepath, encoding='utf8') as entrada:
#     reader = csv.reader(entrada, delimiter='\t')
#     headersInstituicoes = next(reader)
#     dataInstituicoes = list(reader)

# filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "Subdisciplinas.tsv"))
# with open(filepath, encoding='utf8') as entrada:
#     reader = csv.reader(entrada, delimiter='\t')
#     headersSubdisciplinas = next(reader)
#     dataSubdisciplinas = list(reader)

# filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2010.csv"))
# with open(filepath, encoding='utf8') as entrada:
#     reader = csv.reader(entrada, delimiter='\t')
#     next(reader)
#     headersEstabelecimentos2010 = next(reader)
#     dataEstabelecimentos2010 = list(reader)

# filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2011.csv"))
# with open(filepath, encoding='utf8') as entrada:
#     reader = csv.reader(entrada, delimiter='\t')
#     next(reader)
#     headersEstabelecimentos2011 = next(reader)
#     dataEstabelecimentos2011 = list(reader)

# filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2012.csv"))
# with open(filepath, encoding='utf8') as entrada:
#     reader = csv.reader(entrada, delimiter='\t')
#     next(reader)
#     headersEstabelecimentos2012 = next(reader)
#     dataEstabelecimentos2012 = list(reader)

# filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2013.csv"))
# with open(filepath, encoding='utf8') as entrada:
#     reader = csv.reader(entrada, delimiter='\t')
#     next(reader)
#     headersEstabelecimentos2013 = next(reader)
#     dataEstabelecimentos2013 = list(reader)

# filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2014.csv"))
# with open(filepath, encoding='utf8') as entrada:
#     reader = csv.reader(entrada, delimiter='\t')
#     next(reader)
#     headersEstabelecimentos2014 = next(reader)
#     dataEstabelecimentos2014 = list(reader)

# filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2015.csv"))
# with open(filepath, encoding='utf8') as entrada:
#     reader = csv.reader(entrada, delimiter='\t')
#     next(reader)
#     headersEstabelecimentos2015 = next(reader)
#     dataEstabelecimentos2015 = list(reader)

# filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais", "PIB_dos_Municípios.csv"))
# with open(filepath, encoding='utf8') as entrada:
#     reader = csv.reader(entrada)
#     headersPIBdosMunicipios = next(reader)
#     dataPIBdosMunicipios = list(reader)

##
#
#   Tratamento de dados iniciais
#
##

# dictPublicacoesPorAnoInstituicao = {}
# dictPublicacoesPorAnoInstituicaoSubdisciplina = {}

# for chave in dataPublicacoes:
#     idDaInstituicao = chave[1]
#     anoPublicacao = chave[2]
#     subDisciplina = chave[4]

#     if ( idDaInstituicao, anoPublicacao ) in dictPublicacoesPorAnoInstituicao:
#         dictPublicacoesPorAnoInstituicao[( idDaInstituicao, anoPublicacao )] += 1
#     else:
#         dictPublicacoesPorAnoInstituicao[( idDaInstituicao, anoPublicacao )] = 1

#     if ( idDaInstituicao, anoPublicacao, subDisciplina ) in dictPublicacoesPorAnoInstituicaoSubdisciplina:
#         dictPublicacoesPorAnoInstituicaoSubdisciplina[( idDaInstituicao, anoPublicacao, subDisciplina )] += 1
#     else:
#         dictPublicacoesPorAnoInstituicaoSubdisciplina[( idDaInstituicao, anoPublicacao, subDisciplina )] = 1

# filepathPublicacoesPorAnoInstituicao = path.abspath( path.join(pathBase, "..", "dados", "calculados", "PublicacoesPorAnoInstituicao.csv"))
# f = open(filepathPublicacoesPorAnoInstituicao, "w")
# f.write("idDaInstituicao\tanoDePublicacao\ttotal\n")

# for chave in dictPublicacoesPorAnoInstituicao:
#     idDaInstituicao, anoPublicacao = chave
#     f.write("{}\t{}\t{}\n".format(idDaInstituicao, anoPublicacao, dictPublicacoesPorAnoInstituicao[chave]))

# f.close()

# filepathPublicacoesPorAnoInstituicaoSubdisciplina = path.abspath( path.join(pathBase, "..", "dados", "calculados", "PublicacoesPorAnoInstituicaoSubdisciplina.csv"))
# f = open(filepathPublicacoesPorAnoInstituicaoSubdisciplina, "w")
# f.write("idDaInstituicao\tanoDePublicacao\tsub_disciplina\ttotal\n")

# for chave in dictPublicacoesPorAnoInstituicaoSubdisciplina:
#     idDaInstituicao, anoPublicacao, subDisciplina = chave
#     f.write("{}\t{}\t{}\t{}\n".format(idDaInstituicao, anoPublicacao, subDisciplina, dictPublicacoesPorAnoInstituicaoSubdisciplina[chave]))

# f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "PublicacoesPorAnoInstituicao.csv"))
with open(filepath, encoding='utf8') as entrada:
    reader = csv.reader(entrada, delimiter="\t")
    headersPublicacoesPorAnoInstituicao = next(reader)
    dataPublicacoesPorAnoInstituicao = list(reader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "PublicacoesPorAnoInstituicaoSubdisciplina.csv"))
with open(filepath, encoding='utf8') as entrada:
    reader = csv.reader(entrada, delimiter="\t")
    headersPublicacoesPorAnoInstituicaoSubdisciplina = next(reader)
    dataPublicacoesPorAnoInstituicaoSubdisciplina = list(reader)

# TODO: Filter expressive producers

