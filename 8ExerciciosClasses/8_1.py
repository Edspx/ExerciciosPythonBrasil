"""1. Classe Bola: Crie uma classe que modele uma bola:
a. Atributos: Cor, circunferência, material
b. Métodos: trocaCor e mostraCor"""

# Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor=None, circunferencia=0, material=None):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def mostraCor(self):
        return self.cor

    def trocaCor(self):
        print('Cor Atual: ', self.cor)
        nova_cor = input('Digite a nova cor: ')
        self.cor = nova_cor
        print('Nova Cor: ',self.cor)

x = Bola("Branco", 5, "metal")
print(x.mostraCor())
x.trocaCor()
print(x.mostraCor())
print(x.cor, x.circunferencia, x.material)

    
