'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

somaIdade = 0
velho = 0
novas = 0

for pessoas in range(1, 5):
    print(f'-----DADOS DA {pessoas}ª PESSOA-----')
    nome = input('Nome: ').strip().lower()
    idade = int(input('Idade: '))
    genero = input('Gênero (F/M): ').strip().lower()
    somaIdade += idade

    if genero == 'm' and pessoas == 1:
        velho = idade
        homem = nome

    elif genero == 'm' and idade > velho:
        velho = idade
        homem = nome

    elif genero == 'f' and idade < 20:
        novas += 1

print('-' * 20)
print('RESULTADOS:')
print(f'- A média de idade do grupo é {somaIdade / 4:.2f}')
print(f'- O homem mais velho tem {velho} anos de idade e se chama {homem.title()}')
print(f'- {novas} mulher(es) tem/têm menos de 20 anos de idade')