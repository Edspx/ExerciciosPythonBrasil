"""4. Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
F
FU
FUL
FULA
FULAN
FULANO"""

while True:

    nome = input('\nDigite seu Nome: ')
    for i in range(len(nome)+1):
        print(nome[0:i].upper())