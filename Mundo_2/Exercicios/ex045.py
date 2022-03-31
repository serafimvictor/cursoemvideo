# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada? '))
computador = randint(0, 2)
print('~' * 33)
print('Computador jogou {}.'.format(itens[computador]))
print('Você jogou {}.'.format(itens[jogada]))
print('~' * 33)
if jogada == 0: # Jogador escolheu PEDRA
    if computador == 0:
        print('Nós empatamos!')
    elif computador == 1:
        print('Eu ganhei! Computador WIN')
    elif computador == 2:
        print('Ah... Você me ganhou! Jogador WIN')
elif jogada == 1: # Jogador escolheu PAPEL 
    if computador == 0:
        print('Ah... Você me ganhou! Jogador WIN')
    elif computador == 1:
        print('Nós empatamos!')
    elif computador == 2:
        print('Eu ganhei! Computador WIN')
elif jogada == 2: # Jogador escolheu TESOURA
    if computador == 0:
        print('Eu ganhei! Computador WIN')
    elif computador == 1:
        print('Ah... Você me ganhou! Jogador WIN')
    elif computador == 2:
        print('Nós empatamos!')
