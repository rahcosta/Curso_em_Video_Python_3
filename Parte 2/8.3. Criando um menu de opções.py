'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

print('-=' * 15)
print('          MENU')
print('-=' * 15)
valor1 = float(input('Digite um número: '))
valor2 = float(input('Digite mais um número: '))
usuario = 0

while usuario != 5:
    print()
    print('''O que você deseja fazer?
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    print('-' * 20)
    usuario = int(input('Sua escolha: '))
    print('-' * 20)

    if usuario == 1:
        somar = valor1 + valor2
        print(f'{valor1} + {valor2} = {somar}')
    elif usuario == 2:
        multiplicar = valor1 * valor2
        print(f'{valor1} x {valor2} = {multiplicar}')
    elif usuario == 3:
        if valor1 > valor2:
            maior = valor1
            menor = valor2
            print(f'O número {maior} é maior do que o número {menor}.')
        elif valor2 > valor1:
            maior = valor2
            menor = valor1
            print(f'O número {maior} é maior do que o número {menor}.')
        else:
            print('Os dois valores são iguais.')
    elif usuario == 4:
        valor1 = float(input('Digite um número: '))
        valor2 = float(input('Digite mais um número: '))
    elif usuario == 5:
        print('\033[7mFinalizando...\033[m')
        #print('Você saiu do programa.', end=(' '))
    else:
        print('Opção inválida!')

sleep(1)
print('Você saiu do programa. Volte sempre!')
