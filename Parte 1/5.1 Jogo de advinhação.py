# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR PENSAR EM UM NÚMERO INTEIRO ENTRE 0 E 5
# E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR.
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU.

from random import randint
from time import sleep

print('-' * 50)
print('Vamos ver se você é bom em advinhação? \nEu estou pensando em um número de 0 a 5.')
print('-' * 50)
computador = randint(0, 5)
usuario = int(input('Qual número eu pensei? '))

print('\033[7;30mProcessando...\033[m')
sleep(1)

if usuario == computador:
    print('\033[1;34mParabéns, você acertou!\033[m')
else:
    print(f'\033[1;31mErrou! Eu estava pensando no número {computador}\033[m')