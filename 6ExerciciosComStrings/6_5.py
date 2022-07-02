"""5. Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
FULANO
FULAN
FULA
FUL
FU
F"""

while True:

    nome = input('\nDigite seu Nome: ')
    print(nome[:].upper())
    for i in range(len(nome)):
        print(nome[:-(i+1)].upper())