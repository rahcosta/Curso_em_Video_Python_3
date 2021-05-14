# ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO. SE ELE ULTRAPASSAR 80 KM/H,
# MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO. A MULTA VAI CUSTAR 7,00 REAIS
# POR CADA KM ACIMA DO LIMITE.

from time import sleep

carro = int(input('Digite a velocidade detectada em Km: '))
print('Processando...')
sleep(1)

multa = (carro - 80) * 7

if carro > 80:
    print(f'A velocidade detectada foi maior do que 80 km/h, por isso o motorista receberá uma multa de R$ {abs(multa):.2f}')

print(f'Parabéns! Você estava dentro do limite permitido')