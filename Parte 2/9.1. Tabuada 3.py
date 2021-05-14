'''Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

n = 0

print('-=' * 10)
print('      TABUADA')
print('-=' * 10)
while True:
    n = int(input('Digite um número inteiro: '))
    if n < 0:
        break
    for i in range(1, 11):
        m = i * n
        print(f'{n} x {i:^2} =  {m}')
    print('-=' * 10)
print('Programa encerrado!')
