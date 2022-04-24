# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = list()

for n in range(0, 5):
    valores.append(int(input(f'{n} - Digite um valor: ')))
maior = max(valores)
menor = min(valores)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}; ', end='')
print()

print(f'O menor valor digitado foi {menor} na posição ', end='')
for c, num in enumerate(valores):
    if num == menor:
        print(f'{c}; ', end='')
print()
