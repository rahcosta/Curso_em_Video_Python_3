# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE 3 RETAS E DIGA AO USUÁRIO SE ELAS
# PODEM OU NÃO FORMAR UM TRIÂNGULO.

print('\033[4m-\033[m' * 25)
print('Analizador de triângulos')
print('\033[4m-\033[m' * 25)
reta1 = int(input('Digite a primeira reta: '))
reta2 = int(input('Digite a segunda reta: '))
reta3 = int(input('Digite a terceira reta: '))

if ((reta1 + reta2) > reta3) and ((reta1 + reta3) > reta2) and ((reta2 + reta3) > reta1):
    print(f'\033[1;34mAs retas {reta1, reta2, reta3} podem formar um triângulo')
else:
    print(f'\033[31mAs retas {reta1, reta2, reta3} não cumprem a desigualdade trinagular, logo, \nnão podem formar um triângulo')
