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
#   Juncao de modelos
#
##

##
#   
##