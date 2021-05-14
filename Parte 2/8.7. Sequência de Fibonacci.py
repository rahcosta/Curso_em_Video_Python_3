'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci. Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8'''

'''Os números seguintes são sempre a soma dos dois números anteriores. 
Portanto, depois de 0 e 1, vêm 1, 2, 3, 5, 8, 13, 21, 34…'''

elementos = int(input('Quantos elementos da Seguência de Fibonacci deseja mostrar? '))
n1 = 1
anterior = 0
cont = 2
print('0, 1,', end=' ')
while cont < elementos:
    cont += 1
    n1 = n1 + anterior
    print(n1, end='')
    if cont < elementos:
        print(', ', end='')
    anterior = n1 - anterior
print(' FIM')
