'''Melhore o exercício 8.5., perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('-=' * 15)
print('    TERMOS DE UMA PA')
print('-=' * 15)
a1 = int(input('Primeiro termo de uma PA: '))
r = int(input('Razão de uma PA: '))
#a10 = a1 + 9 * r
termos = 2
total = 0
mais = 10
print('PA = {', end=' ')
print(f'{a1}, ', end='')
while mais != 0:
    total += mais
    while termos <= total:
        pa = a1 + (termos - 1) * r
        print(pa, end='')
        if termos < total:
            print(', ', end='')
        else:
            print(' }', end=' ')
        termos += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
