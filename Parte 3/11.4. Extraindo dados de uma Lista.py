'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
cont = 0

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    resp = input('Deseja continuar? [S/N] ').strip().lower()[0]
    while resp not in 'sn':
        resp = input('Opção inválida! Deseja continuar? [S/N] ').strip().lower()[0]
    cont += 1
    if resp == 'n':
        break

lista.sort(reverse=True)

print(f'\nLista em ordem decrescente -> {lista}'
      f'\nForam digitados {cont} valores.') #poderia ter sido feito usando len(lista)

if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
