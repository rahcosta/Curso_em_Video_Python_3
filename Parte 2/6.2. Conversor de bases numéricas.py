# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER
# QUAL SERÁ A BASE DE CONVERSÃO:
# 1 PARA BINÁRIO;
# 2 PARA OCTAL;
#3 PARA HEXADECIMAL.

n = int(input('Digite o número a ser convertido: '))
print('Escolha a base de conversão:')
print('[ 1 ] converter para BINÁRIO \n[ 2 ] converter para OCTAL \n[ 3 ] converter para HEXADECIMAL')
escolha = int(input('Sua opção: '))

if escolha == 1:
    print(f'O número {n} convertido para Binário corresponde a {bin(n)[2:]}')
elif escolha == 2:
    print(f'O número {n} convertido para Octal corresponde a {oct(n)[2:]}')
elif escolha == 3:
    print(f'O número {n} convertido para Hexadecimal corresponde a {hex(n)[2:]}')
else:
    print('Opção inválida. Tente novamente!')