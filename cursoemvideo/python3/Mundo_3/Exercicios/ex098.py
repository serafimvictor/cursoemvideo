# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada: 
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def contador(i, f, p):
    cont = 0
    print(f'{"-" * 10} Contador de {i} a {f} pulando {p} {"-" * 10}')
    
    if f < i:
        p *= -1
        f -= 1
    else:
        f += 1
    
    for c in range(i, f, p):
        cont += 1
        print(c, end=' ', flush = True)
        sleep(0.5)
    print('FIM.')


contador(1, 10, 1)
contador(10, 0, 2)

inicio = int(input('Qual número você quer iniciar a contagem? '))
fim = int(input('Qual número será o final da contagem? '))
pulo = int(input('A contagem vai pular de quanto em quanto? '))

contador(inicio, fim, pulo)
