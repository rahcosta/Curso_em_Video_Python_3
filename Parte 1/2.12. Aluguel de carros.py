# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO
# E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO.
# CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$ 60 POR DIA E R$ 0,15 POR KM RODADO.

dias = int(input('Quantos dias o automóvel foi alugado: '))
km = float(input('Quantos Km foram rodados: '))

precoFinal = (dias * 60) + (km * 0.15)

print(f'O total a pagar = R$ {precoFinal:.2f}')