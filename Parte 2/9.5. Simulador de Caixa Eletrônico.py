'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('-=' * 15)
print('  CAIXA ELETRÔNICO BANCO RCA')
print('-=' * 15)

valor = int(input('Digite o valor que deseja sacar: R$ '))
total = valor
cedula = 50
total_ced = 0
while True:
    if total >= cedula:
        total -= cedula
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédula(s) de R$ {cedula:.2f} reais')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_ced = 0
        if total == 0:
            break
print('-=' * 15)
print('Agradecemos pela preferência! \nVolte sempre!')