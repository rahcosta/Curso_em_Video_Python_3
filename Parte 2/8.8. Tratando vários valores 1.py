'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag).'''

cont = 0
soma = 0

n = int(input('Digite um número: '))

while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite mais um número: '))
print(f'Você digitou {cont} números e a soma entre eles é igual a {soma}.')