'''48. Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
 12376489
 => 98467321'''
def numero_invertido():
    numero = int(input('\n\nDigite um umero: '))

    numero_invertido = str(numero)[::-1]

    print('\nNumero Digitado: {}\nNumero Invertido: {}\n'.format(numero,numero_invertido))
numero_invertido()

