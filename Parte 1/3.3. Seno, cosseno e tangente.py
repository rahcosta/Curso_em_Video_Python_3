# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO
# SENO, COSSENO E TANGENTE DESSE ÂNGULO.

import math

angulo = int(input('Digite o valor de um ângulo: '))

# Atenção: math.sin/cos/tan dão os valores em radianos, por isso eu preciso converter ângulo para radianos.

print(f'O seno do ângulo {angulo} é {math.sin(math.radians(angulo)):.2f}')
print(f'O cosseno do ângulo {angulo} é {math.cos(math.radians(angulo)):.2f}')
print(f'A tangente do ângulo {angulo} é {math.tan(math.radians(angulo)):.2f}')