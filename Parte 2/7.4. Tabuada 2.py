'''Refaça o exercício da parte 1 tabuada, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''

n = int(input('Digite um número inteiro: '))

print('-=' * 10)
print(f'TABUADA DO NÚMERO {n}')
print('-=' * 10)

for i in range(1, 11):
    m = i * n
    print(f'{n} x {i:^2} =  {m}')
print('-=' * 10)