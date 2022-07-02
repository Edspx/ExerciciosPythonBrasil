#EstruturaDeRepeticao
#29/08/2020 EstruturaDeRepeticao - PythonBrasil
#https://wiki.python.org.br/EstruturaDeRepeticao 3/5

'''1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.'''
def nota_valida():
    nota = int(input('Digite uma nota de 0 a 10: '))
    while nota < 0 or nota > 10:
        nota = int(input(' Nota fora do padrão, Digite uma nota de 0 a 10: '))
    print('\n A nota digitada e: ',nota)
nota_valida()
        

'''2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
uma mensagem de erro e voltando a pedir as informações.'''
def user_senha():
    user =  input('Usuario: ')
    passwd = input('senha: ')
    
    while user == passwd:
        print('Erro a senha não pode ser igual ao nome de usuario:')
        user =  input('Usuario: ')
        passwd = input('senha: ')
    print('Usuario e senha OK')
user_senha()
        


'''3. Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';'''
def avaliar_informacoes():
    nome = input('Nome: ')
    while len(nome) <= 3:
        nome = input('Nome tem que conter acima de 3 caracteres\nNome: ')
        
    idade = int(input('Idade: '))
    while idade < 0 or idade > 150:
        idade = int(input('Idade tem que ser entre 0 e 150 anos.\n Idade: '))
        
    salario = float(input('Salario: '))
    while salario <= 0:
        salario = float(input('Salario tem que ser maior que Zero.\nSalario: R$'))
        
    sexo = input('Sexo: ')
    while sexo not in ('f','m'):
        sexo =  input('Digite f-minino ou m-masculino.\nSexo: ')
        
    estado_civil = input('Estado Civil: ')
    while estado_civil not in ('s', 'c', 'v', 'd'):
        estado_civil = input('Estado Civil fora do padrao digite\n s-olteiro\n c-asado\n v-iuvo\n d-ivorciado\nEstado Civil: ')
        
    print('\nDados digitados Validados')
    print(' Nome: {}\n Idade: {}\n Salario: {}\n Sexo: {}\n Estado Civil: {}'
          .format(nome,idade,salario,sexo,estado_civil))
avaliar_informacoes()

'''4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e
que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.'''
def aumento_polulacao():
    A = 80000
    B = 200000
    tx_cresc_A = 0.03
    tx_cresc_B = 0.015
    anos = 0
    #print(anos, A,B)
    while A < B:
        A = A * tx_cresc_A + A
        B = B * tx_cresc_B + B
        anos = anos + 1
        #print(i, int(A),int(B))
    print('São {}, a  quantidade de anos que o \nPais A {} precisara para ultrapassar o \nPais B {}.'.format(anos,int(A),int(B)))
aumento_da_polulacao()



'''5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a
entrada e permita repetir a operação.'''
def aumento_populacionalV2():
    pais_A = int(input('Qual a População do Pais A: '))
    taxa_cresci_A = float(input('Qual a Taxa de Crescimento do Pais A: '))
    pais_B = int(input('Qual a População do Pais B: '))
    taxa_cresci_B = float(input('Qual a Taxa de Crescimento do Pais B: '))
    anos = 0
    
    if pais_A < pais_B:
        while pais_A < pais_B:
            pais_A = pais_A * taxa_cresci_A/100  + pais_A
            pais_B = pais_B * taxa_cresci_B/100  + pais_B
            anos += 1
        print('São {}, a  quantidade de anos que o \nPais A {} precisara para ultrapassar o \nPais B {}.'.format(anos,int(pais_A),int(pais_B)))
        
        
    else:
        print('O pais A com {} já e maior que o pais B com {} habitantes'.format(pais_A,pais_B))
aumento_populacionalV2()
    
    

'''6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que
ele mostre os números um ao lado do outro.'''
def order_numeros():
    for i in range(20):
        print(i+1)
order_numeros()

def order_numeros():
    for i in range(20):
        print(i+1, end=' ')
order_numeros()


'''7. Faça um programa que leia 5 números e informe o maior número.'''
def mostrar_o_maior_numero():
    numero = []
    while len(numero) < 5:
        numero.append(int(input('Digite o numero {}:  '.format(len(numero)+1))))
        
    lista_ordenada = sorted(numero)
    lista_decresente = lista_ordenada[::-1]
    maior_numero = lista_decresente[0]
    
    print('\n O maior numero digitado é:  ',maior_numero)
mostrar_o_maior_numero()
    


'''8. Faça um programa que leia 5 números e informe a soma e a média dos números.'''
def soma_e_media():
    numero = []
    while len(numero) < 5:
        numero.append(int(input('Digite o Numero {}:  '.format(len(numero)+1))))
        
    soma = sum(numero)
    media = soma / len(numero)
    
    print('\nA Soma é: {}\nA media é: {}'.format(soma,media))
soma_e_media()


'''9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.'''
def imprimir_impares():
    numero = 0
    while numero < 50:
        if numero%2 != 0:
            print(numero, end=' ')
        numero += 1
imprimir_impares()
        
    

'''10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por
eles.'''
def intervalo_de_numeros_inteiros():
    entrada = []
    while len(entrada) < 2:
        entrada.append(int(input('Digite o {}º Numero: '.format(len(entrada)+1))))
        
    entrada = sorted(entrada)
    num1,num2 = entrada[0], entrada[1]
    
    while num1 < (num2 - 1):
        entrada.append(num1+1)
        num1 += 1
        
    print(sorted(entrada))
intervalo_de_numeros_inteiros()
        


'''11. Altere o programa anterior para mostrar no final a soma dos números.'''
def intervalo_de_numeros_inteiros():
    entrada = []
    while len(entrada) < 2:
        entrada.append(int(input('Digite o {}º Numero: '.format(len(entrada)+1))))
        
    entrada = sorted(entrada)
    num1,num2 = entrada[0], entrada[1]
    
    while num1 < (num2 - 1):
        entrada.append(num1+1)
        num1 += 1
        
    print( sorted(entrada),"\nSoma: ",sum(entrada))
intervalo_de_numeros_inteiros()

'''12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve
informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50'''
def tabuada():
    while True:
        tabuada = int(input('Digite a Tabuada desejada: '))
        inteiro = 0
        resultado = 0
        while inteiro <= 10:
            print('{} X {} = {}'.format(inteiro,tabuada,inteiro*tabuada))
            inteiro += 1
tabuada()
        


'''13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo
número. Não utilize a função de potência da linguagem.'''
def elevado():
    base = int(input('Digite o numero Base: '))
    expoente = int(input('Digite o numero expoente: '))
    loop = 0
    result = base
    while loop < (expoente - 1):
        result = result * base
        loop += 1
        
    return result
elevado()

'''14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
números impares.'''
def pares_e_impares():
    numeros = []
    par = []
    impar = []
    print('Digite 10 numeros inteiros')
    while len(numeros) < 10:
        numeros.append(int(input('Digite o {}º Numero: '.format(len(numeros)+1))))
    
    loop = len(numeros)
    for i in range(len(numeros)):
        resto = numeros[i]%2
        if resto == 0:
            par.append(numeros[i])
        else:
            impar.append(numeros[i])
    
    print('\nNumeros Pares: {}, sendo: {}'.format(len(par),par[:]))
    print('Numeros Impares: {}, sendo: {}'.format(len(impar),impar[:]))
pares_e_impares()


'''15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o
n−ésimo termo.'''
def fibonacci():
    termo = int(input('Digite o termo para gerar a serie: '))
    a, b = 0,1
    
    while b <= termo:
        a, b = b, a+b
        print(a, end=' ')
fibonacci()
    

'''16. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o
valor seja maior que 500.'''
def fibonacci():
    termo = 500
    a, b = 0,1
    
    while b <= termo:
        a, b = b, a+b
        print(a, end=' ')
    a, b = b, a+b
    print(a, end=' ')
fibonacci()

'''17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120'''
def fatorial():
    num = int(input('Digite um numero para Fatorar: '))
    fator = num
    loop = num - 1
    print(fator, end='!=')

    while fator > 1:
        num = num*loop
        print(fator, end='.')
        fator -= 1
        loop -= 1
    print(fator, end='')
    print(' =',num)
fatorial()


'''18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.'''
def conjuntoN():
    num = []
    conjunto = []
    while True:
        if 'n' in num:
            break
        else:
            num.append(input('Digite n-ão para parar ou Digite um numero: '))
    num.pop(-1)
    for i in range(len(num)):
        conjunto.append(int(num[i]))
    conjunto = sorted(conjunto)

    menor, maior, soma = conjunto[0], conjunto[-1],sum(conjunto)
    print('Dos numero, ',num)
    print('O menor: {}\nO maior: {}\nA soma: {}'.format(menor, maior, soma))
conjuntoN()
        

'''19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.'''
def conjunto_n_0_1000():
    num = []
    conjunto = []
    while True:
        num.append(input('Digite n-ão para sair ou Digite um numero de 0 a 1000: '))
        if 'n' in num:
            num.pop(-1)
            break
        else:
            if int(num[-1]) >= 0 and int(num[-1]) <= 1000:
                conjunto.append(int(num[-1]))
            else:
                print('O numero {} e invalido'.format(int(num[-1])))
    num = conjunto
    conjunto = sorted(conjunto)
           
    menor, maior, soma = conjunto[0], conjunto[-1],sum(conjunto)
    print('Dos numero, ',num)
    print('O menor: {}\nO maior: {}\nA soma: {}'.format(menor, maior, soma))
conjunto_n_0_1000()      

'''20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a
números inteiros positivos e menores que 16.'''
def fatorial_v2():
    try:
        while True:
            num = int(input('Digite um numero para fatorar: '))
            if num > 0 and num <= 16:
                loop = num
                fator = num -1
                print(num, end='!=')
                while loop > 1:
                    num = num*fator
                    print(loop, end='.')
                    loop -= 1
                    fator -= 1
                print(loop,'=',num)
            else:
                if num < 0:
                    print('Fator tem que ser positivo e menor que dezesseis')
                else:
                    print('Fator limite de dezesseis apenas')
    except:
        print('Fatorial Finalizado!!!!!')
fatorial_v2()
        
            
        
'''21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele
que é divisível somente por ele mesmo e por 1.'''
def numero_primo():
    try:
        while True:
            num = int(input('Digite um numero: '))
            loop = num - 1
            
            while loop > 1:
                resto = num%loop
                if resto == 0:
                    print('{} Não é Primo'.format(num))
                    break         
                loop -= 1
            if loop == 1:
                print('{} É Primo'.format(num))
    except:
        print('Numero Primo Finalizado!!!!')
numero_primo()



'''22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é
divisível.'''
def numero_primo_v2():
    divisivel = []
    try:
        while True:
            num = int(input('Digite um numero: '))
            loop = num - 1
            divisivel = []
            while loop > 1:
                resto = num%loop
                if resto == 0:
                    divisivel.append(loop)
                loop -= 1
            
            if len(divisivel) >= 1:
                print('{} Não é Primo, ele e divisivel por: {}'.format(num,divisivel))    
            if len(divisivel) == 0:
                print('{} É Primo, ele e divisivel por 1 e por Ele mesmo'.format(num))
    except:
        print('Numero Primo Finalizado!!!!')
numero_primo_v2()


'''23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.'''
def numero_primo_v3():

    try:
        while True:
            num = int(input('Digite um numero: '))
            dividendo = num
            divisor = dividendo - 1
            qtde_divisao = 0
            primo = []
            while dividendo >= 1:
                divisivel = []
                composto = []
                while divisor > 1:
                    resto = dividendo%divisor
                    qtde_divisao += 1
                    if resto == 0:
                        divisivel.append(divisor)
                    divisor -= 1
                
                if len(divisivel) >= 1:
                    #print('{} Não é Primo, ele e divisivel por: {}'.format(num,divisivel))
                    composto.append(dividendo)
                if len(divisivel) == 0:
                    #print('{} É Primo, ele e divisivel por 1 e por Ele mesmo'.format(dividendo))
                    primo.append(dividendo)
                dividendo -= 1
                divisor = dividendo - 1
            print('Até o numero {}\n os Primos são {}\n Total de divisoes: {}'.format(num,primo,qtde_divisao))
    except:
        print('Numero Primo Finalizado!!!!')
numero_primo_v3()


'''24. Faça um programa que calcule o mostre a média aritmética de N notas.'''
def media_aritimetica():
    num = []
    try:
        while True:
            num.append(float(input('Digite o numero para compor a media: ')))
            media = sum(num) / len(num)
            print('A Media de {} é {}'.format(num,round(media,2)))
    except:
        print('media_aritimetica Finalizada!!!')
media_aritimetica()


'''25. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média
29/08/2020 EstruturaDeRepeticao - PythonBrasil
https://wiki.python.org.br/EstruturaDeRepeticao 2/5
calculada.'''
def media_idade():
    num = []
    try:
        while True:
            num.append(int(input('Digite a Idade: ')))
            media = sum(num) / len(num)
            
            if media > 0 and media <= 25:
                print('Turma Jovem')
            elif media >= 26 and media <= 60:
                print('Turma Adulta')
            elif media > 60:
                print('Turma Idosa')
        
    except:
        print('media_idade Finalizado!!!!')
media_idade()


'''26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
votar e ao final mostrar o número de votos de cada candidato.'''
  
import random 
def eleicao():
    try:
        while True:
            cand1 = 0
            cand2 = 0
            cand3 = 0
            
            total_votos = int(input('Qual o total de votos: '))
            
            while total_votos > 0:
                voto = random.randrange(3)+1
                if voto == 1:
                    cand1 += 1
                elif voto == 2:
                    cand2 += 1
                elif voto == 3:
                    cand3 += 1
                total_votos -= 1
        
            print('Votos entre os candidatos\n Candidato 01 : {}\n Candidato 02 : {}\n Candidato 03 : {}'.format(cand1,cand2,cand3))
    except:
        print('Eleicao Finalizada!!!!!')
eleicao()


'''27. Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.'''
def media_por_turma():
    turmas = int(input('Digite a quantidade de Turmas: '))
    alunos = []
    i = 1
     
    while turmas > 0:
        alunos.append(int(input('Digite a Quantidade de alunos da {}ª Turma: '.format(i))))
        while alunos[-1] > 40 and turmas > 0:
            alunos.pop(-1)
            alunos.append(int(input('Turmas não podem ter mais que 40 Alunos\nDigite a Quantidade de alunos da {}ª Turma: '.format(i))))
        turmas -= 1
        i += 1
        
    media = sum(alunos) / len(alunos)
    print('A media por turma é: ',round(media,2))
media_por_turma()
        




'''28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto
em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''
def colecionador_cds():
    colecao = int(input('Qual o total de cds da coleção: '))
    total_cds = colecao
    precos = []
    while total_cds > 0:
        precos.append(float(input('Digite o Preço do {}ª cd: '.format(len(precos)+1))))
        total_cds -= 1
        
    soma = sum(precos)
    media = soma / len(precos)
    
    print('\n A quantidade de cds é {} custando um total de R${} e a media de preço é R${}'.format(colecao,round(soma,2),round(media,2)))
colecionador_cds()
        

'''29. O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de
quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado
o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na
tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os
preços de 1 até 50 produtos, conforme o exemplo abaixo:
Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50
'''
def tabela_precos_199():
    try:
        while True:
            qtde = int(input("Digite a Quantidade de produtos da Compra: "))
            preco_uni = 1.99
            loop = qtde
            i = 1
            if qtde <= 50:
                while loop > 0:
                    print('{} - R$ {}'.format(i,i*preco_uni))
                    i += 1
                    loop -= 1
            else:
                print('Quantidade Maxima de Itens é 50')
    except:
        print('Finalizado!!!')
tabela_precos_199()
        
'''30. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um
sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1
até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00'''
def tabela_precos_pao():
    try:
        while True:
            qtde = int(input("Digite a Quantidade de Paes: "))
            preco_uni = 0.18
            loop = qtde
            i = 1
            if qtde <= 50:
                while loop > 0:
                    print('{} - R$ {}'.format(i,round(i*preco_uni,2)))
                    i += 1
                    loop -= 1
            else:
                print('Quantidade Maxima de paes é 50')
    except:
        print('Finalizado!!!')
tabela_precos_pao()



'''31. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número
desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para
indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente
forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...
'''
def caixa_conveniencia():
    try:
        while True:
            produtos = []
            produtos.append(float(input('Digite o Preço do {}ª Produto: '.format(len(produtos)+1))))
            while produtos[-1] != 0:
                produtos.append(float(input('Digite o Preço do {}ª Produto: '.format(len(produtos)+1))))
                
            total = sum(produtos)
            print('Total: R$ {}'.format(total))
            pagamento = float(input('Dinheiro: '))
            troco = pagamento - total
            print('\n')
            for i in range(len(produtos)):
                print('Produto {}: R$ {}'.format(i+1,produtos[i]))
                
            print('Total: R$ {}'.format(total))
            print('Dinheiro: R$ {}'.format(pagamento))
            print('Troco: R$ {}'.format(troco))
    except:
        print('Finalizado!!!')
caixa_conveniencia()
    
    


'''32. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve
ser conforme o exemplo abaixo:
Fatorial de: 5
5! = 5 . 4 . 3 . 2 . 1 = 120'''
def fatorial_32():
    try:
        while True:
            fator =  int(input('Fator: '))
            loop = fator
            result = fator
            
            print('Fatorial de: ',fator)
            print(fator,end = '! = ')
            
            while loop > 1:
                result = result * (loop - 1)
                print('{}'.format(loop), end=' . ')
                loop -= 1
                
            print('{}'.format(loop), end=' = ')
            print(result)
    except:
        print('Finalizado!!!')
fatorial_32()
    

'''33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das
temperaturas.'''
def temperatura():
    try:
        while True:
            try:
                temperatura = []
                temp = []
                while True:
                    temp = int(input('Temperatura {}: '.format(len(temperatura)+1)))
                    if temp >= 0 :
                        temperatura.append(temp)
                    else:
                        print('Apenas Temperaturas')
            except:
                temperatura_ordenada = sorted(temperatura)
                temp_min, temp_max = temperatura_ordenada[0], temperatura_ordenada[-1]
                media = sum(temperatura) / len(temperatura)
                
                print('\n Temperatura\n  Minima: {}\n  Maxima: {}\n  Media: {}'.format(temp_min,temp_max,round(media,2)))
    except:
        print('Finalizado!!!')
temperatura()


'''34. Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é
aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele
é ou não um número primo.'''
def primo_34():
    try:
        while True:
            num = int(input('Numero: '))
            divisor = num - 1
            resto = 1
            while divisor > 1:
                resto = num%divisor
                if resto == 0:
                    print('{} Não é Primo'.format(num))
                    break
                divisor -= 1
            if resto == 1:
                print('{} é Primo'.format(num))
    except:
        print('Finalizado!!!')    
primo_34()     
    
    

'''35. Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre
1 e um número inteiro informado pelo usuário.'''
def numero_primo_35():

    try:
        while True:
            num = int(input('Numero: '))
            dividendo = num
            divisor = dividendo - 1
            qtde_divisao = 0
            primo = []
            while dividendo >= 1:
                divisivel = []
                composto = []
                while divisor > 1:
                    resto = dividendo%divisor
                    qtde_divisao += 1
                    if resto == 0:
                        divisivel.append(divisor)
                    divisor -= 1
                
                if len(divisivel) >= 1:
                    #print('{} Não é Primo, ele e divisivel por: {}'.format(num,divisivel))
                    composto.append(dividendo)
                if len(divisivel) == 0:
                    #print('{} É Primo, ele e divisivel por 1 e por Ele mesmo'.format(dividendo))
                    primo.append(dividendo)
                dividendo -= 1
                divisor = dividendo - 1
            print('Até o numero {}\n os Primos são {}\n Total de divisoes: {}'.format(num,sorted(primo),qtde_divisao))
    except:
        print('Numero Primo Finalizado!!!!')
numero_primo_35()



'''36. Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada
não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário,
conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7
Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.'''
def tabuada_36():
    while True:
        tabuada = int(input('Tabuada: '))
        comeca = int(input('Começa: '))
        termina = int(input('Termina: '))
        
        if termina > comeca:
            print('Vou mantar a tabuada de {} começando em {} e terminado em {}:'.format(tabuada,comeca,termina))
            while comeca <= termina:
                print('{} X {} = {}'.format(tabuada,comeca, tabuada*comeca))
                comeca += 1
        else:
            print('O inicio tem que ser menor do que termino')
tabuada_36()

'''37. Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e
seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o
programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais
magro, além da média das alturas e dos pesos dos clientes'''
def academia():
    codigo = 1
    codigo_aluno = []
    altura_aluno = []
    peso_aluno = []
        
    while codigo != 0:
        #codigo?
        codigo = int(input('Codigo: '))
        if codigo == 0:
            break
        else:
            codigo_aluno.append(codigo)
            #altura?
            altura = int(input('Altura: '))
            altura_aluno.append(altura)
            #peso?
            peso = int(input('Peso: '))
            peso_aluno.append(peso)
            
        print(codigo_aluno,altura_aluno,peso_aluno)
    mais_alto_index = altura_aluno.index(max(altura_aluno))
    mais_baixo_index = altura_aluno.index(min(altura_aluno))
    mais_gordo_index = peso_aluno.index(max(peso_aluno))
    mais_magro_index = peso_aluno.index(min(peso_aluno))
    
    media_altura = sum(altura_aluno) / len(altura_aluno)
    media_peso = sum(peso_aluno) / len(peso_aluno)
    print('O cliente mais Alto é {} com altura de {}'.format(codigo_aluno[mais_alto_index],altura_aluno[mais_alto_index]))
    print('O cliente mais Bairo é {} com altura de {}'.format(codigo_aluno[mais_baixo_index],altura_aluno[mais_baixo_index]))
    print('O cliente mais Gordo é {} com peso de {}'.format(codigo_aluno[mais_gordo_index],peso_aluno[mais_gordo_index]))
    print('O cliente mais Magro é {} com peso de {}'.format(codigo_aluno[mais_magro_index],peso_aluno[mais_magro_index]))
    print('A media das Alturas é {}\nA media dos Pesos é {}'.format(media_altura,media_peso))
academia()

'''38. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo
que o usuário digite o salário inicial do funcionário.'''
def reajuste_salario():
    salario = float(input('Digite o Salario inicial: '))
    reajuste = 1.5
    inicio = 1995
    fim = 2020
    while inicio < fim :
        salario_corrigido = salario + (salario * (reajuste / 100))
        print('Ano: {}, Salario: {}, Percentual {}'.format(inicio+1,round(salario_corrigido,2),reajuste))
        inicio += 1
        reajuste = reajuste * 2
reajuste_salario()
    

'''39. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto
e o número do aluno mais baixo, junto com suas alturas.'''
def altura_aluno():
    num_aluno = []
    alt_aluno = []
    for i in range(10):
        num_aluno.append(int(input('Digite o Codigo do {}º Aluno :'.format(i + 1))))
        alt_aluno.append(int(input('Digite a Altura do {}º Aluno :'.format(i + 1))))
         
    mais_alto,mais_baixo = alt_aluno.index(max(alt_aluno)),alt_aluno.index(min(alt_aluno))
    print('\nO aluno mais Alto é o Numero {} e sua Altura é {}'.format(num_aluno[mais_alto],alt_aluno[mais_alto]))
    print('O aluno mais Baixo é o Numero {} e sua Altura é {}'.format(num_aluno[mais_baixo],alt_aluno[mais_baixo]))
altura_aluno()
         




'''40. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
seguintes dados:
a. Código da cidade;
b. Número de veículos de passeio (em 1999);
c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
e. Qual a média de veículos nas cinco cidades juntas;
f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.'''
'''41. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor
dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
1 0
3 10
6 15
9 20
12 25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela
R$ 1.000,00 0 1 R$ 1.000,00
R$ 1.100,00 100 3 R$ 366,00
R$ 1.150,00 150 6 R$ 191,67'''
'''42. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número
negativo.'''
'''43. O cardápio de uma lanchonete é o seguinte:
Especificação Código Preço
Cachorro Quente 100 R$ 1,20
Bauru Simples 101 R$ 1,30
Bauru com ovo 102 R$ 1,50
Hambúrguer 103 R$ 1,20
Cheeseburguer 104 R$ 1,30
Refrigerante 105 R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser
pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido
deve ser encerrado.'''
'''44. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos
utilizados são:
1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)'''
'''5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
29/08/2020 EstruturaDeRepeticao - PythonBrasil
https://wiki.python.org.br/EstruturaDeRepeticao 4/5
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
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
dos alunos usarem o programa.'''
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
'''47. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua
nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos
sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima
informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados
ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7
Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04'''
'''48. Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
29/08/2020 EstruturaDeRepeticao - PythonBrasil
https://wiki.python.org.br/EstruturaDeRepeticao 5/5
12376489
=> 98467321'''
'''49. Faça um programa que mostre os n termos da Série a seguir:
S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.'''
'''50. Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.'''
'''51. Faça um programa que mostre os n termos da Série a seguir:
S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.'''
