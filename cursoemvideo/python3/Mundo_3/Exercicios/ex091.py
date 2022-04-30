# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Player1': randint(1, 6), 
        'Player2': randint(1, 6),
        'Player3': randint(1, 6),
        'Player4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
print('-=' * 20)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'{"-=" * 8} Ranking {"-=" * 8}')
for i, e in enumerate(ranking):
    print(f'{i + 1}º Lugar =  {e[0]} com {e[1]} pontos.')
