# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Digite o salário da pessoa: R$'))
aum = sal * 0.15
saln = sal + aum

print('Seu salário de R${:.2f} teve um aumento de R${:.2f} e agora será de R${:.2f}'.format(sal, aum, saln))
