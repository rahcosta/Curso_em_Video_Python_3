'''Melhore o jogo do exercício 5.1 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.'''

from random import randint
from time import sleep

print('-' * 50)
print('Vamos ver se você é bom em advinhação? \nEu estou pensando em um número entre 0 e 10.')
print('-' * 50)

palpites = 0

computador = randint(0, 10)
usuario = int(input('Qual número eu pensei? '))

print('\033[7mProcessando...\033[m')
sleep(1)

while usuario != computador:
    palpites += 1
    print('\033[1;31mErrou!\033[m', end=(' '))
    if usuario > computador:
        print('Pensei num número MENOR...')
    else:
        print('Pensei num número MAIOR...')
    usuario = int(input(f'Tente novamente: '))

print(f'''\033[1;34mParabéns, você acertou!\033[m
Você precisou de {palpites} tentativa(s) para acertar.''')
