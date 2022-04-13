lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

for comida in lanche:
    print(f'Eu vou comer {comida}!')

print(f'Comi demais')

print(sorted(lanche)) # Mostra organizado em ordem alfabética.

##### Outro exemplo

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # Une os dois na ordem que está sendo somado
print(c.count(5)) # Conta quantos '5' tem na tupla
print(c)
print(c.index(4)) # Mostra em qual posição está a primeira ocorrência do valor solicitado
