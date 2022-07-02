'''44. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos
utilizados são:
1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
'''
def eleicao():
    #Criando lista de Canditados
    candidatos = ['Jose', 'João', 'Maria', 'Lucia', 'Voto Nulo', 'Voto em Branco']

    #Populando lista com codigo, e lista de votos para receber contagem de votos.
    codigo = []
    votos = []
    for i in range(len(candidatos)):
        codigo.append(i+1)
        votos.append(0)

       #Setando valar aleatorio de entrada de variavel
    voto = 10
    #Coletando Votos
    while voto != 0:
        voto = int(input('Digite:\n 1 - Jose\n 2 - João\n 3 - Maria\n 4 - Lucia\n 5 - Voto Nulo\n 6 - Voto em Branco\nDigite seu Voto: '))
        if voto > 0 and voto <= len(candidatos):
            votos[voto - 1] += 1
        else:
            print('Voto Invalido')

        #Acompanhamento da Votação
        print(votos)

    #Resultado
    print('\nResultado')
    for i in range(len(candidatos)):
        print('{} - {}: {} Votos - {}%'.format(codigo[i],candidatos[i],votos[i],votos[i]/sum(votos)))

eleicao()

    
