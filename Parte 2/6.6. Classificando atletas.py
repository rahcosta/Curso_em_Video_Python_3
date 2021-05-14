# A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE
# UM ATLETA E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE:
# ATÉ 9 ANOS: MIRIM
# ATÉ 14 ANOS: INFANTIL
# ATÉ 19 ANOS: JÚNIOR
# ATÉ 20 ANOS: SÊNIOR
# ACIMA: MASTER

from datetime import date

nasc = int(input('Ano de nascimento: '))
idade = date.today().year - nasc

if idade < 10:
    print(f'O/A atleta tem {idade} anos. \nCategoria: MIRIM')
elif idade < 15:
    print(f'O/A atleta tem {idade} anos. \nCategoria: INFANTIL')
elif idade < 20:
    print(f'O/A atleta tem {idade} anos. \nCategoria: JÚNIOR')
elif idade < 21:
    print(f'O/A atleta tem {idade} anos. \nCategoria: SÊNIOR')
else:
    print(f'O/A atleta tem {idade} anos. \nCategoria: MASTER')