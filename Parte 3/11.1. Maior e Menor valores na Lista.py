'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

num = list()
for cont in range(1, 6):
    num.append(int(input(f'Digite o {cont}º valor: ')))

max = max(num)
min = min(num)

print()
print(f'A lista criada contém os seguintes números -> {num}')
print(f'O \033[34mMAIOR\033[m número da lista é {max} e está na(s) posição(ões)', end=' ')
for i, n in enumerate(num):
    if n == max:
        print(f'{i+1}...', end='')

print(f'\nO \033[31mMENOR\033[m número da lista é {min} e está na(s) posição(ões)', end=' ')
for i, n in enumerate(num):
    if n == min:
        print(f'{i+1}...', end='')