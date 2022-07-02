'''42. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número
negativo.'''
def contagem():
    numeros = []
    numeros.append(int(input('Digite {}º Numero: '.format(len(numeros)+1))))
    while numeros[-1] >= 0:
        numeros.append(int(input('Digite {}º Numero: '.format(len(numeros)+1))))
        
    numeros.pop(-1)
    I_25 = []
    I26_50 = []
    I51_75 = []
    I76_100 = []
    for i in range(len(numeros)):
        if numeros[i] >= 0 and numeros[i] <= 25:
            I_25.append(numeros[i])

        if numeros[i] >= 26 and numeros[i] <= 50:
            I26_50.append(numeros[i])

        if numeros[i] >= 51 and numeros[i] <= 75:
            I51_75.append(numeros[i])

        if numeros[i] >= 76 and numeros[i] <= 100:
            I76_100.append(numeros[i])
    print('\n') 
    print('intervalos de [0-25]  : ',I_25)
    print('intervalos de [26-50] : ',I26_50)
    print('intervalos de [51-75] : ',I51_75)
    print('intervalos de [76-100]: ',I76_100)
    print('\n')
contagem()