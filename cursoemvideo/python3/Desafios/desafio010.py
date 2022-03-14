# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
# e mostre quantos Dólares ela pode comprar de acordo com a cotação = US$1 = R$3.27

n = float(input('Digite quantos R$ tem na sua carteira: '))
d = n // 3.27
r = n % 3.27

print('Com seus R${}, você consegue comprar ${:.0f} e te sobram R${:.2f}'.format(n, d, r))
