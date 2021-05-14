'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
e que se encontram no intervalo de 1 até 500.'''

soma = 0
cont = 0

print(f'\033[4mMúltiplos de 3 | Soma\033[m')

for i in range(1, 501, 2):
    if i % 3 == 0:
        soma = soma + i #soma += i
        cont = cont + 1 #cont += 1
        print(f'{i:^13}  | {soma:^5}')
print(f'CONTADOR = {cont}  SOMA = {soma}')
