# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show = False):
    """"
    ---> Calcula o fatorial de um número
    :param num: É o número a ser calculado
    :param show: Define se vai ou não mostrar o cálculo
    :return: Retorna o calculo ou resultado Fatorial da variavel num.
"""
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c != 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
    return f


#### Default APP 
print('-'* 50)
n = int(input('Número para ver o fatorial: '))
vis = str(input('Deseja ver o resultado completo? [S/N] ')).strip().upper()
if vis[0] == 'S':
    print(fatorial(n, show=True))
elif vis[0] == 'N':
    print(fatorial(n))
