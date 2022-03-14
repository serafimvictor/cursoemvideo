# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

print('A nota 1 foi {:.1f}, a 2º foi {:.1f} e sua média foi de {:.1f}.'.format(n1, n2, media))
