# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla

cont = 0
num = (int(input('Digite um número: ')), int(input('Digite um número: ')), 
int(input('Digite um número: ')), int(input('Digite um número: ')))

print(f'\nVocê digitou os valores: {num}\n')

if num != 9: # if 9 in num: // < usado na aula
    print('Infelizmente não tem 9...\n')
else:
    print(f'O valor 9 apareceu {num.count(9)} vezes.\n')

if num != 3:
    print('Infelizmente não tem 3...\n')
else:
    print(f'A primeira posição em que o valor 3 apareceu foi a {num.index(3) + 1}ª\n')

for n in num:
    if n % 2 == 0:
        print(n, end = ' ')
        cont += 1
if cont == 0:
    print('Não temos números pares... :(')
elif cont > 0:
    print('Esses são os números pares.\n')
