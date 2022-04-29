# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somacol = somapar = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))

print('~' * 60)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='') ## Pra validar o par, embaixo.
    print() ##if matriz[linha][coluna] % 2 == 0: - Aula, fez um if aqui ao invés de embaixo

print('~' * 60)

for coluna in matriz:
    somacol += coluna[2]
    for num in coluna:
        if num % 2 == 0:
            somapar += num

print(f'A soma de todos os pares é igual a {somapar}')
print(f'A soma da terceira coluna é igual a {somacol}')
print(f'O maior valor da segunda linha é o {max(matriz[1])}.')
