# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento.

valor = float(input('Digite o valor do produto: R$'))

pagamento = int(input(''' FORMAS DE PAGAMENTO
[ 1 ] À vista (Dinheiro ou cheque) 
[ 2 ] Cartão (à vista)
[ 3 ] Cartão em 2x
[ 4 ] Cartão em 3 ou mais vezes
Qual é a opção? '''))

if pagamento == 1:
    total = valor - (valor * 0.1)

elif pagamento == 2:
    total = valor - (valor * 0.05)

elif pagamento == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))

elif pagamento == 4:
    total = valor + (valor * 0.2)
    parcelas = int(input('Quantas parcelas? '))
    juros = total / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, juros))

print('Sua compra de {:.2f} vai custar R${:.2f} no final'.format(valor, total))
