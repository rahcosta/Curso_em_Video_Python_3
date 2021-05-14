'''Refaça o exercício 7.6., lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print('-=' * 15)
print('    DEZ TERMOS DE UMA PA')
print('-=' * 15)
a1 = int(input('Primeiro termo de uma PA: '))
r = int(input('Razão de uma PA: '))
#a10 = a1 + 9 * r
termos = 2

print('PA = { ', end='')
print(a1, end=', ')
while termos <= 10:
    pa = a1 + (termos - 1) * r
    print(f'{pa}', end=' ')
    if termos < 10:
        print(', ', end='')
    termos += 1
print('}')
