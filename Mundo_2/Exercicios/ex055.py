# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Peso da {}º pessoa: '.format(pessoa)))
    if pessoa == 1: # É a primeira ocorrência do laço, ou seja, o primeiro vai ser maior e menor
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {:.1f}Kg'.format(maior))
print('O menor peso é {:.1f}Kg'.format(menor))
