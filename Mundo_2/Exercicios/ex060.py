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
