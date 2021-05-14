'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão.'''

print('-=' * 15)
print('    DEZ TERMOS DE UMA PA')
print('-=' * 15)
a1 = int(input('Primeiro termo de uma PA: '))
r = int(input('Razão de uma PA: '))
a10 = a1 + 9 * r

print('PA = { ', end='')
for i in range(a1, a10 + r, r):
    print(f'{i}', end=', ')
print('}')