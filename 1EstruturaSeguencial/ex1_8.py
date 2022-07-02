
'''8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''
def calculo_salario():
    remuneracao_hora = float(input('Quanto você Ganha por hora: '))
    horas_mes = float(input('Quantos Horas Você trabalha por mês: '))
    salario = remuneracao_hora * horas_mes
    print('Seu Salário e R$', salario)
calculo_salario()