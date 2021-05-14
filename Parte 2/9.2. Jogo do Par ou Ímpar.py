'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

cont = soma = 0

print('-=' * 20)
print('       JOGO DE PAR OU ÍMPAR')
print('-=' * 20)

while True:
    escolha = input('Você quer PAR ou ÍMPAR [P/I]: ').strip().lower()[0]
    n = int(input('Digite um número de 1 a 20: '))
    computador = randint(1, 20)
    soma = n + computador
    if escolha == 'p':
        print('-' * 40)
        print(f'Você jogou {n} e o computador jogou {computador}.')
        print('-' * 40)
        if soma % 2 == 0:
            print(f'{n} + {computador} = {soma} -> PAR. \nParabéns, você ganhou!')
            cont += 1
            print('Vamos jogar novamente...')
        else:
            print(f'{n} + {computador} = {soma} -> ÍMPAR. \nVocê perdeu!')
            break
    elif escolha == 'i':
        print('-' * 40)
        print(f'Você jogou {n} e o computador jogou {computador}.')
        print('-' * 40)
        if soma % 2 != 0:
            print(f'{n} + {computador} = {soma} -> ÍMPAR. \nParabéns, você ganhou!')
            cont += 1
            print('Vamos jogar novamente...')
        else:
            print(f'{n} + {computador} = {soma} -> PAR. \nVocê perdeu!')
            break
print(f'Número de vitórias = {cont}')
print('-' * 30)
print('END GAME...')
