'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

genero = input('Digite seu gênero [M/F]: ').upper().strip()[0] #se digitar masculino só será considerado o M.
while genero != 'M' and genero != 'F': #while genero not in 'MmFf':
    genero = input('Dado inválido! Por favor, digite novamente [M/F]: ').strip().upper()[0]
print(f'Gênero {genero} registrado com sucesso.')
