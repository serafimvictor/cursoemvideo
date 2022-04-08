# Escreva um programa que leia um número N inteiro qualquer 
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

print('{}\nSequência de Fibonacci\n{}'.format('-' * 25, '-' * 25))

termos = int(input('Quantos termos você quer mostrar? '))
num1 = 0
num2 = 1 
print('~' * 25)

print('{} -> {}'.format(num1, num2), end = '')
cont = 3
while cont <= termos:
    num3 = num1 + num2
    print(' -> {}'.format(num3), end = '')
    num1 = num2
    num2 = num3
    cont = cont + 1
print(' -> FIM')
