# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randrange
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
num = int(input('Em que número eu pensei? '))
numpc = randrange(6)
# numpc = random.randint(0, 5) - usado na aula
print('Processando...')
sleep(2)
if num == numpc:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(numpc, num))
