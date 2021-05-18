'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

numero = (int(input('Digite o primeiro número: ')),
          int(input('Digite o segundo número: ')),
          int(input('Digite o terceiro número: ')),
          int(input('Digite o quarto número: ')))
print()
print((f'-> Os números digitados foram \033[34m{numero}\033[m.'))
print(f'-> O número 9 apareceu \033[34m{numero.count(9)}\033[m vez(es).')
print(f'-> O número 3 apareceu primeiramente em qual posição?', end=' ')
if 3 in numero:
    print(f'\033[34m{numero.index(3) + 1}ª\033[m')
else:
    print('\033[31mO número 3 não foi digitado.\033[m')

print('-> Os números pares são: \033[34m', end=' ')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')

