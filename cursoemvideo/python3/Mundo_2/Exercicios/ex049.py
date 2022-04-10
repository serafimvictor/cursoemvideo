# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

num = int(input('Digite um número para saber a tabuada: '))
print('=== Tabuada de {} ==='.format(num))
for n in range(0, 11):
    multi = num * n
    print('{} x {} = {}'.format(num, n, multi))

## Aula

# num = int(input('Digite um número para saber a tabuada: '))
# for n in range(0, 11):
#     print('{} x {} = {}'.format(num, n, num * n))
