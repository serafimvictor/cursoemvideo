# Escreva um programa que 
# converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tempc = float(input('Digite a temperatura em ºC: '))
tempf = (tempc * 9 / 5) + 32

print('A temperatura de {}ºC correspondem a {}ºF!'.format(tempc, tempf))
