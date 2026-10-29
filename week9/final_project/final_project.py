'''
trabalho - analise de planilhas excel de investimentos da bolsa e opçoes do usuário,
para a bolsa será usado um API, classe investimentos

as opções consistem:
-analisar investimentos em geral
-analisar invvestimento especifico
-dados da empresa em geral
-dados de empresa especifico
-o quanto cresceu ou diminuiu em certo tempo 
-melhores resultados atuais
'''

import sys
import tabulate
import csv
import requests
import json

class Investimentos:
    def __init__(self):
        ...

url = 'https://api.nasa.gov/planetary/apod'
parametros = {'api_key':'Vygfq7dUd0ycAKYb5Eym09dAMyDVlBR49hi2M9Ar',
              'hd': True}

try:
    request = requests.get(url,params=parametros)
    request.raise_for_status()
    dados = request.json()
    print(dados['explanation'])
except requests.HTTPError:
    sys.exit('erro')    