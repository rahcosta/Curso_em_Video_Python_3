# REFAÇA O DESAFIO ANALISANDO TRIÂNGULOS, ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO
# DE TRIÂNGULO SERÁ FORMADO:
# EQUILÁTERO: TODOS OS LADOS IGUAIS
# ISÓCELES: DOIS LADOS IGUAIS
# ESCALENO: TODOS OS LADOS DIFERENTES

print('\033[4m-\033[m' * 25)
print('Analizador de triângulos')
print('\033[4m-\033[m' * 25)
reta1 = int(input('Digite a primeira reta: '))
reta2 = int(input('Digite a segunda reta: '))
reta3 = int(input('Digite a terceira reta: '))

# Se forma um trinângulo:
if ((reta1 + reta2) > reta3) and ((reta1 + reta3) > reta2) and ((reta2 + reta3) > reta1):
    print(f'\033[1;34mAs retas {reta1, reta2, reta3} podem formar um triângulo', end=(''))

    # O tipo de triângulo:
    if reta1 == reta2 == reta3:
        print(' do tipo EQUILÁTERO.')
    elif reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
        print(' do tipo ESCALENO.')
    else:
        print(' do tipo ISÓCELES.')
else:
    print(f'\033[31mAs retas {reta1, reta2, reta3} não cumprem a desigualdade trinagular, logo, \nnão podem formar um triângulo')
