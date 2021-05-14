'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

print('-=' * 10)
print('CADASTRO DE PRODUTOS')
print('-=' * 10)

total = mais_mil = barato = cont = 0
produto_barato = ''

while True:
    nome = input('Nome do Produto: ').strip()
    preco = float(input('Preço R$: '))
    cont += 1
    if preco > 1000:
        mais_mil += 1
    total += preco
    if cont == 1 or preco < barato:
        barato = preco
        produto_barato = nome
    resp = ' '
    while resp not in 'sn':
        resp = input('Deseja continuar? [S/N] ').strip().lower()[0]
    if resp == 'n':
        break
print('-' * 15)
print(f'Total a pagar = R$ {total:.2f}')
print(f'Quantidade de produtos que custam mais de R$ 1000.00 reais = {mais_mil}')
print(f'O produto mais barato da lista foi {produto_barato} e custou R$ {barato:.2f} reais')