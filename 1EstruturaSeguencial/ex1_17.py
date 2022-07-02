
'''17.Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, 
    isto é, considere latas cheias.'''
def loja_de_tintas2():
    area = float(input('Qual é o Tamanho em Metros² da Área a ser Pintada: '))
    cobertura_tinta_por_litro = 6 #m²
    latas18 = 80 #reais
    galoes3_6 = 25 #reais
    cobertura_latas18 = 18 * cobertura_tinta_por_litro
    cobertura_galoes3_6 = 3.6 * cobertura_tinta_por_litro
    
    #comprar apenas latas de 18 litros;
    latas18_nescessarias = int(area / cobertura_latas18)
    latas18_nescessarias_ajuste = float(area / cobertura_latas18)
    if latas18_nescessarias < latas18_nescessarias_ajuste:
        latas18_nescessarias = latas18_nescessarias + 1
    print('\n')
    print('-'*20)
    print('Latas de Tinta de 18 Litros: ',latas18_nescessarias)
    print('Preço Por Lata e R$%.2f :: Total a Pagar em Latas de 18 l é: R$%.2f ' %(latas18,latas18*int(latas18_nescessarias)))
        
    
    #comprar apenas galões de 3,6 litros;
    cobertura_galoes3_6_nescessarios = int(area / cobertura_galoes3_6)
    cobertura_galoes3_6_nescessarios_ajuste = float(area / cobertura_galoes3_6)
    if cobertura_galoes3_6_nescessarios < cobertura_galoes3_6_nescessarios_ajuste:
        cobertura_galoes3_6_nescessarios = cobertura_galoes3_6_nescessarios + 1
    print('\n')
    print('-'*20)
    print('Galoes de Tinta de 3.6 Litros: ',cobertura_galoes3_6_nescessarios)
    print('Preço Por Lata e R$%.2f :: Total a Pagar em Galão de 3.6 l é: R$%.2f ' %(galoes3_6,galoes3_6*cobertura_galoes3_6_nescessarios))
    
    #misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, 
    if area > cobertura_galoes3_6:
        if area < (cobertura_galoes3_6 * 5):
            galoes_para_compra = float(area / cobertura_galoes3_6)  
            galoes_para_compra = int(galoes_para_compra + (galoes_para_compra * 0.10))
            print('\n')
            print('-'*20)
            print('Galoes de 3.6 Litros: ',galoes_para_compra)
            print('Preço Por Galoes e R$%.2f :: Total a Pagar em Galoes de 3.6l é: R$%.2f ' %(galoes3_6,galoes3_6*galoes_para_compra))
            
        else:
            #Utilise apartir de uma lata
            latas_para_compra = float(area / cobertura_latas18)
            quantidade_latas_nescessaria = float(area / cobertura_latas18)
            quantidade_latas_nescessaria = str(quantidade_latas_nescessaria).split('.')[0]
            latas_para_compra_ajuste_galoes_3_6 = float(area / cobertura_latas18) - int(quantidade_latas_nescessaria)
            quantidade_litros_faltantes = latas_para_compra_ajuste_galoes_3_6 * 18 # litragem flatante
            quantidade_galoes_3_6_falantes = quantidade_litros_faltantes / 3.6
            quantidade_galoes_3_6_nescessarios =  int(quantidade_galoes_3_6_falantes + (quantidade_galoes_3_6_falantes * 0.1))
            print('\n')
            print('-'*20)
            print('A quantidade de tinta nescessario e de')
            print('Latas de Tinta de 18 Litros: ',int(quantidade_latas_nescessaria))
            print('Preço Por Lata e R$%.2f :: Total a Pagar em Latas de 18l é: R$%.2f ' %(latas18,latas18*int(quantidade_latas_nescessaria)))
            print('Galoes de 3.6 Litros: ',quantidade_galoes_3_6_nescessarios)
            print('Preço Por Galoes e R$%.2f :: Total a Pagar em Galoes de 3.6l é: R$%.2f ' %(galoes3_6,galoes3_6*int(quantidade_galoes_3_6_nescessarios)))
            print('Valor da compra é R$ ',(latas18*int(quantidade_latas_nescessaria)) + (galoes3_6*int(quantidade_galoes_3_6_nescessarios)))
            
    else:
        #apenas um galão e o suficiente
        print('\n')
        print('-'*20)
        print('Apenas um Galão e Suficiente')
        print('Galoes de 3.6 Litros: ',quantidade_galoes_3_6_nescessarios)
        print('Preço Por Galoes e R$%.2f :: Total a Pagar em Galoes de 3.6l é: R$%.2f ' %(galoes3_6,galoes3_6*int(quantidade_latas_nescessaria)))
    
loja_de_tintas2() 
