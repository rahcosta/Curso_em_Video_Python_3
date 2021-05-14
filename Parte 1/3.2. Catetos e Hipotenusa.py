# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE
# DE UM TRIÂNGULO RETÂNGULO. CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.

import math

oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))

print(f'O comprimento da hipotenusa é {math.hypot(oposto, adjacente):.2f}')