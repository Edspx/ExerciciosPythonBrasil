
'''16.Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''
def loja_de_tintas():
    area = float(input('Qual é o tamanho em metros quadrados da área: '))
    cobertura_tinta = 3 # m² para cada litro
    latas_tinta = 18 #litros
    latas_tinta_valor = 80 #reais por lata com 18litros
    cobertura_lata_tinta = latas_tinta * cobertura_tinta
    #Quantidade de tintas a seram compradas
    tinta_nescessaria = area / cobertura_tinta
    latas_nescessarias = int(tinta_nescessaria / latas_tinta)
    latas_nescessarias_ajuste = float(tinta_nescessaria / latas_tinta)
    if latas_nescessarias < latas_nescessarias_ajuste:
        latas_nescessarias = latas_nescessarias + 1
    
    valor_total = latas_nescessarias * latas_tinta_valor
    print('\n')
    print('Total de latas para a Pintura da área informada')
    print('Área Cliente %.2fm²' %area)
    print('Quantidade de Tinta Nescessario: %dL' %tinta_nescessaria)
    print('Latas de tinta a ser comprada: R$ ',latas_nescessarias)
    print('Valor total das latas: R$ ',latas_nescessarias * latas_tinta_valor)
loja_de_tintas()
        
    