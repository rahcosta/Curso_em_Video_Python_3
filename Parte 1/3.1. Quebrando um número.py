# CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA
# A SUA PORÇÃO INTEIRA.
# DIGITE UM NÚMERO: 6.127
# O NÚMERO 6.127 TEM A PARTE INTEIRA 6

import math

num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {math.trunc(num)}') #poderia usar int(num)