# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. FAÇA UM
# PROGRAMA QUE O AJUDE, LENDO O NOME DOS ALUNOS E ESCREVENDO O NOME DO ESCOLHIDO.

import random

nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')

lista = [nome1, nome2, nome3, nome4]

print(f'O/A aluno/a escolhido/a foi: {random.choice(lista)}')