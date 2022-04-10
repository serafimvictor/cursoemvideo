# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('''{}
Vou pensar num número de 0 a 10
{}'''.format('~' * 40, '~' * 40))
num = int(input('Adivinha que número eu pensei? '))
numpc = randint(0, 10)
cont = 1
while numpc != num:
    if num < numpc:
        num = int(input('Mais... Tenta de novo aí: '))
    if num > numpc:
        num = int(input('Menos... Tenta de novo: '))
    cont = cont + 1
print('Aeeee acertou mizeravi!')
print('Você acertou na {}º tentativa.'.format(cont))


#### Exemplo Aula ####

# computador = randint(0, 10)
# print(''' Acabei de pensar num número entre 0 e 10.
# Consegue adivinhar qual foi?''')
# acertou = False
# palpites = 0
# while not acertou:
#     jogador = int(input('Qual seu palpite? '))
#     palpites += 1
#     if jogador == computador:
#         acertou = True
#     else:
#         if jogador < computador:
#             print('Mais... Tente de novo')
#         elif jogador > computador:
#             print('Menos.. Tente de novo')
# print('Acertou com {} tentativas, parabéns!'.format(palpites))
