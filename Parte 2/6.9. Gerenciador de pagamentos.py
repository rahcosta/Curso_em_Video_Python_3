# ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO,
# CONSIDERANDO O SEU PREÇO NORMAL E A CONDIÇÃO DE PAGAMENTO:
# À VISTA DINHEIRO / CHEQUE: 10% DE DESCONTO
# À VISTA NO CARTÃO: 5% DE DESCONTO
# EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
# 3X OU MAIS NO CARTÃO: 20% DE JUROS

produto = float(input('Preço do produto: R$ '))

print('-' * 40)
print('Escolha a forma de pagamento:')
print('[1] à vista em Dinheiro ou Cheque \n[2] à vista no Cartão de crédito')
print('[3] em até 2x no Cartão de crédito \n[4] em 3x ou mais no Cartão de crédito')
escolha = int(input('Forma de pagamento: '))
if escolha == 4:
    parcelas = int(input('Quantas parcelas? '))
print('-' * 40)

dc = produto - (produto * 0.10)
cartao = produto - (produto * 0.05)
parcelado3 = produto + (produto * 0.20)

if escolha == 1:
    print('Forma de pagamento escolhida: à vista em Dinheiro ou Cheque')
    print(f'\033[34mDesconto de 10%\033[m \nTotal a ser pago: R$ {dc:.2f}')
elif escolha == 2:
    print('Forma de pagamento escolhida: à vista no Cartão de crédito')
    print(f'\033[34mDesconto de 5%\033[m \nTotal a ser pago: R$ {cartao:.2f}')
elif escolha == 3:
    print('Forma de pagamento escolhida: parcelado em até 2x no Cartão de crédito')
    print(f'Valor das parcelas: R$ {produto / 2} \nTotal a ser pago: R$ {produto:.2f}')
elif escolha == 4:
    print('Forma de pagamento escolhida: parcelado em 3x ou mais no Cartão de crédito')
    print(f'\033[31mJuros de 20%\033[m')
    print(f'Valor das parcelas: R$ {parcelado3 / parcelas:.2f} \nTotal a ser pago: R$ {parcelado3:.2f}')
else:
    print('OPÇÃO INVÁLIDA!')