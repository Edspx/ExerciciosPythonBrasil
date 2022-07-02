'''
45. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao
aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota
(atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai
utilizar o sistema. Após todos os alunos terem respondido informar:
a. Maior e Menor Acerto;
b. Total de Alunos que utilizaram o sistema;
c. A Média das Notas da Turma.
Gabarito da Prova:
01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes
dos alunos usarem o programa.
'''
def gabarito():
    #Gabarito Padrão
    gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
    #Case queira entrar com outro Gabarito
    gab = input('\n\ndeseja Preencher o Gabarito: S-IM ou N-AO: ')
    if gab == 'S':
        gabarito = []
        print('\nPreencha o Gabarito')

        while gab != 'FIM':
            gab = input('Digite FIM para encerar ou a {}ª Resposta do gabarito: '.format(len(gabarito)+1))
            if gab != 'FIM':
                gabarito.append(gab)
    
    cod_aluno = []
    acertos = []
    #Iniciando Coleta de Dados
    executa = input('\nDeseja Entrar Com as Notas de um Aluno digite S-IM ou N-AO: ')
    while executa == 'S':
        #Pegando referencia do aluno
        cod_aluno.append(int(input('Digite o Codigo do Aluno: ')))
        acerto = 0
        #Pegando suas Notas
        print('\nDigite as Respostas')
        for i in range(len(gabarito)):
            resposta = input('{}ª : '.format(i+1))
            if resposta == gabarito[i]:
                acerto += 1
        acertos.append(acerto)
        executa = input('\nDeseja Entrar Com as Notas de outro Aluno digite S-IM ou N-AO: ')
        #tratando resultado
        maior_acerto = max(acertos)
        menor_acerto = min(acertos)
        total_alunos = len(cod_aluno)
        media_nota_turma = sum(acertos) / len(cod_aluno)
    #Resultado
    print('\nResultado dos Alunos:')
    print(' A Maior nota foi: ',maior_acerto)
    print(' A Menor nota foi: ',menor_acerto)
    print(' O Total de Alunos foram: ',total_alunos)
    print(' A Media da Turma foi: ',round(media_nota_turma,2))
gabarito()



