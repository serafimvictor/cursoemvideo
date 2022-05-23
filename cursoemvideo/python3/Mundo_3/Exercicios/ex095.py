# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = list()
jogador = dict()
gols = list()
total = 0
while True:
    jogador['Nome'] = str(input('Nome: ')).strip()
    partidas = int(input('Quantas partidas jogou? '))
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols no jogo {i + 1}? ')))
    jogador['Gols'] = gols[:]
    jogador['Total_Gols'] = sum(gols)
    gols.clear()
    time.append(jogador.copy())
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    while opcao[0] not in 'SN':
        opcao = str(input('Não entendi... Quer continuar? [S/N] ')).strip().upper()
    if opcao[0] == 'N':
        break
print()
print('-=' * 30)
print(f"{'Cod'} | {'Nome':<20} | {'Gols':<20} | {'Total'}")
print('--' * 30)

for c, k in enumerate(time):
    print(f'{c:>4} {k["Nome"]:<22} {k["Gols"]} {k["Total_Gols"]:>8}')

print('-=' * 30)

while True:
    dados = int(input('Insira o código para verificar os dados do jogador: [999 pra parar] '))
    if dados == 999:
        break
    if dados >= len(time):
        print(f'Erro! Jogador {dados} não encontrado. Digite novamente: [999 = Parar] ')
    else:    
        print('--' * 30)
        print(f' --- Dados do jogador {time[dados]["Nome"]}:')
        for i, g in enumerate(time[dados]['Gols']):
            print(f'  - Na {i + 1}º partida: {g} gols.')

print('Obrigado, volte sempre!')
