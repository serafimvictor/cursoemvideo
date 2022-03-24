# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior



# Definindo os valores que serão recebidos.
primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))

# Definindo as condições
if primeiro == segundo:
    print('Não existe valor maior, os dois são iguais')
elif primeiro < segundo:
    print('O SEGUNDO valor é maior')
else:
    print('O PRIMEIRO valor é maior')
