# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e 
# que se encontram no intervalo de 1 até 500.

num = 0
soma = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
        num = num + 1
print('A soma dos {} números que são múltiplos de 3 e impares equivalem a {}.'.format(num, soma))
