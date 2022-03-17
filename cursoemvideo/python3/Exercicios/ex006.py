# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
raiz = n ** (0.5)

print(' O dobro de {} é {}.\n O triplo é {}.\n E sua raiz quadrada é {:.2f}.'.format(n, d, t, raiz))
