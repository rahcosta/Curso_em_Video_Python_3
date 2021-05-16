lanche = ('hamburguer', 'suco', 'pizza', 'pudim') # Não é necessário colocar parênteses
print(lanche[3])
print(lanche[1:3])

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print('-' * 30)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')
print('-' * 30)
for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')
print('Comi pra caramba!')
# Tuplas sãp imutáveis. Só posso mexer na atribuição inicial
# lanche[1] = 'refrigerante'

print(sorted(lanche)) # ordem alfabética
print(lanche)
print()

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5)) # mostra quantas vezes o número 5 apareceu
print(c.index(8)) # mostra a posição que o 8 se encontra.
print(c.index(2)) # indica a primeira ocorrência do 2
print(c.index(2,1)) # indica a posição da segunda ocorrência do 2

pessoa = ('Gustavo', 33, 'M', 99.88)
print(pessoa)
del(pessoa) # deleta a tupla
