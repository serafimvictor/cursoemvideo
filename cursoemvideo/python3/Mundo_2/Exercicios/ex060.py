# Faça um programa que leia um número qualquer e mostre o seu fatorial.

fat = int(input('Digite um número para calcular seu fatorial: '))
contfat = 1
print('Calculando {}! = '.format(fat), end = ' ')
for n in range(fat, 0, -1):
    contfat = contfat * n
    if n != 1:
        print(n, end = ' x ')
    else:
        print('{} = '.format(n), end = '')
print('{}'.format(contfat))


### Exemplo 1 - aula ###

# from math import factorial
#
# n = int(input('Digite um número para calcular seu fatorial: '))
# f = factorial(n)
# print('O fatorial de {} é {}.'.format(n, f))

### Exemplo 2 - aula ###

# n = int(input('Digite um número para calcular seu fatorial: '))
# c = n
# f = 1
# print('Calculando {}! = '.format(n), end = '')
# while c > 0:
#     print('{}'.format(c), end = '')
#     print(' x ' if c > 1 else ' = ', end = '')
#     f *= c
#     #f = f * c
#     c -= 1
#     #c = c - 1
# print(f)
