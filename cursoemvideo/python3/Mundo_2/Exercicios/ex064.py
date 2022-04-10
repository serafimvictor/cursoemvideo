# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles

soma = 0
num = 0
cont = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    soma = soma + num
    cont = cont + 1
print('A soma dos {} números que você digitou é igual a {}'.format(cont - 1, soma - 999))
