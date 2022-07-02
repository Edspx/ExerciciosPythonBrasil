'''40. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
seguintes dados:
a. Código da cidade;
b. Número de veículos de passeio (em 1999);
c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
e. Qual a média de veículos nas cinco cidades juntas;
f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.'''

def estatistica_cidades():
    cod = []
    num_veic = []
    num_acid = []

    while len(cod) < 5:
        cod.append(int(input('{}ª Cidade Codigo : '.format(len(cod)+1))))
        num_veic.append(int(input('{}ª Cidade Numero de Veiculos: '.format(len(num_veic)+1))))
        num_acid.append(int(input('{}ª Cidade Numero de Acidentes: '.format(len(num_acid)+1))))

    index_trans_min, index_trans_max = num_veic.index(min(num_veic)),num_veic.index(max(num_veic))
    media_veic = sum(num_veic) / len(num_veic)

    cid_menor_2mil = []
    for i in range(len(num_veic)):
        qtde = num_veic[i]
        if qtde < 2000:
            cid_menor_2mil.append(qtde)

    media_cid_menor_2mil = sum(cid_menor_2mil) / len(cid_menor_2mil)

    print('\nO Maior índice de Acidente de carro é: {} e O codigo da Cidade é: {}'.format(num_acid[index_trans_max],cod[index_trans_max]))
    print('O Menor índice de Acidente de carro é: {} e O codigo da Cidade é: {}'.format(num_acid[index_trans_min],cod[index_trans_min]))
    print('A media de Veiculos nas cinco cidade é: {}'.format(media_veic))
    print('A Media de acidente de trasito nas cidades com Menos de 2mil habitantes é: {}'.format(media_cid_menor_2mil))
    print('\n')
estatistica_cidades()


    
        