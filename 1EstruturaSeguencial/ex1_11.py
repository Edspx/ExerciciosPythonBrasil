'''
11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''
def dois_numeros_inteiros_e_numero_real():
    numInt1 = int(input('Digite o Primeiro Numero sendo Inteiro: '))
    numInt2 = int(input('Digite o Segunto Numero sendo Inteiro: '))
    numReal = float(input('Digite o Terceiro Numero sendo Real: '))
    result1 = (numInt1*2) * (numInt2/2)
    result2 = (numInt1*3) + numReal
    result3 = numReal**3
    print('\n')
    print('o produto do dobro do primeiro com metade do segundo',result1)
    print('a soma do triplo do primeiro com o terceiro',result2)
    print('o terceiro elevado ao cubo',result3)
dois_numeros_inteiros_e_numero_real()