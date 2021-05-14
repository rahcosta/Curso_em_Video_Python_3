# Cie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada:

import math

x = float(input('Digite um número: '))
dobro = x * 2
triplo = x * 3
#raizQ = x ** (1/2) ou pow(x, (1/2))

print(f'Dobro: {dobro} \nTriplo: {triplo} \nRaiz Quadrada: {math.sqrt(x):.2f}')