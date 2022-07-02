
'''7.Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.'''
def area_do_quadrado_mostrando_o_dobro():
    lado = float(input('Medita de um dos lados do Quadrado: '))
    area = float(lado**2)
    dobro_area = area*2
    print ('O lado e %.2fcm a Área é %.2fcm² e o Dobro da Área é %.2fcm²' %(lado,area,dobro_area ))
area_do_quadrado_mostrando_o_dobro()