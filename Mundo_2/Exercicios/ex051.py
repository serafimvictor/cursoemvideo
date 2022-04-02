#  Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#  No final, mostre os 10 primeiros termos dessa progressão.

print('''{}
    10 TERMOS DE UMA PA
{} 
'''.format('=' * 25, '=' * 25))

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

print(termo, end= ' -> ') # Recurso alternativo de alta eficiência (RAAE) ou gambiarra

for n in range(1, 10):
    termo = termo + razao
    print(termo, end = ' -> ')
print('ACABOU')

## Exemplo AULA

# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razão: '))
# decimo = primeiro + (10 - 1) * razao
# for c in range(primeiro, decimo + razao, razao):
#     print('{} '.format(c), end = '-> ')
# print('ACABOU')
