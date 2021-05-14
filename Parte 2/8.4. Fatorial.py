'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120'''

print('-=' * 15)
print('          FATORIAL')
print('-=' * 15)

n = int(input('Digite um número e descubra o seu fatorial: '))
c = n
fatorial = 1

'''print(f'{n}! = ', end=(''))
while c > 0:
    print(c, end=(''))
    if c > 1:
        print(' x ', end=(''))
    else:
        print(' = ', end=(''))
    fatorial = fatorial * c
    c = c - 1
print(fatorial)'''

print(f'{n}! = ', end=(''))
for c in range(n, 0, -1):
    print(c, end=(''))
    if c > 1:
        print(' x ', end=(''))
    else:
        print(' = ', end=(''))
    fatorial *= c
    c -= 1
print(fatorial)