# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

print('-~' * 20)
print('{:^40}'.format('Joguinho de Par ou Ímpar'))
print('-~' * 20)
cont = 0

while True:
    jogescolha = str(input('Par ou Ímpar? ')).strip().upper()[0]
    ## While pra validar a escolha do jogador.
    while True:
        if jogescolha == 'P' or jogescolha == 'I':
            break
        else:
            jogescolha = str(input('Opção inválida. Par ou Ímpar? ')).strip().upper()[0]
    
    jognum = int(input('Escolha um número: '))
    computador = randint(0, 10)
    soma = jognum + computador
    
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    
    print('-' * 40)
    print(f'Você escolheu {jognum} e o computador {computador}. A soma deu {soma} É {resultado}')
    print('-' * 40)

    ## Validação das escolhas e resultado do jogo

    if jogescolha == 'P' and resultado == 'PAR':
        print('Você ganhou :)')
        cont = cont + 1
        print('-' * 40)
    elif jogescolha == 'I' and resultado == 'ÍMPAR':
        print('Você Ganhou')
        cont = cont + 1
        print('-' * 40)
    else:
        print('Perdeu bobão!')
        print('-~' * 20)
        break
    print('Vamos mais uma...\n{}'.format('-' * 40))
    
if cont == 0:
    print('É... Você não ganhou nenhuma :(')
elif cont > 0:
    print(f'Acabou, você ganhou {cont} vezes.')
