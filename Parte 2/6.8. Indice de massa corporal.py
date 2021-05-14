# DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA,
# CALCULE SEU IMC E MOSTRE SEU STATUS, DE ACORDO COM A TABELA ABAIXO:
# ABAIXO DE 18.5: ABAIXO DO PESO
# ENTRE 18.5 E 25: PESO IDEAL
# 25 ATÉ 30: SOBREPESO
# 30 ATÉ 40: OBESIDADE
# ACIMA DE 40: OBESIDADE MÓRBIDA

peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)


if imc < 18.5:
    print(f'IMC = {imc:.1f} \nVocê está ABAIXO DO PESO.')
elif imc < 26:
    print(f'IMC = {imc:.1f} \nVocê está no PESO IDEAL.')
elif imc < 31:
    print(f'IMC = {imc:.1f} \nVocê está com SOBREPESO.')
elif imc < 41:
    print(f'IMC = {imc:.1f} \nVocê está com OBESIDADE.')
else:
    print(f'IMC = {imc:.1f} \nVocê está no OBESIDADE MÓRBIDA.')