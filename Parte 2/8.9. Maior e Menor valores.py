'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve
perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

cont = soma = media = maior = menor = 0

usuario = 's'

while usuario in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    usuario = input('Deseja digitar mais valores? [S/N] ').strip().lower()[0]
media = soma / cont
print(f'''Você digitou {cont} número(s) e a média foi {media:.2f}.
O maior número é {maior} e o menor é {menor}''')
