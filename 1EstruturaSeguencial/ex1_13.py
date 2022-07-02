
'''
13.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
'''

def peso_ideal_por_genero():
    altura = float(input( 'Qual a sua Altura: '))
    homens =  (72.7 * altura) - 58
    mulheres = (62.1 * altura) - 44.7
    print('Com essa Altura o Peso Ideal para Homem é %dKg E o Peso Ideal para Mulheres é %dKg  ' %(homens,mulheres))
peso_ideal_por_genero()
