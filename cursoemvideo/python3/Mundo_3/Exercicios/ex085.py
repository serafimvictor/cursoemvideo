# Crie um programa onde o usuário possa digitar sete valores numéricos 
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

lista = []
par = []
impar = []

for n in range(0, 7):
    num = int(input(f'{n + 1}º - Digite um número: '))
    if num % 2 == 0:
        par.append(num)
        # lista[0].append(num) - Usado na aula com a lista declarada > lista = [[], []]
    else:
        impar.append(num)
par.sort() # lista[0].sort() - Usado na aula
impar.sort() # lista[1].sort() - Usado na aula
lista.append(par[:])
lista.append(impar[:])
print(f'Você cadastrou na lista os seguintes números: {lista}')
print(f'Os números pares são: {lista[0]}')
print(f'Os números impares são: {lista[1]}')
