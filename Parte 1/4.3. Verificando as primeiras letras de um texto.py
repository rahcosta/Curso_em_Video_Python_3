# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM O NOME 'SANTO'.

cidade = input('Em qual cidade você nasceu? ').lower().strip()

#print(cidade[:5] == 'santo')

separa = cidade.split()
santo = separa[0] == 'santo'

print(f'O nome da cidade começa com Santo? {santo}')