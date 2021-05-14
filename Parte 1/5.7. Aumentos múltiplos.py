# ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO.
# PARA SALÁRIOS SUPERIORES A R$ 1.250,00, CALCULETE UM AUMENTO DE 10%.
# PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%.

salario = float(input('Qual é o salário do funcionário? R$ '))

if salario > 1250:
    aumento = (salario * 0.10) + salario
else:
    aumento = (salario * 0.15) + salario

print(f'O novo salário será de R$ {aumento:.2f}')