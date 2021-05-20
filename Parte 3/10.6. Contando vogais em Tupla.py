'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

conjunto = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'TRABALHADOR', 'FUTURO')

for palavra in conjunto:
    print(f'\nNa palavra {palavra} temos ', end='')
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
