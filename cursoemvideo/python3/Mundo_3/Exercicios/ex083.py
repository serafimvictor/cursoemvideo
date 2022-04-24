# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se
# a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = str(input('Digite a expressão: '))
pilha = []

for simb in exp: # Validando os parenteses
    if simb == '(': # Ao encontrar o parenteses '(' ele adiciona à lista
        pilha.append('(')
    elif simb == ')': # Validar o parenteses ')' 
        if len(pilha) > 0: # Se a lista já tiver um abrindo, ele deleta e 'completa' o parenteses
            pilha.pop()
        else: # Se não tiver nada, ele adiciona e encerra, validando que está errado
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão errada!')
