# CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM
# NO FINAL, DE ACORDO COM A MÉDIA ATINGIDA:
# MÉDIA ABAIXO DE 5.0: REPROVADO!
# MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
# MÉDIA 7.0 OU SUPERIOR: APROVADO!

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print(f'Sua média foi {media:.1f}. \n\033[31mREPROVADO!\033[m')
elif media < 6.9:
    print(f'Sua média foi {media:.1f}. \nRECUPERAÇÃO.')
else:
    print(f'Sua média foi {media:.1f}. \n\033[34mAPROVADO!\033[m')