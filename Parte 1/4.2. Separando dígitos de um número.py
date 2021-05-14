# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA
# UM DOS DÍGITOS SEPARADOS.
# EX: DIGITE UM NÚMERO: 1834
# UNIDADE: 4
# DEZENA: 3
# CENTENA: 8
# MILHAR: 1

numero = int(input('Digite um número: '))

#n = str(numero)
#print(f'Unidade: {n[3]}')
#print(f'Dezena: {n[2]}')
#print(f'Centena: {n[1]}')
#print(f'Milhar: {n[0]}')

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')