"""3. Classe Retangulo: Crie uma classe que modele um retangulo:
a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, 
    a escolher)
b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular 
    Área e calcular Perímetro;
c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário 
    que informe as medidades de um local. Depois,deve criar um objeto 
    com as medidas e calcular a quantidade de pisos e de rodapés 
    necessárias para o local.
"""
class Retangulo:

    def __init__(self, base=None, altura=None):
        self.base = base
        self.altura = altura

    def mudarValorLados(self):
        print('Valores Atuais Base {}, Atura {}'.format(self.base,self.altura))
        base = float(input("Digite o novo valor da Base: "))
        altura =  float(input("Digite o novo valoo do Lado: "))
        self.base = base
        self.altura = altura
        print('Valores Atualizados Base {}, Atura {}'.format(self.base,self.altura))

    def retornarValorLados(self):
        print('Valores Atuais Base {}, Atura {}'.format(self.base,self.altura))

    def calcularArea(self):
        area = self.base * self.altura
        return area

    def calcularPerimetro(self):
        perimetro = (self.base * 2) + (self.altura * 2)
        return perimetro

    
"""
c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário 
que informe as medidades de um local. Depois, deve criar um objeto com 
as medidas e calcular a quantidade de pisos e de rodapés necessárias 
para o local.
"""
while True:
    print("\n\nDigite as Medias do local")
    base = float(input("Digite a Base: "))
    altura = float(input("Digite a Altura: "))

    medidas = Retangulo(base, altura)

    #Piso medio 45 cm
    piso = 0.45

    #quantidade de pisos 
    #Arela do local
    area = medidas.calcularArea()

    #calculo do Piso
    # (Area do local  / (metro quadrado do piso)) + 10 Porcento de Ajuste
    qtde_piso = (area / (piso**2)) + ((area / (piso**2)) * 0.10)

    #quantidade de rodapés  
    #Dimienções do Rodape definidas como 45 x 15 por padrão
    #area do rodape
    area_rodape = ((base * 0.15) + (altura * 0.15)) * 2

    #quantidade de pisos
    qtde_piso_rodape = (area_rodape / (piso * 0.15)) / 3
    #ajuste de 10 por centos
    qtde_piso_rodape = qtde_piso_rodape + (qtde_piso_rodape * 0.10)

    print("\nMedidas Recebidas:")
    print(' Base: {}m, Altura: {}m'.format(base,altura))
    print(' Area do Local: {}m², Qtde de Pisos: {}'.format(round(area,2), int(qtde_piso)))
    print(' Area do Rodape: {}m², Qtde de Pisos: {}'.format(round(area_rodape,2),int(qtde_piso_rodape)))
    