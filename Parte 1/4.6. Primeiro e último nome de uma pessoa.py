# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA
# O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE.
# EX: ANA MARIA DE SOUZA
# PRIMEIRO = ANA
# ÚLTIMO = SOUZA

nome = str(input('Digite seu nome completo: ')).strip().lower()
n = nome.split()

print(f'Seu primeiro nome é: {n[0].title()}')
print(f'Seu último nome é: {n[len(n) -1].title()}')