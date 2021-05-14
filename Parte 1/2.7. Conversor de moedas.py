# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES
# ELA PODE COMPRAR:
# CONSIDERE US$ 1,00 = R$ 5,57

carteira = float(input('Digite quanto dinheiro tem na carteira: R$ '))

dolares = carteira / 5.57

print(f"Poderá comprar US$ {dolares:.2f}")