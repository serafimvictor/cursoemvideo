# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resposta = 'S'
cont = 0
soma = 0
maior = 0
menor = 0

while resposta != 'N':
    numero = int(input('Digite um número: '))
    resposta = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    soma = soma + numero
    cont = cont + 1
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
media = soma / cont
print('Você digitou {} números e a media deles foi {:.2f}'.format(cont, media))
print('O maior valor digitado é {} e o menor valor é {}'.format(maior, menor))
