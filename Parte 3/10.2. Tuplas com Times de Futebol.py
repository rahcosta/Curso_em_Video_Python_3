'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Sport Recife.'''

print('-=' * 30)
print('     TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL 2020')
print('-=' * 30)

times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense',
         'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino',
         'Ceará SC', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife',
         'Fortaleza', 'Vasco da Gama', 'Goias', 'Coritiba', 'Botafogo')

for posicao in range(len(times)):
    print(f'{posicao + 1}º {times[posicao]}')

print()
print('\033[4mColocação final dos 5 primeiros colocados no Brasileirão 2020:\033[m')
for posicao in range(0, 5):
    print(f'{posicao + 1}º {times[posicao]}')

print()
print('\033[4mColocação final dos 4 últimos colocados no Brasileirão 2020:\033[m')
for posicao in range(16, 20):
    print(f'{posicao + 1}º {times[posicao]}')

print()
print('\033[4mTimes em ordem alfabética:\033[m')
print(sorted(times))

print()
print('\033[4mColocação do time do Sport Recife:\033[m')
print(f'{times.index("Sport Recife") + 1}º {times[14]}')