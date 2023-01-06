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

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais", "Dados_de_Publicacoes.txt"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaDadosDePublicacoes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "Instituicoes.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaInstituicoes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "Subdisciplinas.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaSubdisciplinas = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2010.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2010 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2011.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2011 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2012.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2012 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2013.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2013 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2014.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2014 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais",  "RAIS_N_ESTABELECIMENTOS_2015.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2015 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "iniciais", "PIB_dos_Municípios.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaPIBdosMunicipios = list(dictReader)

##
#
#   Obtenção dos modelos de dados alterados (para compatibilidade)
#
##

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "Dados_de_Publicacoes_alterado.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaDadosDePublicacoes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados", "Instituicoes_alterado.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaInstituicoes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados",  "municipios.csv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file)
    listaMunicipios = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados",  "RAIS_N_ESTABELECIMENTOS_2010_ALTERADO.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2010 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados",  "RAIS_N_ESTABELECIMENTOS_2011_ALTERADO.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2011 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados",  "RAIS_N_ESTABELECIMENTOS_2012_ALTERADO.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2012 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados",  "RAIS_N_ESTABELECIMENTOS_2013_ALTERADO.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2013 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados",  "RAIS_N_ESTABELECIMENTOS_2014_ALTERADO.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2014 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "alterados",  "RAIS_N_ESTABELECIMENTOS_2015_ALTERADO.csv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file)
    listaEstabelecimentos2015 = list(dictReader)

##
#
#   Obtenção dos modelos de dados calculados (durante a preparacao dos dados)
#
##

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "IDsGeograficos.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaIdGeograficos = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "QuantificacaoDePublicacoes.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaQuantidadePublicacoes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "QuantificacaoDePublicacoesPorInstituicao_Ordenado.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaPublicacoesPorInstituicao_ordenado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "QuantificacaoDePublicacoesPorInstituicao.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaPublicacoesPorInstituicao = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "QuantificacaoDePublicacoesPorInstituicaoEAno_Ordenado.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaPublicacoesPorInstituicaoEAno_ordenado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "QuantificacaoDePublicacoesPorInstituicaoEAno.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaPublicacoesPorInstituicaoEAno = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "microrregioes", "PIBdeMicrorregioes.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaDePIBdeMicrorregioes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2010_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2010 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2011_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2011 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2012_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2012 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2013_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2013 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2014_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2014 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2015_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2015 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "mesorregioes", "PIBdeMesorregioes.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaDePIBdeMesorregioes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2010_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2010 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2011_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2011 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2012_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2012 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2013_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2013 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2014_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2014 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2015_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2015 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "estados", "PIBdeEstados.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaDePIBdeEstados = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "estados", "ESTABELECIMENTOS_ESTADOS_2010_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2010 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "estados", "ESTABELECIMENTOS_ESTADOS_2011_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2011 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "estados", "ESTABELECIMENTOS_ESTADOS_2012_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2012 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "estados", "ESTABELECIMENTOS_ESTADOS_2013_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2013 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "estados", "ESTABELECIMENTOS_ESTADOS_2014_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2014 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "calculados", "estados", "ESTABELECIMENTOS_ESTADOS_2015_ALTERADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2015 = list(dictReader)

##
#
#   Obtenção dos modelos de dados filtrados (após a preparacao dos dados)
#
##

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "QuantificacaoDePublicacoes_Filtrado.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaQuantidadePublicacoes_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "QuantificacaoDePublicacoesPorInstituicao_Filtrado.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaPublicacoesPorInstituicao_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "QuantificacaoDePublicacoesPorInstituicaoEAno_Filtrado.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaPublicacoesPorInstituicaoEAno_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "Instituicoes_filtrado.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaInstituicoes_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "Subdisciplinas_filtrado.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaSubdisciplinas_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "microrregioes", "PIBdeMicrorregioes_filtrado.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaDePIBdeMicrorregioes_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2010_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2010 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2011_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2011 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2012_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2012 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2013_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2013 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2014_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2014 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "microrregioes", "ESTABELECIMENTOS_MICRORREGIOES_2015_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2015 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "mesorregioes", "PIBdeMicrorregioes_filtrado.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaDePIBdeMesorregioes_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2010_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2010_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2011_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2011_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2012_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2012_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2013_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2013_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2014_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2014_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "mesorregioes", "ESTABELECIMENTOS_MESORREGIOES_2015_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2015_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "microrregioes", "PIBdeEstados_filtrado.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaDePIBdeEstados_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "microrregioes", "ESTABELECIMENTOS_ESTADOS_2010_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2010_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "microrregioes", "ESTABELECIMENTOS_ESTADOS_2011_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2011_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "microrregioes", "ESTABELECIMENTOS_ESTADOS_2012_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2012_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "microrregioes", "ESTABELECIMENTOS_ESTADOS_2013_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2013_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "microrregioes", "ESTABELECIMENTOS_ESTADOS_2014_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2014_filtrado = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "filtrados", "microrregioes", "ESTABELECIMENTOS_ESTADOS_2015_FILTRADO.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2015_filtrado = list(dictReader)