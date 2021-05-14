# ESCREVA UM PROGRAMA QUE LEIA 2 NÚMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA UMA MENSAGEM:
# O PRIMEIRO VALOR É MAIOR;
# O SEGUNDO VALOR É MAIOR;
# NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro valor é maior.')
elif n1 < n2:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior. Os dois são iguais.')