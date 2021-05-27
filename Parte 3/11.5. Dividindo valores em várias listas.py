'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os
valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

lista_geral = list()
pares = []
impares = []

while True:
    n = int(input('Digite um número: '))
    lista_geral.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = input('Quer continuar? [S/N] ').strip().lower()[0]
    while resp not in 'sn':
        resp = input('Resposta inválida. Quer continuar? [S/N] ').strip().lower()[0]
    if resp == 'n':
        break
print(f'\nLISTA GERAL: {lista_geral}'
      f'\nPARES: {pares}'
      f'\nIMPARES: {impares}')
