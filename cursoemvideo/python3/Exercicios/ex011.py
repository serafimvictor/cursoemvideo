# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input('Digite a largura em metros: '))
alt = float(input('Digite a altura em metros: '))
area = larg * alt
tinta = area / 2

print('Essa parede tem uma área de {}m² e precisará de {}L de tinta para pintá-la.'.format(area, tinta))
