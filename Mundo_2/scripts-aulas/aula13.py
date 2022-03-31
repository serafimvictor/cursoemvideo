## Pequena tabuada ##

n = int(input('Digite um número: '))
for c in range(0, 11):
    mult = n * c
    print('{} x {} = {}'.format(n, c, mult))
print('Fim')

# Aula #

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n
print('O Somatório de todos os valores foi {}.'.format(s))
