'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

print('-=' * 20)
print('       ANÁLISE DE DADOS DO GRUPO')
print('-=' * 20)

cont_pessoa = mais_dezoito = homem = menos_vinte = 0

while True:
    cont_pessoa += 1
    print('-' * 40)
    print(f'              CADASTRO {cont_pessoa}')
    print('-' * 40)
    idade = int(input('Idade: '))
    genero = input('Gênero [F/M]: ').strip().lower()[0]
    if idade > 18:
        mais_dezoito += 1
    if genero == 'm':
        homem += 1
    elif genero == 'f' and idade < 20:
        menos_vinte += 1
    escolha = input('Deseja cadastrar mais pessoas? [S/N]: ').strip().lower()[0]
    if escolha == 'n':
        break
print()
print('-' * 40)
print(f'       ANALISANDO OS DADOS CADASTRADOS:')
print('-' * 40)
print(f'Quantas pessoas com mais de 18 anos de idade foram cadastradas? \033[1;34m{mais_dezoito}\033[m.')
print(f'Quantas pessoas do sexo masculino foram cadastradas? \033[1;34m{homem}\033[m.')
print(f'Quantas mulheres com menos de 20 anos de idade foram cadastradas? \033[1;34m{menos_vinte}\033[m.')
