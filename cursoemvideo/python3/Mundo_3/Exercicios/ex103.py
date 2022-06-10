# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog='<unknown>', gols=0):
    """"
    --> Mostrará a ficha de um jogador de acordo com os dados passados pelo usuário
    :jog: Mostrará o nome do jgoador, caso vazio será '<desconhecido>'
    :gols: Mostrará a quantidade de gols feita pelo jogador inserido pelo usuário, caso vazio será 0
    :return: Retorno da funcão
    """
    print(f'O jogador {jog} fez {gols} gols neste torneio')

jogador = str(input('Nome do Jogador: ')).strip()
g = str(input('Quantos gols ele fez? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if jogador.strip() == '':
    ficha(gols=g)
else:
    ficha(jogador, g)
