# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(*num):
    cont = maior = 0
    print('\nAnalisando os valores passados.')
    for n in num:
        print(n, end = ' ', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = n
        else:
            if n >= maior:
                maior = n
        cont += 1
    print(f'\nO maior número dos {cont} analisados é o {maior}.')

maior(9, 7, 1, 12, 10, 8)
maior(2, 4, 6, 8, 99, 3)
maior(-1, -99, -88, -2, -3)
