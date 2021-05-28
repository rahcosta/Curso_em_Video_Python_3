'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e
fechados na ordem correta.'''

text = input('Digite sua expressão: ').strip()

pilha = []

for simb in text:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0: # se a pilha já estiver preenchida coms os '(', eu removo e coloco ')'.
            pilha.pop() # remove o último elemento da lista
        else:
            pilha.append(')')
            break
if len(pilha) == 0: # significa que cada '(' foi igual aos ')'.
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
