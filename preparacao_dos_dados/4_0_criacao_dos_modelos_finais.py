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
#   Criação dos modelos de instituicoes
##

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "Instituicoes_filtrado.tsv"))
with open(filepath, 'r') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaInstituicoes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", "QuantificacaoDePublicacoes_Filtrado.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaDadosDePublicacoes = list(dictReader)

listaInstituicoesEm2010 = OrderedDict()
listaInstituicoesEm2011 = OrderedDict()
listaInstituicoesEm2012 = OrderedDict()
listaInstituicoesEm2013 = OrderedDict()
listaInstituicoesEm2014 = OrderedDict()
listaInstituicoesEm2015 = OrderedDict()
listaInstituicoesTotal = OrderedDict()

for contagemPublicacoes in listaDadosDePublicacoes :
        
    idDaInstituicao = contagemPublicacoes["ID_da_instituicao"]

    idDaDisciplina = int(contagemPublicacoes["ID_da_disciplina"])
    anoPublicacao = int(contagemPublicacoes["Ano"])
    noDePublicacoes = int(contagemPublicacoes["Publicacoes"])

    if idDaInstituicao not in listaInstituicoesTotal :

        nomeDaInstituicao = "-1"
        idDaMicrorregiao = "-1"
        idDaMesorregiao = "-1"
        idDoEstado = "-1"

        for instituicao in listaInstituicoes :
            if instituicao["ID_da_instituicao"] == idDaInstituicao :
                nomeDaInstituicao = instituicao["Nome_da_instituicao"]
                idDaMicrorregiao = instituicao["ID_da_microregiao"]
                idDaMesorregiao = instituicao["ID_da_mesoregiao"]
                idDoEstado = instituicao["ID_do_estado"]
                break

        dictInstituicaoNovo = dict(
            nome_da_instituicao = nomeDaInstituicao,
            ID_da_microregiao = idDaMicrorregiao,
            ID_da_mesoregiao = idDaMesorregiao,
            ID_do_estado = idDoEstado,
            Publicacoes_Disciplina_Biologia = 0,
            Publicacoes_Disciplina_Biotecnologia = 0,
            Publicacoes_Disciplina_Especialidades_Medicas = 0,
            Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica = 0,
            Publicacoes_Disciplina_Quimica = 0,
            Publicacoes_Disciplina_Ciencias_da_Natureza = 0,
            Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao = 0,
            Publicacoes_Disciplina_Pesquisas_Neurologicas = 0,
            Publicacoes_Disciplina_Humanas = 0,
            Publicacoes_Disciplina_Doencas_Infecciosas = 0,
            Publicacoes_Disciplina_Matematica_e_Fisica = 0,
            Publicacoes_Disciplina_Profissionais_da_Saude = 0,
            Publicacoes_Disciplina_Ciencias_Sociais = 0,
            Total_Publicacoes = 0
        )

        listaInstituicoesEm2010[idDaInstituicao] = copy.copy(dictInstituicaoNovo)
        listaInstituicoesEm2011[idDaInstituicao] = copy.copy(dictInstituicaoNovo)
        listaInstituicoesEm2012[idDaInstituicao] = copy.copy(dictInstituicaoNovo)
        listaInstituicoesEm2013[idDaInstituicao] = copy.copy(dictInstituicaoNovo)
        listaInstituicoesEm2014[idDaInstituicao] = copy.copy(dictInstituicaoNovo)
        listaInstituicoesEm2015[idDaInstituicao] = copy.copy(dictInstituicaoNovo)
        listaInstituicoesTotal[idDaInstituicao] = copy.copy(dictInstituicaoNovo)

    if anoPublicacao == 2010 :
        if idDaDisciplina == 1 :
            listaInstituicoesEm2010[idDaInstituicao]["Publicacoes_Disciplina_Biologia"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Biologia"] += noDePublicacoes
            listaInstituicoesEm2010[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 2 :
            listaInstituicoesEm2010[idDaInstituicao]["Publicacoes_Disciplina_Biotecnologia"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Biotecnologia"] += noDePublicacoes
            listaInstituicoesEm2010[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 3 :
            listaInstituicoesEm2010[idDaInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"] += noDePublicacoes
            listaInstituicoesEm2010[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 4 :
            listaInstituicoesEm2010[idDaInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"] += noDePublicacoes
            listaInstituicoesEm2010[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 5 :
            listaInstituicoesEm2010[idDaInstituicao]["Publicacoes_Disciplina_Quimica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Quimica"] += noDePublicacoes
            listaInstituicoesEm2010[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 6 :
            listaInstituicoesEm2010[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"] += noDePublicacoes
            listaInstituicoesEm2010[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 7 :
            listaInstituicoesEm2010[idDaInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"] += noDePublicacoes
            listaInstituicoesEm2010[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 8 :
            listaInstituicoesEm2010[idDaInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"] += noDePublicacoes
            listaInstituicoesEm2010[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 9 :
            listaInstituicoesEm2010[idDaInstituicao]["Publicacoes_Disciplina_Humanas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Humanas"] += noDePublicacoes
            listaInstituicoesEm2010[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 10 :
            listaInstituicoesEm2010[idDaInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"] += noDePublicacoes
            listaInstituicoesEm2010[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 11 :
            listaInstituicoesEm2010[idDaInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"] += noDePublicacoes
            listaInstituicoesEm2010[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 12 :
            listaInstituicoesEm2010[idDaInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"] += noDePublicacoes
            listaInstituicoesEm2010[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 13 :
            listaInstituicoesEm2010[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"] += noDePublicacoes
            listaInstituicoesEm2010[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
    elif anoPublicacao == 2011 :
        if idDaDisciplina == 1 :
            listaInstituicoesEm2011[idDaInstituicao]["Publicacoes_Disciplina_Biologia"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Biologia"] += noDePublicacoes
            listaInstituicoesEm2011[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 2 :
            listaInstituicoesEm2011[idDaInstituicao]["Publicacoes_Disciplina_Biotecnologia"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Biotecnologia"] += noDePublicacoes
            listaInstituicoesEm2011[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 3 :
            listaInstituicoesEm2011[idDaInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"] += noDePublicacoes
            listaInstituicoesEm2011[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 4 :
            listaInstituicoesEm2011[idDaInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"] += noDePublicacoes
            listaInstituicoesEm2011[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 5 :
            listaInstituicoesEm2011[idDaInstituicao]["Publicacoes_Disciplina_Quimica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Quimica"] += noDePublicacoes
            listaInstituicoesEm2011[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 6 :
            listaInstituicoesEm2011[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"] += noDePublicacoes
            listaInstituicoesEm2011[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 7 :
            listaInstituicoesEm2011[idDaInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"] += noDePublicacoes
            listaInstituicoesEm2011[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 8 :
            listaInstituicoesEm2011[idDaInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"] += noDePublicacoes
            listaInstituicoesEm2011[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 9 :
            listaInstituicoesEm2011[idDaInstituicao]["Publicacoes_Disciplina_Humanas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Humanas"] += noDePublicacoes
            listaInstituicoesEm2011[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 10 :
            listaInstituicoesEm2011[idDaInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"] += noDePublicacoes
            listaInstituicoesEm2011[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 11 :
            listaInstituicoesEm2011[idDaInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"] += noDePublicacoes
            listaInstituicoesEm2011[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 12 :
            listaInstituicoesEm2011[idDaInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"] += noDePublicacoes
            listaInstituicoesEm2011[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 13 :
            listaInstituicoesEm2011[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"] += noDePublicacoes
            listaInstituicoesEm2011[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
    elif anoPublicacao == 2012 :
        if idDaDisciplina == 1 :
            listaInstituicoesEm2012[idDaInstituicao]["Publicacoes_Disciplina_Biologia"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Biologia"] += noDePublicacoes
            listaInstituicoesEm2012[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 2 :
            listaInstituicoesEm2012[idDaInstituicao]["Publicacoes_Disciplina_Biotecnologia"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Biotecnologia"] += noDePublicacoes
            listaInstituicoesEm2012[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 3 :
            listaInstituicoesEm2012[idDaInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"] += noDePublicacoes
            listaInstituicoesEm2012[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 4 :
            listaInstituicoesEm2012[idDaInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"] += noDePublicacoes
            listaInstituicoesEm2012[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 5 :
            listaInstituicoesEm2012[idDaInstituicao]["Publicacoes_Disciplina_Quimica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Quimica"] += noDePublicacoes
            listaInstituicoesEm2012[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 6 :
            listaInstituicoesEm2012[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"] += noDePublicacoes
            listaInstituicoesEm2012[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 7 :
            listaInstituicoesEm2012[idDaInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"] += noDePublicacoes
            listaInstituicoesEm2012[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 8 :
            listaInstituicoesEm2012[idDaInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"] += noDePublicacoes
            listaInstituicoesEm2012[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 9 :
            listaInstituicoesEm2012[idDaInstituicao]["Publicacoes_Disciplina_Humanas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Humanas"] += noDePublicacoes
            listaInstituicoesEm2012[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 10 :
            listaInstituicoesEm2012[idDaInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"] += noDePublicacoes
            listaInstituicoesEm2012[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 11 :
            listaInstituicoesEm2012[idDaInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"] += noDePublicacoes
            listaInstituicoesEm2012[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 12 :
            listaInstituicoesEm2012[idDaInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"] += noDePublicacoes
            listaInstituicoesEm2012[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 13 :
            listaInstituicoesEm2012[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"] += noDePublicacoes
            listaInstituicoesEm2012[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
    elif anoPublicacao == 2013 :
        if idDaDisciplina == 1 :
            listaInstituicoesEm2013[idDaInstituicao]["Publicacoes_Disciplina_Biologia"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Biologia"] += noDePublicacoes
            listaInstituicoesEm2013[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 2 :
            listaInstituicoesEm2013[idDaInstituicao]["Publicacoes_Disciplina_Biotecnologia"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Biotecnologia"] += noDePublicacoes
            listaInstituicoesEm2013[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 3 :
            listaInstituicoesEm2013[idDaInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"] += noDePublicacoes
            listaInstituicoesEm2013[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 4 :
            listaInstituicoesEm2013[idDaInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"] += noDePublicacoes
            listaInstituicoesEm2013[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 5 :
            listaInstituicoesEm2013[idDaInstituicao]["Publicacoes_Disciplina_Quimica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Quimica"] += noDePublicacoes
            listaInstituicoesEm2013[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 6 :
            listaInstituicoesEm2013[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"] += noDePublicacoes
            listaInstituicoesEm2013[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 7 :
            listaInstituicoesEm2013[idDaInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"] += noDePublicacoes
            listaInstituicoesEm2013[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 8 :
            listaInstituicoesEm2013[idDaInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"] += noDePublicacoes
            listaInstituicoesEm2013[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 9 :
            listaInstituicoesEm2013[idDaInstituicao]["Publicacoes_Disciplina_Humanas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Humanas"] += noDePublicacoes
            listaInstituicoesEm2013[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 10 :
            listaInstituicoesEm2013[idDaInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"] += noDePublicacoes
            listaInstituicoesEm2013[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 11 :
            listaInstituicoesEm2013[idDaInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"] += noDePublicacoes
            listaInstituicoesEm2013[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 12 :
            listaInstituicoesEm2013[idDaInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"] += noDePublicacoes
            listaInstituicoesEm2013[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 13 :
            listaInstituicoesEm2013[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"] += noDePublicacoes
            listaInstituicoesEm2013[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
    elif anoPublicacao == 2014 :
        if idDaDisciplina == 1 :
            listaInstituicoesEm2014[idDaInstituicao]["Publicacoes_Disciplina_Biologia"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Biologia"] += noDePublicacoes
            listaInstituicoesEm2014[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 2 :
            listaInstituicoesEm2014[idDaInstituicao]["Publicacoes_Disciplina_Biotecnologia"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Biotecnologia"] += noDePublicacoes
            listaInstituicoesEm2014[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 3 :
            listaInstituicoesEm2014[idDaInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"] += noDePublicacoes
            listaInstituicoesEm2014[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 4 :
            listaInstituicoesEm2014[idDaInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"] += noDePublicacoes
            listaInstituicoesEm2014[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 5 :
            listaInstituicoesEm2014[idDaInstituicao]["Publicacoes_Disciplina_Quimica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Quimica"] += noDePublicacoes
            listaInstituicoesEm2014[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 6 :
            listaInstituicoesEm2014[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"] += noDePublicacoes
            listaInstituicoesEm2014[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 7 :
            listaInstituicoesEm2014[idDaInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"] += noDePublicacoes
            listaInstituicoesEm2014[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 8 :
            listaInstituicoesEm2014[idDaInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"] += noDePublicacoes
            listaInstituicoesEm2014[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 9 :
            listaInstituicoesEm2014[idDaInstituicao]["Publicacoes_Disciplina_Humanas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Humanas"] += noDePublicacoes
            listaInstituicoesEm2014[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 10 :
            listaInstituicoesEm2014[idDaInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"] += noDePublicacoes
            listaInstituicoesEm2014[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 11 :
            listaInstituicoesEm2014[idDaInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"] += noDePublicacoes
            listaInstituicoesEm2014[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 12 :
            listaInstituicoesEm2014[idDaInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"] += noDePublicacoes
            listaInstituicoesEm2014[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 13 :
            listaInstituicoesEm2014[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"] += noDePublicacoes
            listaInstituicoesEm2014[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
    elif anoPublicacao == 2015 :
        if idDaDisciplina == 1 :
            listaInstituicoesEm2015[idDaInstituicao]["Publicacoes_Disciplina_Biologia"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Biologia"] += noDePublicacoes
            listaInstituicoesEm2015[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 2 :
            listaInstituicoesEm2015[idDaInstituicao]["Publicacoes_Disciplina_Biotecnologia"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Biotecnologia"] += noDePublicacoes
            listaInstituicoesEm2015[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 3 :
            listaInstituicoesEm2015[idDaInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"] += noDePublicacoes
            listaInstituicoesEm2015[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 4 :
            listaInstituicoesEm2015[idDaInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"] += noDePublicacoes
            listaInstituicoesEm2015[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 5 :
            listaInstituicoesEm2015[idDaInstituicao]["Publicacoes_Disciplina_Quimica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Quimica"] += noDePublicacoes
            listaInstituicoesEm2015[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 6 :
            listaInstituicoesEm2015[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"] += noDePublicacoes
            listaInstituicoesEm2015[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 7 :
            listaInstituicoesEm2015[idDaInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"] += noDePublicacoes
            listaInstituicoesEm2015[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 8 :
            listaInstituicoesEm2015[idDaInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"] += noDePublicacoes
            listaInstituicoesEm2015[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 9 :
            listaInstituicoesEm2015[idDaInstituicao]["Publicacoes_Disciplina_Humanas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Humanas"] += noDePublicacoes
            listaInstituicoesEm2015[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 10 :
            listaInstituicoesEm2015[idDaInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"] += noDePublicacoes
            listaInstituicoesEm2015[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 11 :
            listaInstituicoesEm2015[idDaInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"] += noDePublicacoes
            listaInstituicoesEm2015[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 12 :
            listaInstituicoesEm2015[idDaInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"] += noDePublicacoes
            listaInstituicoesEm2015[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
        elif idDaDisciplina == 13 :
            listaInstituicoesEm2015[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"] += noDePublicacoes
            listaInstituicoesEm2015[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes
            listaInstituicoesTotal[idDaInstituicao]["Total_Publicacoes"] += noDePublicacoes


filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final") )
if not os.path.exists(filepath):
    os.makedirs(filepath)

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes") )
if not os.path.exists(filepath):
    os.makedirs(filepath)

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", "Publicacoes_Instituicoes_2010.tsv"))
f = open(filepath, "w")
f.write(
    "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(

        "ID_da_instituicao",
        "nome_da_instituicao",
        "ID_da_microregiao",
        "ID_da_mesoregiao",
        "ID_do_estado",

        "Publicacoes_Disciplina_Biologia",
        "Publicacoes_Disciplina_Biotecnologia",
        "Publicacoes_Disciplina_Especialidades_Medicas",
        "Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica",
        "Publicacoes_Disciplina_Quimica",

        "Publicacoes_Disciplina_Ciencias_da_Natureza",
        "Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao",
        "Publicacoes_Disciplina_Pesquisas_Neurologicas",
        "Publicacoes_Disciplina_Humanas",
        "Publicacoes_Disciplina_Doencas_Infecciosas",

        "Publicacoes_Disciplina_Matematica_e_Fisica",
        "Publicacoes_Disciplina_Profissionais_da_Saude",
        "Publicacoes_Disciplina_Ciencias_Sociais",
        "Total_Publicacoes"

    )
)

for idDeInstituicao in listaInstituicoesEm2010:
    f.write(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(

            idDeInstituicao, 
            listaInstituicoesEm2010[idDeInstituicao]["nome_da_instituicao"],
            listaInstituicoesEm2010[idDeInstituicao]["ID_da_microregiao"],
            listaInstituicoesEm2010[idDeInstituicao]["ID_da_mesoregiao"],
            listaInstituicoesEm2010[idDeInstituicao]["ID_do_estado"],
            
            listaInstituicoesEm2010[idDeInstituicao]["Publicacoes_Disciplina_Biologia"],
            listaInstituicoesEm2010[idDeInstituicao]["Publicacoes_Disciplina_Biotecnologia"],
            listaInstituicoesEm2010[idDeInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"],
            listaInstituicoesEm2010[idDeInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"],
            listaInstituicoesEm2010[idDeInstituicao]["Publicacoes_Disciplina_Quimica"],
            
            listaInstituicoesEm2010[idDeInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"],
            listaInstituicoesEm2010[idDeInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"],
            listaInstituicoesEm2010[idDeInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"],
            listaInstituicoesEm2010[idDeInstituicao]["Publicacoes_Disciplina_Humanas"],
            listaInstituicoesEm2010[idDeInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"],
            
            listaInstituicoesEm2010[idDeInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"],
            listaInstituicoesEm2010[idDeInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"],
            listaInstituicoesEm2010[idDeInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"],
            listaInstituicoesEm2010[idDeInstituicao]["Total_Publicacoes"]

        )
    
    )

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", "Publicacoes_Instituicoes_2011.tsv"))
f = open(filepath, "w")
f.write(
    "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(

        "ID_da_instituicao",
        "nome_da_instituicao",
        "ID_da_microregiao",
        "ID_da_mesoregiao",
        "ID_do_estado",

        "Publicacoes_Disciplina_Biologia",
        "Publicacoes_Disciplina_Biotecnologia",
        "Publicacoes_Disciplina_Especialidades_Medicas",
        "Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica",
        "Publicacoes_Disciplina_Quimica",

        "Publicacoes_Disciplina_Ciencias_da_Natureza",
        "Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao",
        "Publicacoes_Disciplina_Pesquisas_Neurologicas",
        "Publicacoes_Disciplina_Humanas",
        "Publicacoes_Disciplina_Doencas_Infecciosas",

        "Publicacoes_Disciplina_Matematica_e_Fisica",
        "Publicacoes_Disciplina_Profissionais_da_Saude",
        "Publicacoes_Disciplina_Ciencias_Sociais",
        "Total_Publicacoes"

    )
)

for idDeInstituicao in listaInstituicoesEm2011:
    f.write(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(

            idDeInstituicao, 
            listaInstituicoesEm2011[idDeInstituicao]["nome_da_instituicao"],
            listaInstituicoesEm2011[idDeInstituicao]["ID_da_microregiao"],
            listaInstituicoesEm2011[idDeInstituicao]["ID_da_mesoregiao"],
            listaInstituicoesEm2011[idDeInstituicao]["ID_do_estado"],
            
            listaInstituicoesEm2011[idDeInstituicao]["Publicacoes_Disciplina_Biologia"],
            listaInstituicoesEm2011[idDeInstituicao]["Publicacoes_Disciplina_Biotecnologia"],
            listaInstituicoesEm2011[idDeInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"],
            listaInstituicoesEm2011[idDeInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"],
            listaInstituicoesEm2011[idDeInstituicao]["Publicacoes_Disciplina_Quimica"],
            
            listaInstituicoesEm2011[idDeInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"],
            listaInstituicoesEm2011[idDeInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"],
            listaInstituicoesEm2011[idDeInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"],
            listaInstituicoesEm2011[idDeInstituicao]["Publicacoes_Disciplina_Humanas"],
            listaInstituicoesEm2011[idDeInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"],
            
            listaInstituicoesEm2011[idDeInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"],
            listaInstituicoesEm2011[idDeInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"],
            listaInstituicoesEm2011[idDeInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"],
            listaInstituicoesEm2011[idDeInstituicao]["Total_Publicacoes"]

        )
    
    )

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", "Publicacoes_Instituicoes_2012.tsv"))
f = open(filepath, "w")
f.write(
    "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(

        "ID_da_instituicao",
        "nome_da_instituicao",
        "ID_da_microregiao",
        "ID_da_mesoregiao",
        "ID_do_estado",

        "Publicacoes_Disciplina_Biologia",
        "Publicacoes_Disciplina_Biotecnologia",
        "Publicacoes_Disciplina_Especialidades_Medicas",
        "Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica",
        "Publicacoes_Disciplina_Quimica",

        "Publicacoes_Disciplina_Ciencias_da_Natureza",
        "Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao",
        "Publicacoes_Disciplina_Pesquisas_Neurologicas",
        "Publicacoes_Disciplina_Humanas",
        "Publicacoes_Disciplina_Doencas_Infecciosas",

        "Publicacoes_Disciplina_Matematica_e_Fisica",
        "Publicacoes_Disciplina_Profissionais_da_Saude",
        "Publicacoes_Disciplina_Ciencias_Sociais",
        "Total_Publicacoes"

    )
)

for idDeInstituicao in listaInstituicoesEm2012:
    f.write(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(

            idDeInstituicao, 
            listaInstituicoesEm2012[idDeInstituicao]["nome_da_instituicao"],
            listaInstituicoesEm2012[idDeInstituicao]["ID_da_microregiao"],
            listaInstituicoesEm2012[idDeInstituicao]["ID_da_mesoregiao"],
            listaInstituicoesEm2012[idDeInstituicao]["ID_do_estado"],
            
            listaInstituicoesEm2012[idDeInstituicao]["Publicacoes_Disciplina_Biologia"],
            listaInstituicoesEm2012[idDeInstituicao]["Publicacoes_Disciplina_Biotecnologia"],
            listaInstituicoesEm2012[idDeInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"],
            listaInstituicoesEm2012[idDeInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"],
            listaInstituicoesEm2012[idDeInstituicao]["Publicacoes_Disciplina_Quimica"],
            
            listaInstituicoesEm2012[idDeInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"],
            listaInstituicoesEm2012[idDeInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"],
            listaInstituicoesEm2012[idDeInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"],
            listaInstituicoesEm2012[idDeInstituicao]["Publicacoes_Disciplina_Humanas"],
            listaInstituicoesEm2012[idDeInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"],
            
            listaInstituicoesEm2012[idDeInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"],
            listaInstituicoesEm2012[idDeInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"],
            listaInstituicoesEm2012[idDeInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"],
            listaInstituicoesEm2012[idDeInstituicao]["Total_Publicacoes"]

        )
    
    )

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", "Publicacoes_Instituicoes_2013.tsv"))
f = open(filepath, "w")
f.write(
    "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(

        "ID_da_instituicao",
        "nome_da_instituicao",
        "ID_da_microregiao",
        "ID_da_mesoregiao",
        "ID_do_estado",

        "Publicacoes_Disciplina_Biologia",
        "Publicacoes_Disciplina_Biotecnologia",
        "Publicacoes_Disciplina_Especialidades_Medicas",
        "Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica",
        "Publicacoes_Disciplina_Quimica",

        "Publicacoes_Disciplina_Ciencias_da_Natureza",
        "Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao",
        "Publicacoes_Disciplina_Pesquisas_Neurologicas",
        "Publicacoes_Disciplina_Humanas",
        "Publicacoes_Disciplina_Doencas_Infecciosas",

        "Publicacoes_Disciplina_Matematica_e_Fisica",
        "Publicacoes_Disciplina_Profissionais_da_Saude",
        "Publicacoes_Disciplina_Ciencias_Sociais",
        "Total_Publicacoes"

    )
)

for idDeInstituicao in listaInstituicoesEm2013:
    f.write(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(

            idDeInstituicao, 
            listaInstituicoesEm2013[idDeInstituicao]["nome_da_instituicao"],
            listaInstituicoesEm2013[idDeInstituicao]["ID_da_microregiao"],
            listaInstituicoesEm2013[idDeInstituicao]["ID_da_mesoregiao"],
            listaInstituicoesEm2013[idDeInstituicao]["ID_do_estado"],
            
            listaInstituicoesEm2013[idDeInstituicao]["Publicacoes_Disciplina_Biologia"],
            listaInstituicoesEm2013[idDeInstituicao]["Publicacoes_Disciplina_Biotecnologia"],
            listaInstituicoesEm2013[idDeInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"],
            listaInstituicoesEm2013[idDeInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"],
            listaInstituicoesEm2013[idDeInstituicao]["Publicacoes_Disciplina_Quimica"],
            
            listaInstituicoesEm2013[idDeInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"],
            listaInstituicoesEm2013[idDeInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"],
            listaInstituicoesEm2013[idDeInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"],
            listaInstituicoesEm2013[idDeInstituicao]["Publicacoes_Disciplina_Humanas"],
            listaInstituicoesEm2013[idDeInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"],
            
            listaInstituicoesEm2013[idDeInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"],
            listaInstituicoesEm2013[idDeInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"],
            listaInstituicoesEm2013[idDeInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"],
            listaInstituicoesEm2013[idDeInstituicao]["Total_Publicacoes"]

        )
    
    )

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", "Publicacoes_Instituicoes_2014.tsv"))
f = open(filepath, "w")
f.write(
    "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(

        "ID_da_instituicao",
        "nome_da_instituicao",
        "ID_da_microregiao",
        "ID_da_mesoregiao",
        "ID_do_estado",

        "Publicacoes_Disciplina_Biologia",
        "Publicacoes_Disciplina_Biotecnologia",
        "Publicacoes_Disciplina_Especialidades_Medicas",
        "Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica",
        "Publicacoes_Disciplina_Quimica",

        "Publicacoes_Disciplina_Ciencias_da_Natureza",
        "Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao",
        "Publicacoes_Disciplina_Pesquisas_Neurologicas",
        "Publicacoes_Disciplina_Humanas",
        "Publicacoes_Disciplina_Doencas_Infecciosas",

        "Publicacoes_Disciplina_Matematica_e_Fisica",
        "Publicacoes_Disciplina_Profissionais_da_Saude",
        "Publicacoes_Disciplina_Ciencias_Sociais",
        "Total_Publicacoes"

    )
)

for idDeInstituicao in listaInstituicoesEm2014:
    f.write(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(

            idDeInstituicao, 
            listaInstituicoesEm2014[idDeInstituicao]["nome_da_instituicao"],
            listaInstituicoesEm2014[idDeInstituicao]["ID_da_microregiao"],
            listaInstituicoesEm2014[idDeInstituicao]["ID_da_mesoregiao"],
            listaInstituicoesEm2014[idDeInstituicao]["ID_do_estado"],
            
            listaInstituicoesEm2014[idDeInstituicao]["Publicacoes_Disciplina_Biologia"],
            listaInstituicoesEm2014[idDeInstituicao]["Publicacoes_Disciplina_Biotecnologia"],
            listaInstituicoesEm2014[idDeInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"],
            listaInstituicoesEm2014[idDeInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"],
            listaInstituicoesEm2014[idDeInstituicao]["Publicacoes_Disciplina_Quimica"],
            
            listaInstituicoesEm2014[idDeInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"],
            listaInstituicoesEm2014[idDeInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"],
            listaInstituicoesEm2014[idDeInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"],
            listaInstituicoesEm2014[idDeInstituicao]["Publicacoes_Disciplina_Humanas"],
            listaInstituicoesEm2014[idDeInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"],
            
            listaInstituicoesEm2014[idDeInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"],
            listaInstituicoesEm2014[idDeInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"],
            listaInstituicoesEm2014[idDeInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"],
            listaInstituicoesEm2014[idDeInstituicao]["Total_Publicacoes"]

        )
    
    )

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", "Publicacoes_Instituicoes_2015.tsv"))
f = open(filepath, "w")
f.write(
    "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(

        "ID_da_instituicao",
        "nome_da_instituicao",
        "ID_da_microregiao",
        "ID_da_mesoregiao",
        "ID_do_estado",

        "Publicacoes_Disciplina_Biologia",
        "Publicacoes_Disciplina_Biotecnologia",
        "Publicacoes_Disciplina_Especialidades_Medicas",
        "Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica",
        "Publicacoes_Disciplina_Quimica",

        "Publicacoes_Disciplina_Ciencias_da_Natureza",
        "Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao",
        "Publicacoes_Disciplina_Pesquisas_Neurologicas",
        "Publicacoes_Disciplina_Humanas",
        "Publicacoes_Disciplina_Doencas_Infecciosas",

        "Publicacoes_Disciplina_Matematica_e_Fisica",
        "Publicacoes_Disciplina_Profissionais_da_Saude",
        "Publicacoes_Disciplina_Ciencias_Sociais",
        "Total_Publicacoes"

    )
)

for idDeInstituicao in listaInstituicoesEm2015:
    f.write(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(

            idDeInstituicao, 
            listaInstituicoesEm2015[idDeInstituicao]["nome_da_instituicao"],
            listaInstituicoesEm2015[idDeInstituicao]["ID_da_microregiao"],
            listaInstituicoesEm2015[idDeInstituicao]["ID_da_mesoregiao"],
            listaInstituicoesEm2015[idDeInstituicao]["ID_do_estado"],
            
            listaInstituicoesEm2015[idDeInstituicao]["Publicacoes_Disciplina_Biologia"],
            listaInstituicoesEm2015[idDeInstituicao]["Publicacoes_Disciplina_Biotecnologia"],
            listaInstituicoesEm2015[idDeInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"],
            listaInstituicoesEm2015[idDeInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"],
            listaInstituicoesEm2015[idDeInstituicao]["Publicacoes_Disciplina_Quimica"],
            
            listaInstituicoesEm2015[idDeInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"],
            listaInstituicoesEm2015[idDeInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"],
            listaInstituicoesEm2015[idDeInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"],
            listaInstituicoesEm2015[idDeInstituicao]["Publicacoes_Disciplina_Humanas"],
            listaInstituicoesEm2015[idDeInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"],
            
            listaInstituicoesEm2015[idDeInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"],
            listaInstituicoesEm2015[idDeInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"],
            listaInstituicoesEm2015[idDeInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"],
            listaInstituicoesEm2015[idDeInstituicao]["Total_Publicacoes"]

        )
    
    )

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "instituicoes", "Publicacoes_Instituicoes_Total.tsv"))
f = open(filepath, "w")
f.write(
    "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(

        "ID_da_instituicao",
        "nome_da_instituicao",
        "ID_da_microregiao",
        "ID_da_mesoregiao",
        "ID_do_estado",

        "Publicacoes_Disciplina_Biologia",
        "Publicacoes_Disciplina_Biotecnologia",
        "Publicacoes_Disciplina_Especialidades_Medicas",
        "Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica",
        "Publicacoes_Disciplina_Quimica",

        "Publicacoes_Disciplina_Ciencias_da_Natureza",
        "Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao",
        "Publicacoes_Disciplina_Pesquisas_Neurologicas",
        "Publicacoes_Disciplina_Humanas",
        "Publicacoes_Disciplina_Doencas_Infecciosas",

        "Publicacoes_Disciplina_Matematica_e_Fisica",
        "Publicacoes_Disciplina_Profissionais_da_Saude",
        "Publicacoes_Disciplina_Ciencias_Sociais",
        "Total_Publicacoes"

    )
)

for idDeInstituicao in listaInstituicoesTotal:
    f.write(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(

            idDeInstituicao, 
            listaInstituicoesTotal[idDeInstituicao]["nome_da_instituicao"],
            listaInstituicoesTotal[idDeInstituicao]["ID_da_microregiao"],
            listaInstituicoesTotal[idDeInstituicao]["ID_da_mesoregiao"],
            listaInstituicoesTotal[idDeInstituicao]["ID_do_estado"],
            
            listaInstituicoesTotal[idDeInstituicao]["Publicacoes_Disciplina_Biologia"],
            listaInstituicoesTotal[idDeInstituicao]["Publicacoes_Disciplina_Biotecnologia"],
            listaInstituicoesTotal[idDeInstituicao]["Publicacoes_Disciplina_Especialidades_Medicas"],
            listaInstituicoesTotal[idDeInstituicao]["Publicacoes_Disciplina_Engenharias_Civil_Mecanica_e_Quimica"],
            listaInstituicoesTotal[idDeInstituicao]["Publicacoes_Disciplina_Quimica"],
            
            listaInstituicoesTotal[idDeInstituicao]["Publicacoes_Disciplina_Ciencias_da_Natureza"],
            listaInstituicoesTotal[idDeInstituicao]["Publicacoes_Disciplina_Engenharia_Eletrica_e_Ciencias_da_Computacao"],
            listaInstituicoesTotal[idDeInstituicao]["Publicacoes_Disciplina_Pesquisas_Neurologicas"],
            listaInstituicoesTotal[idDeInstituicao]["Publicacoes_Disciplina_Humanas"],
            listaInstituicoesTotal[idDeInstituicao]["Publicacoes_Disciplina_Doencas_Infecciosas"],
            
            listaInstituicoesTotal[idDeInstituicao]["Publicacoes_Disciplina_Matematica_e_Fisica"],
            listaInstituicoesTotal[idDeInstituicao]["Publicacoes_Disciplina_Profissionais_da_Saude"],
            listaInstituicoesTotal[idDeInstituicao]["Publicacoes_Disciplina_Ciencias_Sociais"],
            listaInstituicoesTotal[idDeInstituicao]["Total_Publicacoes"]

        )
    
    )

f.close()

##
#   Criação dos modelos de indices socio-economicos
##

#   + Microrregiões

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'microrregioes', "PIBdeMicrorregioes_filtrado.tsv"))
with open(filepath, 'r', encoding='utf-8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaPIBdeMicrorregioes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'microrregioes', "ESTABELECIMENTOS_MICRORREGIOES_2010_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2010 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'microrregioes', "ESTABELECIMENTOS_MICRORREGIOES_2011_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2011 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'microrregioes', "ESTABELECIMENTOS_MICRORREGIOES_2012_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2012 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'microrregioes', "ESTABELECIMENTOS_MICRORREGIOES_2013_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2013 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'microrregioes', "ESTABELECIMENTOS_MICRORREGIOES_2014_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2014 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'microrregioes', "ESTABELECIMENTOS_MICRORREGIOES_2015_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMicrorregioes2015 = list(dictReader)
    
    indicesIndicadores = []

    for field in dictReader.fieldnames:
        indicesIndicadores.append( field )
    indicesEstabelecimentos = copy.copy(listaEstabelecimentosMicrorregioes2010[0])
    del indicesEstabelecimentos[ "ID_da_microregiao" ]
    for field in indicesEstabelecimentos.keys() :
        indicesIndicadores.append( field )


listaIndicadores2010 = OrderedDict()
listaIndicadores2011 = OrderedDict()
listaIndicadores2012 = OrderedDict()
listaIndicadores2013 = OrderedDict()
listaIndicadores2014 = OrderedDict()
listaIndicadores2015 = OrderedDict()
listaIndicadoresTotal = OrderedDict()

for microrregiao in listaPIBdeMicrorregioes :

    ano = int(microrregiao["Ano"])
    idMicrorregiao = int(microrregiao["ID_da_microregiao"])
		
    nomeMicrorregiao = microrregiao["Nome_da_microregiao"]
    valorAgropecuaria = float(microrregiao["Valor_bruto_agropecuaria"])
    valorIndustria = float(microrregiao["Valor_bruto_industria"])
    valorServicos = float(microrregiao["Valor_bruto_servicos"])
    valorAdministracao = float(microrregiao["Valor_bruto_administracao"])
    valorTotal = float(microrregiao["Valor_bruto_total"])
    impostos = float(microrregiao["Impostos"])
    pib = float(microrregiao["PIB"])
    populacao = float(microrregiao["Populacao"])
    pibPerCapita = float(microrregiao["PIB_per_capita"])
    
    dictIndicadoresNovo = dict(
        nome_da_microrregiao = nomeMicrorregiao,
        Valor_bruto_agropecuaria = valorAgropecuaria,
        Valor_bruto_industria = valorIndustria,
        Valor_bruto_servicos = valorServicos,
        Valor_bruto_administracao = valorAdministracao,
        Valor_bruto_total = valorTotal,
        Impostos = impostos,
        PIB = pib,
        Populacao = populacao,
        PIB_per_capita = pibPerCapita
    )

    estabelecimentosMicrorregiao = []

    if ano == 2010 :
        for dictEstabelecimentos in listaEstabelecimentosMicrorregioes2010 :
            if int(dictEstabelecimentos["ID_da_microregiao"]) == idMicrorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_da_microregiao"]

                if idMicrorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMicrorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMicrorregiao].keys() :
                        if chave != "nome_da_microrregiao" :
                            listaIndicadoresTotal[idMicrorregiao][chave] = float(listaIndicadoresTotal[idMicrorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2010[idMicrorregiao] = copy.copy(dictNovaEntrada)
                break

    elif ano == 2011 :
        for dictEstabelecimentos in listaEstabelecimentosMicrorregioes2011 :
            if int(dictEstabelecimentos["ID_da_microregiao"]) == idMicrorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_da_microregiao"]

                if idMicrorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMicrorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMicrorregiao].keys() :
                        if chave != "nome_da_microrregiao" :
                            listaIndicadoresTotal[idMicrorregiao][chave] = float(listaIndicadoresTotal[idMicrorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2011[idMicrorregiao] = copy.copy(dictNovaEntrada)
                break

    elif ano == 2012 :
        for dictEstabelecimentos in listaEstabelecimentosMicrorregioes2012 :
            if int(dictEstabelecimentos["ID_da_microregiao"]) == idMicrorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_da_microregiao"]

                if idMicrorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMicrorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMicrorregiao].keys() :
                        if chave != "nome_da_microrregiao" :
                            listaIndicadoresTotal[idMicrorregiao][chave] = float(listaIndicadoresTotal[idMicrorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2012[idMicrorregiao] = copy.copy(dictNovaEntrada)
                break
            
    elif ano == 2013 :
        for dictEstabelecimentos in listaEstabelecimentosMicrorregioes2013 :
            if int(dictEstabelecimentos["ID_da_microregiao"]) == idMicrorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_da_microregiao"]

                if idMicrorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMicrorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMicrorregiao].keys() :
                        if chave != "nome_da_microrregiao" :
                            listaIndicadoresTotal[idMicrorregiao][chave] = float(listaIndicadoresTotal[idMicrorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2013[idMicrorregiao] = copy.copy(dictNovaEntrada)
                break
            
    elif ano == 2014 :
        for dictEstabelecimentos in listaEstabelecimentosMicrorregioes2014 :
            if int(dictEstabelecimentos["ID_da_microregiao"]) == idMicrorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_da_microregiao"]

                if idMicrorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMicrorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMicrorregiao].keys() :
                        if chave != "nome_da_microrregiao" :
                            listaIndicadoresTotal[idMicrorregiao][chave] = float(listaIndicadoresTotal[idMicrorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2014[idMicrorregiao] = copy.copy(dictNovaEntrada)
                break
            
    elif ano == 2015 :
        for dictEstabelecimentos in listaEstabelecimentosMicrorregioes2015 :
            if int(dictEstabelecimentos["ID_da_microregiao"]) == idMicrorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_da_microregiao"]

                if idMicrorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMicrorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMicrorregiao].keys() :
                        if chave != "nome_da_microrregiao" :
                            listaIndicadoresTotal[idMicrorregiao][chave] = float(listaIndicadoresTotal[idMicrorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2015[idMicrorregiao] = copy.copy(dictNovaEntrada)
                break
    
filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes") )
if not os.path.exists(filepath):
    os.makedirs(filepath)

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "microrregioes") )
if not os.path.exists(filepath):
    os.makedirs(filepath)

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "microrregioes", "Indicadores_Socioeconomicos_2010.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_da_microregiao\t"
for idMicrorregiao in listaIndicadores2010 :
    for index in listaIndicadores2010[idMicrorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMicrorregiao in listaIndicadores2010:
    
    row = str(idMicrorregiao) + "\t"

    for indice in listaIndicadores2010[idMicrorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "microrregioes", "Indicadores_Socioeconomicos_2010.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_da_microregiao\t"
for idMicrorregiao in listaIndicadores2010 :
    for index in listaIndicadores2010[idMicrorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMicrorregiao in listaIndicadores2010:
    
    row = str(idMicrorregiao) + "\t"

    for indice in listaIndicadores2010[idMicrorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "microrregioes", "Indicadores_Socioeconomicos_2011.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_da_microregiao\t"
for idMicrorregiao in listaIndicadores2011 :
    for index in listaIndicadores2011[idMicrorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMicrorregiao in listaIndicadores2011:
    
    row = str(idMicrorregiao) + "\t"

    for indice in listaIndicadores2011[idMicrorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "microrregioes", "Indicadores_Socioeconomicos_2012.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_da_microregiao\t"
for idMicrorregiao in listaIndicadores2012 :
    for index in listaIndicadores2012[idMicrorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMicrorregiao in listaIndicadores2012:
    
    row = str(idMicrorregiao) + "\t"

    for indice in listaIndicadores2012[idMicrorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "microrregioes", "Indicadores_Socioeconomicos_2013.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_da_microregiao\t"
for idMicrorregiao in listaIndicadores2013 :
    for index in listaIndicadores2013[idMicrorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMicrorregiao in listaIndicadores2013:
    
    row = str(idMicrorregiao) + "\t"

    for indice in listaIndicadores2013[idMicrorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "microrregioes", "Indicadores_Socioeconomicos_2014.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_da_microregiao\t"
for idMicrorregiao in listaIndicadores2014 :
    for index in listaIndicadores2014[idMicrorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMicrorregiao in listaIndicadores2014:
    
    row = str(idMicrorregiao) + "\t"

    for indice in listaIndicadores2014[idMicrorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "microrregioes", "Indicadores_Socioeconomicos_2015.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_da_microregiao\t"
for idMicrorregiao in listaIndicadores2015 :
    for index in listaIndicadores2015[idMicrorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMicrorregiao in listaIndicadores2015:
    
    row = str(idMicrorregiao) + "\t"

    for indice in listaIndicadores2015[idMicrorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "microrregioes", "Indicadores_Socioeconomicos_Total.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_da_microregiao\t"
for idMicrorregiao in listaIndicadoresTotal :
    for index in listaIndicadoresTotal[idMicrorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMicrorregiao in listaIndicadoresTotal:
    
    row = str(idMicrorregiao) + "\t"

    for indice in listaIndicadoresTotal[idMicrorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

#   + Mesorregiões

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'mesorregioes', "PIBdeMesorregioes_filtrado.tsv"))
with open(filepath, 'r', encoding='utf-8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaPIBdeMesorregioes = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'mesorregioes', "ESTABELECIMENTOS_MESORREGIOES_2010_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2010 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'mesorregioes', "ESTABELECIMENTOS_MESORREGIOES_2011_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2011 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'mesorregioes', "ESTABELECIMENTOS_MESORREGIOES_2012_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2012 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'mesorregioes', "ESTABELECIMENTOS_MESORREGIOES_2013_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2013 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'mesorregioes', "ESTABELECIMENTOS_MESORREGIOES_2014_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2014 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'mesorregioes', "ESTABELECIMENTOS_MESORREGIOES_2015_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosMesorregioes2015 = list(dictReader)
    
    indicesIndicadores = []

    for field in dictReader.fieldnames:
        indicesIndicadores.append( field )
    indicesEstabelecimentos = copy.copy(listaEstabelecimentosMesorregioes2010[0])
    del indicesEstabelecimentos[ "ID_da_mesoregiao" ]
    for field in indicesEstabelecimentos.keys() :
        indicesIndicadores.append( field )


listaIndicadores2010 = OrderedDict()
listaIndicadores2011 = OrderedDict()
listaIndicadores2012 = OrderedDict()
listaIndicadores2013 = OrderedDict()
listaIndicadores2014 = OrderedDict()
listaIndicadores2015 = OrderedDict()
listaIndicadoresTotal = OrderedDict()

for mesorregiao in listaPIBdeMesorregioes :

    ano = int(mesorregiao["Ano"])
    idMesorregiao = int(mesorregiao["ID_da_mesoregiao"])
		
    nomeMicrorregiao = mesorregiao["Nome_da_mesoregiao"]
    valorAgropecuaria = float(mesorregiao["Valor_bruto_agropecuaria"])
    valorIndustria = float(mesorregiao["Valor_bruto_industria"])
    valorServicos = float(mesorregiao["Valor_bruto_servicos"])
    valorAdministracao = float(mesorregiao["Valor_bruto_administracao"])
    valorTotal = float(mesorregiao["Valor_bruto_total"])
    impostos = float(mesorregiao["Impostos"])
    pib = float(mesorregiao["PIB"])
    populacao = float(mesorregiao["Populacao"])
    pibPerCapita = float(mesorregiao["PIB_per_capita"])
    
    dictIndicadoresNovo = dict(
        nome_da_mesorregiao = nomeMicrorregiao,
        Valor_bruto_agropecuaria = valorAgropecuaria,
        Valor_bruto_industria = valorIndustria,
        Valor_bruto_servicos = valorServicos,
        Valor_bruto_administracao = valorAdministracao,
        Valor_bruto_total = valorTotal,
        Impostos = impostos,
        PIB = pib,
        Populacao = populacao,
        PIB_per_capita = pibPerCapita
    )

    estabelecimentosMicrorregiao = []

    if ano == 2010 :
        for dictEstabelecimentos in listaEstabelecimentosMesorregioes2010 :
            if int(dictEstabelecimentos["ID_da_mesoregiao"]) == idMesorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_da_mesoregiao"]

                if idMesorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMesorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMesorregiao].keys() :
                        if chave != "nome_da_mesorregiao" :
                            listaIndicadoresTotal[idMesorregiao][chave] = float(listaIndicadoresTotal[idMesorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2010[idMesorregiao] = copy.copy(dictNovaEntrada)
                break

    elif ano == 2011 :
        for dictEstabelecimentos in listaEstabelecimentosMesorregioes2011 :
            if int(dictEstabelecimentos["ID_da_mesoregiao"]) == idMesorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_da_mesoregiao"]

                if idMesorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMesorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMesorregiao].keys() :
                        if chave != "nome_da_mesorregiao" :
                            listaIndicadoresTotal[idMesorregiao][chave] = float(listaIndicadoresTotal[idMesorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2011[idMesorregiao] = copy.copy(dictNovaEntrada)
                break

    elif ano == 2012 :
        for dictEstabelecimentos in listaEstabelecimentosMesorregioes2012 :
            if int(dictEstabelecimentos["ID_da_mesoregiao"]) == idMesorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_da_mesoregiao"]

                if idMesorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMesorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMesorregiao].keys() :
                        if chave != "nome_da_mesorregiao" :
                            listaIndicadoresTotal[idMesorregiao][chave] = float(listaIndicadoresTotal[idMesorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2012[idMesorregiao] = copy.copy(dictNovaEntrada)
                break
            
    elif ano == 2013 :
        for dictEstabelecimentos in listaEstabelecimentosMesorregioes2013 :
            if int(dictEstabelecimentos["ID_da_mesoregiao"]) == idMesorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_da_mesoregiao"]

                if idMesorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMesorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMesorregiao].keys() :
                        if chave != "nome_da_mesorregiao" :
                            listaIndicadoresTotal[idMesorregiao][chave] = float(listaIndicadoresTotal[idMesorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2013[idMesorregiao] = copy.copy(dictNovaEntrada)
                break
            
    elif ano == 2014 :
        for dictEstabelecimentos in listaEstabelecimentosMesorregioes2014 :
            if int(dictEstabelecimentos["ID_da_mesoregiao"]) == idMesorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_da_mesoregiao"]

                if idMesorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMesorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMesorregiao].keys() :
                        if chave != "nome_da_mesorregiao" :
                            listaIndicadoresTotal[idMesorregiao][chave] = float(listaIndicadoresTotal[idMesorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2014[idMesorregiao] = copy.copy(dictNovaEntrada)
                break
            
    elif ano == 2015 :
        for dictEstabelecimentos in listaEstabelecimentosMesorregioes2015 :
            if int(dictEstabelecimentos["ID_da_mesoregiao"]) == idMesorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_da_mesoregiao"]

                if idMesorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMesorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMesorregiao].keys() :
                        if chave != "nome_da_mesorregiao" :
                            listaIndicadoresTotal[idMesorregiao][chave] = float(listaIndicadoresTotal[idMesorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2015[idMesorregiao] = copy.copy(dictNovaEntrada)
                break
    
filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes") )
if not os.path.exists(filepath):
    os.makedirs(filepath)

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "mesorregioes") )
if not os.path.exists(filepath):
    os.makedirs(filepath)

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "mesorregioes", "Indicadores_Socioeconomicos_2010.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_da_mesoregiao\t"
for idMesorregiao in listaIndicadores2010 :
    for index in listaIndicadores2010[idMesorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMesorregiao in listaIndicadores2010:
    
    row = str(idMesorregiao) + "\t"

    for indice in listaIndicadores2010[idMesorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "mesorregioes", "Indicadores_Socioeconomicos_2010.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_da_mesoregiao\t"
for idMesorregiao in listaIndicadores2010 :
    for index in listaIndicadores2010[idMesorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMesorregiao in listaIndicadores2010:
    
    row = str(idMesorregiao) + "\t"

    for indice in listaIndicadores2010[idMesorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "mesorregioes", "Indicadores_Socioeconomicos_2011.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_da_mesoregiao\t"
for idMesorregiao in listaIndicadores2011 :
    for index in listaIndicadores2011[idMesorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMesorregiao in listaIndicadores2011:
    
    row = str(idMesorregiao) + "\t"

    for indice in listaIndicadores2011[idMesorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "mesorregioes", "Indicadores_Socioeconomicos_2012.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_da_mesoregiao\t"
for idMesorregiao in listaIndicadores2012 :
    for index in listaIndicadores2012[idMesorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMesorregiao in listaIndicadores2012:
    
    row = str(idMesorregiao) + "\t"

    for indice in listaIndicadores2012[idMesorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "mesorregioes", "Indicadores_Socioeconomicos_2013.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_da_mesoregiao\t"
for idMesorregiao in listaIndicadores2013 :
    for index in listaIndicadores2013[idMesorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMesorregiao in listaIndicadores2013:
    
    row = str(idMesorregiao) + "\t"

    for indice in listaIndicadores2013[idMesorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "mesorregioes", "Indicadores_Socioeconomicos_2014.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_da_mesoregiao\t"
for idMesorregiao in listaIndicadores2014 :
    for index in listaIndicadores2014[idMesorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMesorregiao in listaIndicadores2014:
    
    row = str(idMesorregiao) + "\t"

    for indice in listaIndicadores2014[idMesorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "mesorregioes", "Indicadores_Socioeconomicos_2015.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_da_mesoregiao\t"
for idMesorregiao in listaIndicadores2015 :
    for index in listaIndicadores2015[idMesorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMesorregiao in listaIndicadores2015:
    
    row = str(idMesorregiao) + "\t"

    for indice in listaIndicadores2015[idMesorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "mesorregioes", "Indicadores_Socioeconomicos_Total.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_da_mesoregiao\t"
for idMesorregiao in listaIndicadoresTotal :
    for index in listaIndicadoresTotal[idMesorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMesorregiao in listaIndicadoresTotal:
    
    row = str(idMesorregiao) + "\t"

    for indice in listaIndicadoresTotal[idMesorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

#   + Estados

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'estados', "PIBdeEstados_filtrado.tsv"))
with open(filepath, 'r', encoding='utf-8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaPIBdeEstados = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'estados', "ESTABELECIMENTOS_ESTADOS_2010_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2010 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'estados', "ESTABELECIMENTOS_ESTADOS_2011_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2011 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'estados', "ESTABELECIMENTOS_ESTADOS_2012_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2012 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'estados', "ESTABELECIMENTOS_ESTADOS_2013_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2013 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'estados', "ESTABELECIMENTOS_ESTADOS_2014_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2014 = list(dictReader)

filepath = path.abspath( path.join(pathBase, "..", "dados", "3_filtragem_dos_dados", 'estados', "ESTABELECIMENTOS_ESTADOS_2015_FILTRADO.tsv"))
with open(filepath, 'r', encoding='utf8') as file:
    dictReader = DictReader(file, delimiter='\t')
    listaEstabelecimentosEstados2015 = list(dictReader)
    
    indicesIndicadores = []

    for field in dictReader.fieldnames:
        indicesIndicadores.append( field )
    indicesEstabelecimentos = copy.copy(listaEstabelecimentosEstados2010[0])
    del indicesEstabelecimentos[ "ID_do_estado" ]
    for field in indicesEstabelecimentos.keys() :
        indicesIndicadores.append( field )


listaIndicadores2010 = OrderedDict()
listaIndicadores2011 = OrderedDict()
listaIndicadores2012 = OrderedDict()
listaIndicadores2013 = OrderedDict()
listaIndicadores2014 = OrderedDict()
listaIndicadores2015 = OrderedDict()
listaIndicadoresTotal = OrderedDict()

for mesorregiao in listaPIBdeEstados :

    ano = int(mesorregiao["Ano"])
    idMesorregiao = int(mesorregiao["ID_do_estado"])
		
    nomeMicrorregiao = mesorregiao["Nome_do_estado"]
    valorAgropecuaria = float(mesorregiao["Valor_bruto_agropecuaria"])
    valorIndustria = float(mesorregiao["Valor_bruto_industria"])
    valorServicos = float(mesorregiao["Valor_bruto_servicos"])
    valorAdministracao = float(mesorregiao["Valor_bruto_administracao"])
    valorTotal = float(mesorregiao["Valor_bruto_total"])
    impostos = float(mesorregiao["Impostos"])
    pib = float(mesorregiao["PIB"])
    populacao = float(mesorregiao["Populacao"])
    pibPerCapita = float(mesorregiao["PIB_per_capita"])
    
    dictIndicadoresNovo = dict(
        nome_do_estado = nomeMicrorregiao,
        Valor_bruto_agropecuaria = valorAgropecuaria,
        Valor_bruto_industria = valorIndustria,
        Valor_bruto_servicos = valorServicos,
        Valor_bruto_administracao = valorAdministracao,
        Valor_bruto_total = valorTotal,
        Impostos = impostos,
        PIB = pib,
        Populacao = populacao,
        PIB_per_capita = pibPerCapita
    )

    estabelecimentosMicrorregiao = []

    if ano == 2010 :
        for dictEstabelecimentos in listaEstabelecimentosEstados2010 :
            if int(dictEstabelecimentos["ID_do_estado"]) == idMesorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_do_estado"]

                if idMesorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMesorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMesorregiao].keys() :
                        if chave != "nome_do_estado" :
                            listaIndicadoresTotal[idMesorregiao][chave] = float(listaIndicadoresTotal[idMesorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2010[idMesorregiao] = copy.copy(dictNovaEntrada)
                break

    elif ano == 2011 :
        for dictEstabelecimentos in listaEstabelecimentosEstados2011 :
            if int(dictEstabelecimentos["ID_do_estado"]) == idMesorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_do_estado"]

                if idMesorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMesorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMesorregiao].keys() :
                        if chave != "nome_do_estado" :
                            listaIndicadoresTotal[idMesorregiao][chave] = float(listaIndicadoresTotal[idMesorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2011[idMesorregiao] = copy.copy(dictNovaEntrada)
                break

    elif ano == 2012 :
        for dictEstabelecimentos in listaEstabelecimentosEstados2012 :
            if int(dictEstabelecimentos["ID_do_estado"]) == idMesorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_do_estado"]

                if idMesorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMesorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMesorregiao].keys() :
                        if chave != "nome_do_estado" :
                            listaIndicadoresTotal[idMesorregiao][chave] = float(listaIndicadoresTotal[idMesorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2012[idMesorregiao] = copy.copy(dictNovaEntrada)
                break
            
    elif ano == 2013 :
        for dictEstabelecimentos in listaEstabelecimentosEstados2013 :
            if int(dictEstabelecimentos["ID_do_estado"]) == idMesorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_do_estado"]

                if idMesorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMesorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMesorregiao].keys() :
                        if chave != "nome_do_estado" :
                            listaIndicadoresTotal[idMesorregiao][chave] = float(listaIndicadoresTotal[idMesorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2013[idMesorregiao] = copy.copy(dictNovaEntrada)
                break
            
    elif ano == 2014 :
        for dictEstabelecimentos in listaEstabelecimentosEstados2014 :
            if int(dictEstabelecimentos["ID_do_estado"]) == idMesorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_do_estado"]

                if idMesorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMesorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMesorregiao].keys() :
                        if chave != "nome_do_estado" :
                            listaIndicadoresTotal[idMesorregiao][chave] = float(listaIndicadoresTotal[idMesorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2014[idMesorregiao] = copy.copy(dictNovaEntrada)
                break
            
    elif ano == 2015 :
        for dictEstabelecimentos in listaEstabelecimentosEstados2015 :
            if int(dictEstabelecimentos["ID_do_estado"]) == idMesorregiao :

                dictNovaEntrada = dictIndicadoresNovo | dictEstabelecimentos
                del dictNovaEntrada["ID_do_estado"]

                if idMesorregiao not in listaIndicadoresTotal :
                    listaIndicadoresTotal[idMesorregiao] = copy.copy(dictNovaEntrada)
                else :
                    for chave in listaIndicadoresTotal[idMesorregiao].keys() :
                        if chave != "nome_do_estado" :
                            listaIndicadoresTotal[idMesorregiao][chave] = float(listaIndicadoresTotal[idMesorregiao][chave]) + float(dictNovaEntrada[chave])
                
                listaIndicadores2015[idMesorregiao] = copy.copy(dictNovaEntrada)
                break
    
filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes") )
if not os.path.exists(filepath):
    os.makedirs(filepath)

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "estados") )
if not os.path.exists(filepath):
    os.makedirs(filepath)

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "estados", "Indicadores_Socioeconomicos_2010.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_do_estado\t"
for idMesorregiao in listaIndicadores2010 :
    for index in listaIndicadores2010[idMesorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMesorregiao in listaIndicadores2010:
    
    row = str(idMesorregiao) + "\t"

    for indice in listaIndicadores2010[idMesorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "estados", "Indicadores_Socioeconomicos_2010.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_do_estado\t"
for idMesorregiao in listaIndicadores2010 :
    for index in listaIndicadores2010[idMesorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMesorregiao in listaIndicadores2010:
    
    row = str(idMesorregiao) + "\t"

    for indice in listaIndicadores2010[idMesorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "estados", "Indicadores_Socioeconomicos_2011.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_do_estado\t"
for idMesorregiao in listaIndicadores2011 :
    for index in listaIndicadores2011[idMesorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMesorregiao in listaIndicadores2011:
    
    row = str(idMesorregiao) + "\t"

    for indice in listaIndicadores2011[idMesorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "estados", "Indicadores_Socioeconomicos_2012.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_do_estado\t"
for idMesorregiao in listaIndicadores2012 :
    for index in listaIndicadores2012[idMesorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMesorregiao in listaIndicadores2012:
    
    row = str(idMesorregiao) + "\t"

    for indice in listaIndicadores2012[idMesorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "estados", "Indicadores_Socioeconomicos_2013.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_do_estado\t"
for idMesorregiao in listaIndicadores2013 :
    for index in listaIndicadores2013[idMesorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMesorregiao in listaIndicadores2013:
    
    row = str(idMesorregiao) + "\t"

    for indice in listaIndicadores2013[idMesorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "estados", "Indicadores_Socioeconomicos_2014.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_do_estado\t"
for idMesorregiao in listaIndicadores2014 :
    for index in listaIndicadores2014[idMesorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMesorregiao in listaIndicadores2014:
    
    row = str(idMesorregiao) + "\t"

    for indice in listaIndicadores2014[idMesorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "estados", "Indicadores_Socioeconomicos_2015.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_do_estado\t"
for idMesorregiao in listaIndicadores2015 :
    for index in listaIndicadores2015[idMesorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMesorregiao in listaIndicadores2015:
    
    row = str(idMesorregiao) + "\t"

    for indice in listaIndicadores2015[idMesorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()

filepath = path.abspath( path.join(pathBase, "..", "dados", "4_final", "regioes", "estados", "Indicadores_Socioeconomicos_Total.tsv"))
f = open(filepath, "w", encoding='utf-8')

headers = "ID_do_estado\t"
for idMesorregiao in listaIndicadoresTotal :
    for index in listaIndicadoresTotal[idMesorregiao].keys() :
        headers += index + "\t"
    break
headers = headers[:-1] + "\n"

f.write(headers)

for idMesorregiao in listaIndicadoresTotal:
    
    row = str(idMesorregiao) + "\t"

    for indice in listaIndicadoresTotal[idMesorregiao].values():
        row += str(indice) + "\t"
    
    row = row[:-1] + "\n"

    f.write(row)

f.close()
