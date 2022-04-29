# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados 
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep


palpites = list()
jogo = list()
total = 1
print('---' * 15)
print(f"{'MEGA-SENA':^45}")
print('---' * 15)

jogos = int(input('Quantos jogos deseja gerar? '))

while total <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    palpites.append(jogo[:])
    jogo.clear()
    total += 1

print('~=~' * 15)
print(f'Aqui estão seus {jogos} jogos sorteados. Boa sorte!')
sleep(1)
for c, jn in enumerate(palpites):
    print(f'Jogo {c + 1} - {jn}')
    sleep(1)
