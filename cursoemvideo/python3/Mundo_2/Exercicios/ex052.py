# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
cont = 0
for n in range(1, num + 1):
    primo = num % n
    if primo == 0:
        cont = cont + 1
        n = '\033[33m{}\033[m'.format(n)
    else:
        n = '\033[31m{}\033[m'.format(n)
    print(n, end = ' ')
print('\nO número {} foi divisível {} vezes.'.format(num, cont))
if cont > 2:
    print('E por isso ele NÃO É PRIMO!')
elif cont == 2:
    print('E por isso ele É PRIMO!')
