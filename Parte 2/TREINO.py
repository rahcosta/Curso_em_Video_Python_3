# an = a1 + (n - 1) * r

primeiro = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))

'''for i in range(primeiro, 11 * r, r):
    print(i, end=' ')'''

cont = 2
print('PA de 10 termos = { ', end='')
print(primeiro, end=', ')
while cont <= 10:
    pa = primeiro + (cont - 1) * r
    print(pa, end='')
    if cont < 10:
        print(', ', end='')
    cont += 1
print(' }')