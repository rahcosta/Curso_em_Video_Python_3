# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# O NOME COM TODAS AS LETRAS MAIÚSCULAS;
# O NOME COM TODAS AS LETRAS MINÚSCULAS;
# QUANTAS LETRAS AO TODO, SEM CONSIDERAR OS ESPAÇOS;
# QUANTAS LETRAS TEM O PRIMEIRO NOME?
# raissa costa alencar

nome = input('Digite seu nome completo: ').strip()

noSpace = len(nome) - nome.count(' ')
letras = nome.find(' ')
separa = nome.split()

print(f'Todo o nome maiúsculo: {nome.upper()}')
print(f'Todo o nome minúsculo: {nome.lower()}')
print(f'Quantas letras tem ao todo sem considerar os espaços? {noSpace}')
# print(f'Quantas letras tem o primeiro nome? {letras}')
print(f'Quantas letras tem o primeiro nome? {separa[0], len(separa[0])}')