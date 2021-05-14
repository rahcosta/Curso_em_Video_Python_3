'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

print('-=' * 13)
print('\033[7mVERIFICADOR DE PALÍNDROMOS\033[m')
print('-=' * 13)
frase = input('Digite uma frase: ').strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# Exercício sem for i in range():
#inverso = junto[::-1]

# Contar de trás para frente:
for letra in range(len(junto) -1, -1, -1): # comprimento da frase junta -1(pega a última letra), -1 (primeira letra), -1 (passo pra trás)
    inverso += junto[letra]
print(junto, inverso)

if inverso == junto:
    print('\033[34mÉ PALÍNDROMO!\033[m')
else:
    print('\033[31mNÃO É PALÍNDROMO!\033[m')
