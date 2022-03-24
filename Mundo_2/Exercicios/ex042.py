# Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

if l1 == l2 and l1 == l3:
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES')
elif l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

### Exemplo da aula

# r1 = float(input('Primeiro segmento: '))
# r2 = float(input('Segundo segmento: '))
# r3 = float(input('Terceiro segmento: '))

# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print('Os segmentos acima PODEM FORMAR triângulo ', end='')
#     if r1 == r2 == r3:
#         print('EQUILÁTERO!')
#     elif r1 != r2 != r3 != r1:
#         print('ESCALENO!')
#     else:
#         print('ISÓSCELES!')
# else:
#     print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
