# FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO.
from datetime import date

ano = int(input('Digite o ano a ser analizado ou digite 0 para analizar o ano atual: '))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano de {ano} é BISSEXTO')
else:
    print(f'O ano de {ano} não é bissexto')