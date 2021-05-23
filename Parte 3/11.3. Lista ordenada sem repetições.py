'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

lista = list()

for cont in range(0, 5):
    n = (int(input(f'Digite um valor: ')))
    if cont == 0 or n > lista[-1]: # último valor da lista
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(lista): #verifica da primeira até a última posição
            if n <= lista[posicao]:
                lista.insert(posicao, n) #na posição coloca o valor n
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1
print(f'Lista -> {lista}')
