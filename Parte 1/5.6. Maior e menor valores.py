# FAÇA UM PROGRAMA QUE LEIA 3 NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR.

print('Digite os números a serem analizados: ')
n1 = float(input())
n2 = float(input())
n3 = float(input())

# verificando quem é o maior:
if (n1 > n2) and (n1 > n3):
    maior = n1
elif n2 > n3:
    maior = n2
else:
    maior = n3

# verificando quem é o menor:
if (n1 < n2) and (n1 < n3):
    menor = n1
elif (n2 < n3):
    menor = n2
else:
    menor = n3

print(f'O menor número é {menor}')
print(f'O maior número é {maior}')