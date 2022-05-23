# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
# a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

### Gerando uma lista randomica

def sorteia(lst):
    print('Sorteando 5 valores para a lista...')
    for n in range(0, 5):
        r = randint(1, 50)
        lst.append(r)
    print(f'A lista gerada foi: {lst}.')

def somaPar(lst):
    par = 0
    for n in lst:
        if n % 2 == 0:
            par += n
    print(f'A soma dos números pares da lista é igual a {par}')


numeros = list()

sorteia(numeros)
somaPar(numeros)
