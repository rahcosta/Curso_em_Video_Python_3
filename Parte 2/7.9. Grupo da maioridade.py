'''Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade (21 anos) e quantas já são maiores.'''

import datetime
maior = 0
menor = 0

for pessoas in range(1, 8):
    nasc = int(input(f'Ano de nascimento da {pessoas}ª pessoa: '))
    idade = datetime.date.today().year - nasc
    if idade < 21:
        menor += 1
    else:
        maior += 1

print(f'\033[31m{menor} pessoa(s) não atingiu(ram) a maioridade de 21 anos.\033[m')
print(f'\033[34m{maior} pessoa(s) atingiu(ram) a maioridade de 21 anos.\033[m')
