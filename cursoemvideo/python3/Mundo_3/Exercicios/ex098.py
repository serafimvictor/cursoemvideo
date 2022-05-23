# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada: 
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def contador(i, f, p):
    cont = 0
    for c in range(i, f, p):
        cont += 1
        print(c, end=' ')
    sleep(1)
    print('FIM.')


print(f'{"-" * 10} Contador de 1 a 10 pulando 1 {"-" * 10}')
contador(1, 11, 1)
print(f'{"-" * 10} Contador de 10 a 0 pulando 2 {"-" * 10}')
contador(10, -1, -2)
print(f'{"-" * 10} Agora monte sua contagem {"-" * 10}')

inicio = int(input('Qual número você quer iniciar a contagem? '))
fim = int(input('Qual número será o final da contagem? '))
pulo = int(input('A contagem vai pular de quanto em quanto? '))

print(f'{"-" * 10} Contador de {inicio} a {fim} pulando {pulo} {"-" * 10}')

if fim < inicio:
    pulo *= -1
else:
    fim += 1

contador(inicio, fim, pulo)
