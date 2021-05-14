# ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA.
# O PROGRAMA VAI PERGUNTAR: O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
# CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODERÁ EXCEDER 30% DO SALÁRIO OU ENTÃO
# O EMPRÉSTIMO SERÁ NEGADO.

print('-' * 62)
print('Para aprovarmos o empréstimo, responda o questionário abaixo:')
print('-' * 62)
casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o valor do salário do comprador? R$ '))
anos = int(input('Em quantos anos será pago? '))
prestacao = (casa / anos) / 12

if prestacao > salario * 0.30:
    print('\033[31mEMPRÉSTIMO NEGADO!')
else:
    print('\033[34mParabéns! Seu empréstimo foi APROVADO!\033[m')
    print(f'O valor das parcelas será de R$ {prestacao:.2f} pagos em {anos} anos.')