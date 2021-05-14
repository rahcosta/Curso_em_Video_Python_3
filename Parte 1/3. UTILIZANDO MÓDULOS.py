#import math
from math import sqrt, ceil

num = float(input('Digite um número: '))
#raizQ = math.sqrt(num)
raizQ = sqrt(num)

#print(f'A raiz de {num} é igual a {math.ceil(raizQ)}')
print(f'A raiz de {num} é igual a {ceil(raizQ)}')

# ceil arredonda para cima.
# floor arredonda para baixo