# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS.
# CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE
# TINTA PINTA UMA ÁREA DE 2 METROS QUADRADOS:

largura = float(input('Largura: '))
altura = float(input('Altura: '))

area = largura * altura
tinta = area / 2

print(f'ÁREA: {area:.2f} m²')
print(f'A QUANTIDADE NECESSÁRIA DE TINTA É: {tinta:.2f} L')