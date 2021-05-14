nome = input('Qual é seu nome? ')

if nome == 'Raissa':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino!')
else: # A estrutura do else é opcional!
    print('Seu nome é bem normal!')

print(f'Tenha um bom dia, {nome}!')