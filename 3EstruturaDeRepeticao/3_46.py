'''46. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o
melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer
um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos
saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma
lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa
deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m
Melhor salto: 6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m
Resultado final:
Rodrigo Curvêllo: 5.9 m'''

def atleta_saltos():
    nome = input('\n\nInforme o Nome do Atleta: ')
    if nome != '':
        ordinal = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
        notas = []
        notas_validas = []
        for i in range(len(ordinal)):
            notas.append(float(input('Digite a {}ª Nota: '.format(len(notas)+1))))

        notas_validas = notas[:]
        notas_validas.pop(notas_validas.index(max(notas_validas)))
        notas_validas.pop(notas_validas.index(min(notas_validas)))

        media = sum(notas_validas)/len(notas_validas)

        print('\n\nAtleta: ', nome)
        for i in range(len(notas)):
            print('{} Salto: {} m'.format(ordinal[i], notas[i]))
        print('Melhor Salto: ',max(notas))
        print('Pior Salto: ',min(notas))
        print('Resultado Final:\n{}: {} m\n\n'.format(nome,round(media,2)))

    else:
        print('\nE nescessario a entrada de um nome para Iniciar\n\n')

atleta_saltos()
