# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()
total = 0
jogador['Nome'] = str(input('Nome: ')).strip()
partidas = int(input('Quantas partidas jogou? '))

for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols no jogo {i + 1}? ')))
jogador['Gols'] = gols[:]

for i in gols:
    total += i
jogador['Total_Gols'] = total
### Aula ---- jogador['Total_Gols'] = sum(gols)

print()
print('-=' * 30)
print(jogador)

print()
print('-=' * 30)
for k, v in jogador.items():
    print(f'{k:10}: {v}')

print()
print('-=' * 30)
for n, g in enumerate(gols):
    print(f' - Na {n + 1}º partida, fez {g} gols.')
print(f'Fez {jogador["Total_Gols"]} gols no campeonato.')
