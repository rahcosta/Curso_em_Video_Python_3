'''Uma lista pode ser criada da seguinte forma:
num = [] ou
num = list()

num = (2, 5, 9, 1) Tupla
 num[2] = 3 Tupla é imutável'''

num = [2, 5, 9, 1]
print(num)
num[2] = 3 # Listas são mutáveis!
print(num)
num.append(7) # adiciona 7 a lista
print(num)
num.sort() # coloca em ordem
print(num)
num.sort(reverse=True) # coloca na ordem inversa
print(num)
print(f'A lista {num} tem {len(num)} elementos.')
num.insert(2, 0) # na posição 2, inserir 0 .
print(num)
num.pop() # deleta o elemento da última posição
print(num)
num.pop(2) # deleta o elemento da posição 2
print(num)
num.insert(2, 2)
print(num)
num.remove(2) # deleta a primeira ocorrência do elemento 2
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')

print()
print('-> Ligando uma lista a outra:')
a = [2, 3, 4, 7]
b = a
b[2] = 8 # modifica tanto a lista b quanto a lista a
print(f'Lista A: {a}')
print(f'Lista B: {b}')

print()
print('-> Fazendo uma cópia da lista a:')
a = [2, 3, 4, 7]
b = a[:] # pega todos os elementos da lista a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
