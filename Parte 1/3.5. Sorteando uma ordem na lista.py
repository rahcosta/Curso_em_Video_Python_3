# O MESMO PROFESSOR DO EXERCÍCIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DOS TRABALHOS
# DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA.

import random

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]

random.shuffle(lista) #essa função embaralha a lista

print(f'Ordem de apresentação: \n{lista}')