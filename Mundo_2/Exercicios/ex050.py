par = 0
for n in range(1, 7):
    num = int(input('{} - Digite um número: '.format(n)))
    if num % 2 == 0:
        par = par + num
print('A soma dos números pares digitados equivalem a {}.'.format(par))
