# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA
# TEM 'SILVA' NO NOME.

nome = input('Digite seu nome: ').strip().lower()

silva = 'silva' in nome.split()

print(f'Seu nome tem Silva? {silva}')