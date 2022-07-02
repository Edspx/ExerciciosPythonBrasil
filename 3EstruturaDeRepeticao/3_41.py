'''41. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor
dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
1 0
3 10
6 15
9 20
12 25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela
R$ 1.000,00 0 1 R$ 1.000,00
R$ 1.100,00 100 3 R$ 366,00
R$ 1.150,00 150 6 R$ 191,67'''

def divida_juros():
    divida = float(input('Valor da Divida: R$ '))

    parcelas = [1, 3, 6, 9, 12]
    juros = [0, 10, 15, 20, 25]

    print('\n')
    print('Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela')
    for i in range(len(parcelas)):
        print('R$ {} {} {} R$ {}'.format(round(divida + (divida * juros[i] / 100),2),(divida * juros[i] / 100),parcelas[i],round((divida + (divida * juros[i] / 100)) / parcelas[i],2)))
    print('\n')
divida_juros()
   