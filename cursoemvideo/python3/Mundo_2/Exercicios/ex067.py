# Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Digite um número para ver sua tabuada [Insira um valor negativo pra parar]: '))
    if num < 0:
        break
    print(f'-= Tabuada de {num} =-')
    for n in range(0, 11):
        print(f'{num} x {n} = {num * n}')
print('Tabuada finalizada!')
