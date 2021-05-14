# FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
# QUANTAS VEZES APARECE A LETRA 'A';
# EM QUE POSIÇÃO ELA APARECE PELA PRIMEIRA VEZ;
# EM QUE POSIÇÃO ELA APARECE PELA ÚLTIMA VEZ.

frase = input('Digite a frase a ser analisada: ').strip().lower()
a = frase.count('a')
primeira = frase.find('a')
ultima = frase.rfind('a')

print(f'Analisando a frase {frase}...')
print()
print(f'A letra A apareceu {a} vezes.')
print(f'A primeira letra A apareceu na posição {primeira + 1}')
print(f'A última letra A apareceu na posição {ultima + 1}')
