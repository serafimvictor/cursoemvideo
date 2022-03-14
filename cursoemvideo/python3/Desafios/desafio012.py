# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

p1 = float(input('Digite o valor do produto R$'))
pd = p1 * 0.05
pn = p1 - pd

print('Seu produto de R${} teve R${:.2f} de desconto e saiu por R${:.2f}'.format(p1, pd, pn))
