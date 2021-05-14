# CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ.

from random import choice
from time import sleep

nome = 'JOKENPÔÔÔÔÔ'
print('=' * 50)
print(f'{nome:^45}')
print('=' * 50)

print('''Será que você consegue me vencer no Jokenpô? 
Para jogar escolha uma das seguintes opções:
[1] Pedra
[2] Papel
[3] Tesoura''')
escolha = int(input('Sua escolha é... '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔÔÔÔÔ')

lista = [1, 2, 3]
computador = choice(lista)

if escolha == 1 and computador == 3:
    print('\033[34mJOGADOR: PEDRA')
    print('\033[31mCOMPUTADOR: TESOURA.\033[m')
    print('\033[34mParabéns, você ganhou!')
elif escolha == 3 and computador == 1:
    print(f'\033[34mJOGADOR: TESOURA\033[m')
    print('\033[31mCOMPUTADOR: PEDRA.\033[m')
    print('\033[7;30mO computador ganhou, hahahahaha!\033[m')
elif escolha == 2 and computador == 1:
    print('\033[34mVJOGADOR: PAPEL')
    print('\033[31mCOMPUTADOR: PEDRA.\033[m')
    print('\033[34mParabéns, você ganhou!')
elif escolha == 1 and computador == 2:
    print('\033[34mJOGADOR: PEDRA\033[m')
    print('\033[31mCOMPUTADOR: PAPEL.\033[m')
    print('\033[7;30mO computador ganhou, hahahahaha!\033[m')
elif escolha == 3 and computador == 2:
    print('\033[34mJOGADOR: TESOURA\033[m')
    print('\033[31mCOMPUTADOR: PAPEL.\033[m')
    print('\033[34mParabéns, você ganhou!')
elif escolha == 2 and computador == 3:
    print('\033[34mJOGADOR: PAPEL\033[m')
    print('\033[31mCOMPUTADOR: TESOURA.\033[m')
    print('\033[7;30mO computador ganhou, hahahahaha!\033[m')
elif escolha == 1 and computador == 1:
    print('\033[34mJOGADOR: PEDRA\033[m')
    print('\033[31mCOMPUTADOR: PEDRA.\033[m')
    print('\033[1mEmpatamos. Jogue novamente!')
elif escolha == 2 and computador == 2:
    print('\033[34mJOGADOR: PAPEL\033[m')
    print('\033[31mCOMPUTADOR: PAPEL.\033[m')
    print('\033[1mEmpatamos. Jogue novamente!')
elif escolha == 3 and computador == 3:
    print('\033[34mJOGADOR: TESOURA\033[m')
    print('\033[31mCOMPUTADOR: TESOURA.\033[m')
    print('\033[1mEmpatamos. Jogue novamente!')
else:
    print('Opção inválida!')