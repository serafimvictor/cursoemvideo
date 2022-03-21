
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 6.0:
    print('Você está aprovado! Parabéns!')
else:
    print('Reprovou, volte a estudar!')
print('Sua média foi de {:.1f}.'.format(media))