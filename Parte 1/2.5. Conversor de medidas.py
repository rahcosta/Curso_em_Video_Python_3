# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros:

valor = float(input(f'Digite um valor em metros = '))
km = valor * 0.001
hm = valor * 0.01
dam = valor * 0.1
d = valor * 10
cent = valor * 100
mili = valor * 1000

print(f'QUILÔMETRO = {km}km \nHECTÔMETRO = {hm}hm \nDECÂMETRO = {dam:.1f}dam \nDECÍMETRO = {d:.0f}dm \nCENTÍMETROS = {cent:.0f}cm \nMILÍMETROS = {mili:.0f}mm')