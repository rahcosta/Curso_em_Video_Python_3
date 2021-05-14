# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE:
# SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR;
# SE É A HORA DE SE ALISTAR;
# SE JÁ PASSOU DO TEMPO DE ALISTAMENTO.
# SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO.

from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
print('Escolha seu gênero:')
print('[ F ] Feminino \n[ M ] Masculino')
genero = input('Sua opção: ').upper()

atual = date.today().year
idade = atual - ano
prazo = idade - 18

if ano > 2003 and genero == 'M':
    print(f'Você tem ou irá completar {idade} anos de idade, logo, ainda faltam {abs(prazo)} anos para o seu alistamento.')
    print(f'Seu alistamento será em {ano + abs(prazo)}')
elif ano == 2003 and genero == 'M':
    print(f'Você completou ou irá completar {idade} anos de idade, logo, deverá se alistar este ano.')
elif ano < 2003 and genero == 'M':
    print(f'Você já tem ou irá completar {idade} anos de idade, logo, está em atraso há {prazo} anos para o alistamento.')
    print(f'Você já deveria ter se alistado em {atual - abs(prazo)}')
elif genero == 'F':
    print('Seu gênero é feminino, logo, o alistamento não é obrigatório para você.')