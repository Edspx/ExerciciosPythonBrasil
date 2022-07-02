"""
2. Classe Quadrado: Crie uma classe que modele um quadrado:
a. Atributos: Tamanho do lado
b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""
class Quadrado:

    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudarValorlado(self):
        print('Valor do Lado Atual em Cm: ',self.tamanho_lado)
        lado = float(input('Digite o Novo Valor: '))
        self.tamanho_lado = lado
        print('Valor do Lado Atualizado para: {} cm '.format(self.tamanho_lado))


    def calcularArea(self):
        area = self.tamanho_lado * self.tamanho_lado
        return area

x = Quadrado(2)
print('O valor da Area do Quadrado é ',x.calcularArea())

x.mudarValorlado()
print('O valor da Area do Quadrado é ',x.calcularArea())