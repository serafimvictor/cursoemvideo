# Faça um programa que:
# leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
#import math

angulo = float(input('Digite o ângulo que você deseja: '))

xsen = sin(radians(angulo))
xcos = cos(radians(angulo))
xtan = tan(radians(angulo))

print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, xsen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, xcos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, xtan))
