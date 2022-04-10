# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#Definindo os objetos

valorcasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = valorcasa / (anos * 12)

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valorcasa, anos, prestacao)) 
#Declarando condições

if (salario * 0.3) <= prestacao:
    print('Empréstimo \033[31mNEGADO\033[m!')
elif (salario * 0.3) > prestacao:
    print('Empréstimo pode ser \033[32mCONCEDIDO\033[m!')
