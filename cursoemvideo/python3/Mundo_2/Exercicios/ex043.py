# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

peso = float(input('Peso em Kg: '))
altura = int(input('Altura em cm: '))
imc = peso / ((altura / 100) ** 2)

print('Seu IMC é de {:.1f}.'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Parabéns, seu peso é o ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso!')
elif 30 <= imc < 40:
    print('Você está com obesidade :(')
elif imc >= 40:
    print('Cuidado, você está com obesidade mórbida!')
