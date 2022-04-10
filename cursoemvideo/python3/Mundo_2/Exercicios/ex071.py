# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e 
# o programa vai informar quantas cédulas de cada valor serão entregues. 
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
from time import sleep

print('≃' * 40)
print('{:^40}'.format('Banco Pythonist'))
print('≃' * 40)
sleep(0.6)

valor = int(input('Qual valor você deseja sacar? R$'))
total = valor
cedula = 50
totalcedula = 0
sleep(0.5)
print('Você vai receber:')
sleep(0.5)
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        sleep(0.3)
        if totalcedula != 0:
            print(f'{totalcedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            sleep(0.3)
            break
print('≃' * 40)
print('Retire as cédulas no local indicado. Volte sempre!')
