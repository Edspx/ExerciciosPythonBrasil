
'''
15.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$
    Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
def calculo_salario_liquido():
    salario_hora = float(input('Qual o Valor da sua hora de Trabalho R$: '))
    horas_trabalhadas = int(input('Quantos horas trabalhou esse mes: '))
    salario_bruto = salario_hora * horas_trabalhadas
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicado = salario_bruto * 0.05
    descontos = ir + inss + sindicado
    salario_liquido = salario_bruto - descontos
    
    print('+ Salário Bruto : R$',salario_bruto)
    print('- IR (11%) : R$',ir)
    print('- INSS (8%) : R$',inss)
    print('- Sindicato ( 5%) : R$',sindicado)
    print('- Total de descontos : R$',descontos)
    print('= Salário Liquido : R$',salario_liquido)
calculo_salario_liquido()
    