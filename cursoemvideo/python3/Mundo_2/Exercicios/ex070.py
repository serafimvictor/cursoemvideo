# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

contmaismil = soma = cont = vmenor = 0
menor = ''

print(f'''{'-' * 40}
{'Lojinha da cobra python':^40}
{'-' * 40} ''')
while True:
    produto = str(input('Nome do produto: ')).strip().capitalize()
    valor = float(input('Preço: R$'))
    if valor > 1000:
        contmaismil += 1
    soma += valor
    
    ### Validação do menor valor
    cont += 1 # Contador pra pegar a primeira referência que sempre vai ser o menor pela ordem

    ## Usado na aula pra simplificar, ao invês de dois blocos, tem um só.
    # if cont == 1 or valor < vmenor:
    #     vmenor = valor
    #     menor = produto
    
    if cont == 1:
        vmenor = valor
        menor = produto
    else: # Validação para ir alterando o menor valor após a primeira ocorrência.
        if valor < vmenor:
            vmenor = valor
            menor = produto

    # Bloco de continuar ou não
    opcao = str(input('Tem mais produto? [S/N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Opção inválida. Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        print('{:-^40}'.format(' ACABOU '))
        #print(f'''{'-'*17}ACABOU{'-'*17}''')
        break

print(f'Suas compras ficaram no valor de R${soma:.2f}')
print(f'Temos {contmaismil} produtos custando mais de R$1000.00')
print(f'O produto mais barato que você comprou foi {menor} e custou R${vmenor:.2f}')
