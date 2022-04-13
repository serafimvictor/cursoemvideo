# Crie uma tupla preenchida com os 20 primeiros colocados da 
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo',
'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')

print('-=' * 50)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 50)
print(f'Os 5 primeiros são {times[:5]}')
print('-=' * 50)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 50)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 50)
print(f'O {times[19]} está na {times.index("Chapecoense") + 1}º posição.')
