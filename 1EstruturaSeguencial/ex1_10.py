
'''10.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.'''
def celsius_para_farenheit():
    c = float(input('Qual e a Temperatura em Celsius: '))
    f = (c * 9/5) + 32
    #print('A temperatura em Farenheit equivalente é: %.2f°F' %f)
    return f
    
celsius_para_farenheit()