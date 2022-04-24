num = [2, 5, 9, 1]
print(f'1º - {num}')
num[2] = 3
num.append(7)
print(f'2º - {num}')
num.sort()
print(f'3º - {num}')
num.sort(reverse=True)
num.insert(2, 0)
print(f'4º - {num}')
num.pop()
print(f'5º - {num}')
print(f'6º - Essa lista tem {len(num)} valores.')
if 6 in num:
    num.remove(6)
else:
    print('Não tem 6')

###########

valores = []
#valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for n in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} temos o valor {v}')

###########

a = [2, 3, 4, 7]
b = a
# b = a[:] \\ Copia os valores sem igualar as listas
b[2] = 8 ### Listas igualadas, os valores mudam nas duas
print(f'Lista A: {a}')
print(f'Lista B: {b}')
