# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def área(l, c):
    a = l * c
    print(f'A área do retangulo com as medidas {l}m x {c}m é de {a:.1f}m².')


### Aplicação
largura = float(input('Qual a largura do retângulo em metros? '))
comprimento = float(input('Qual o comprimento do retângulo em metros? '))
área(largura, comprimento)
