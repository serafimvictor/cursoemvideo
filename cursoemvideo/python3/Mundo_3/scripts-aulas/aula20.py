def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


# Default app
soma(b = 4, a = 5)
soma(8, 9)
soma(2, 1)


############################################################################

def contador(*num):
    print(f'Recebi os valores {num} e tem {len(num)} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

############################################################################

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
print(f'Before: {valores}')
dobra(valores)
print(f'After: {valores}')

############################################################################

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} tivemos o total de {s}')

soma(5, 2)
soma(2, 9, 4)
