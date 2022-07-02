'''9.Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.'''
#C = 5 * ((F-32) / 9).

f = float(input('Qual é a Temperatura em Farenheit: '))
c = 5 * ((f - 32) / 9)
print('A temperatura em Celsius e equivale a : %.2f°C' %c)
