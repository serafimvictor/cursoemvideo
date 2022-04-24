# Crie um programa onde o usuário possa digitar cinco valores numéricos 
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
# No final, mostre a lista ordenada na tela.

lista = []
for n in range(0, 5):
    num = int(input('Digite um valor: '))
    if n == 0:
        maior = num
        menor = num
        lista.append(num)
        print('Adicionado ao final da lista.')
    else:
        if num >= maior:
            maior = num
            lista.append(num)
            print('Adicionado ao final da lista.')
        if num <= menor:
            menor = num
            lista.insert(0, num)
            print('Adicionado na posição 0.')
        if menor < num < maior:
            lista.insert(1, num)
            print('Adicionado na posição 1')
print(lista)

### aula
# lista = []
# for c in range(0, 5):
#     n = int(input('Digite um valor: '))
#     if c == 0 or n > lista[-1]:
#         lista.append(n)
#         print('Adicionado ao final da lista.')
#     else:
#         pos = 0
#         while pos < len(lista):
#             if n <= lista[pos]:
#                 lista.insert(pos, n)
#                 print(f'Adicionado na posição {pos} da lista')
#                 break
#             pos += 1
# print(f'Os valores digitados foram {lista}')
