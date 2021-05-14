#nome = input('Qual é o seu nome? ')
# print(f'Prazer em te conhecer {nome:20} !')
# print(f'Prazer em te conhecer {nome:>20} !')
#print(f'Prazer em te conhecer {nome:^20} !')

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
exp = n1 ** n2

print(f'A soma é {s}, \n o produto é {m}, \n e a divisão é {d}', end=' ')
print(f'Divisão inteira {di} e potência {exp}')