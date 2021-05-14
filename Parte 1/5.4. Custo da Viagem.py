# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM.
# CALCULE O PREÇO DA PASSAGEM, COBRANDO R$ 0,50 POR KM PARA VIAGEM DE ATÉ 200 KM E
# R$ 0,45 PARA VIAGENS MAIS LONGAS.

from time import sleep

km = int(input('Distância da viagem em Km: '))
print('Calculando o preço da passagem...')
sleep(1)

if km <= 200:
    preco1 = km * 0.50
    print(f'Preço da passagem = R$ {preco1:.2f}')
else:
    preco2 = km * 0.45
    print(f'Preço da passagem = R$ {preco2:.2f}')