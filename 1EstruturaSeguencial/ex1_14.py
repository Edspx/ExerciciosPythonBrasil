
'''14.João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
    Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
    deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e 
    calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
    Imprima os dados do programa com as mensagens adequadas.'''
    
def pagoDePescador():
    #peso limite de 50kg
    pesoLimite = 50
    excesso = 0
    multaExcesso = 0
    
    #multa R$4 por kg excedente
    multa = 4
    
    #ler a variavel peso de peixes e calule o excesso
    pesoPeixe = float(input('Qual o peso dos Peixes: '))
    
    #gravar a variavel excesso a quantidade de quilos alem do limite e na variavel multa o valor da multa
    if pesoPeixe > pesoLimite:
        excesso = pesoPeixe - pesoLimite
        multaExcesso = multa * excesso
    #imprima os dados do progrma
    if excesso > 0 :
        print('\n')
        print('Atenção Houve excesso de Peso dos Peixes, que acarreta Multas')
        print('-'*20)
        print('Peso limite %dKg Peso Declarado ::%.2fKg '%(pesoLimite,pesoPeixe))
        print('Peso Excedente: %.2fKg Multa de: R$%.2f' %(excesso,multaExcesso))
        print('-'*20)
        print('Valor a Pagar ')
        print('R$ ',multaExcesso)
        print('-'*20)
    else:
        print('\n')
        print('Peso dos Peixes esta dentro dos Limites Permitidos pelo Estado de São Paulo')
        print('-'*20)
        print('NÃO A COBRANÇA PARA ESSE PESO')
        print('-'*20)
pagoDePescador()
