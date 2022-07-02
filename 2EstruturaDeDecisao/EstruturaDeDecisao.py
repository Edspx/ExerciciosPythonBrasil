
 '''1. Faça um Programa que peça dois números e imprima o maior deles. '''
 def qualOMaiorNumero():
     print('1. Faça um Programa que peça dois números e imprima o maior deles.')
     a = int(input('Numero 1: '))
     b = int(input('Numero 2: '))
     if a > b:
         print('O Maior numero é ', a)
     else:
         print('O Maior numero é ', b)
qualOMaiorNumero()

  '''2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.  '''
def positivo_ou_negativo():
    #print('2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo')
    num = float(input('Digite o Numero: '))
    if num > 0:
        pn = 'POSITIVO'
    elif num < 0:
        pn = 'NEGATIVO'
    else:
        pn = 'NEUTRO'
    print('O numero {} e {}'.format(num,pn))
positivo_ou_negativo()
    

  '''3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. '''
def sexo():
    print('3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido')
    sexo = input('Digite o Sexo F - Feminino, M - Masculino: ')
    if sexo in ('F','f'):
        sx = 'FEMININO'
    elif sexo in ('M','m'):
        sx = 'MASCULINO'
    else:
        sx = 'SEXO INVÁLIDO'
    print('O sexo {} digitado e {}'.format(sexo,sx))
sexo()

  '''4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante. '''
def vogal_ou_consoante():
    print('4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.')
    letra = input('Digite uma Letra: ')
    if letra in ('a','e','i','o','u','A','E','I','O','U','Á','á','Â','â','À','à','Å','å','Ã','ã','Ä','ä','Æ','æ','É','é','Ê','ê','È','è','Ë','ë','Ð','ð','Í','í','Î','î','Ì','ì','Ï','ï','Ó','ó','Ô','ô','Ò','ò','Ø','ø','Õ','õ','Ö','ö','Ú','ú','Û','û','Ù','ù','Ü','ü'):
        lt = 'VOGAL'
    else:
        lt = 'CONSOANTE'
    print('A letra digita {} é uma {}'.format(letra,lt))
vogal_ou_consoante()

  '''5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
  * A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
  * A mensagem "Reprovado", se a média for menor do que sete;
  * A mensagem "Aprovado com Distinção", se a média for igual a dez. '''
def media_nota():
    print('5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:')
    notas = []
    for i in range(2):
        notas.append(float(input('Digite a Nota {} : '.format(i+1))))
    media =  sum(notas) / len(notas)
    if media == 10:
        msg = 'Aprovado com distinção'
    elif media > 7:
        msg = 'Aprovado'
    elif media <= 7:
        msg = 'Reprovado' 
    print(' Primeira nota {} \n Segunda nota {} \n Media {} \n O aluno esta {}'.format(notas[0],notas[1],media,msg))
media_nota()


  '''6. Faça um Programa que leia três números e mostre o maior deles.  '''
def qualOMaiorNumero():
    print('6. Faça um Programa que leia três números e mostre o maior deles.')
    num = []
    for i in range(3):
        num.append(float(input('Insira o Numero {}: '.format(i+1))))
    num_sort = sorted(num)
    print('Entre os numeros {} o maior é {}'.format(num,num_sort[2]))
qualOMaiorNumero()
    

  '''7. Faça um Programa que leia três números e mostre o maior e o menor deles.  '''
def qualoMaiorEoMenorNumero():
    print('7. Faça um Programa que leia três números e mostre o maior e o menor deles.')
    num = []
    for i in range(3):
        num.append(float(input('Digite o Numero {}: '.format(i + 1))))
    num_sort = sorted(num)
    print('Entre os Numeros digitados {} o Maior é {}, e o Menor é {}'.format(num,num_sort[2],num_sort[0]))
qualoMaiorEoMenorNumero()

  '''8. Faça um programa que pergunte o preço de três  produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. '''
def compraProduto():
    print('8. Faça um programa que pergunte o preço de três  produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. ')
    preco = []
    for i in range(3):
        preco.append(float(input('Qual o Preço do Produto Numero {}: '.format(i+1))))
    preco_sort = sorted(preco)
    print('Entre os Preços Digitados {} o Menor preço para compra é R${}'.format(preco,preco[0]))
compraProduto()

 ''' 9. Faça um Programa que leia três números e mostre-os em ordem decrescente. '''
def ordemDecrescente():
    print('9. Faça um Programa que leia três números e mostre-os em ordem decrescente.')
    num = []
    for i in range(3):
        num.append(float(input('Digite o Numero {}: '.format(i+1))))
    num_sort = sorted(num)
    #Para esse exercicio resolvi ordenar e inverter a ordenação para criar uma ordem decrescente
    num_decrescente = num_sort[::-1]
    print('Os numeros Digitados foram {} e sua ordem decrescente {}'.format(num,num_decrescente))
ordemDecrescente()
    

  '''10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. '''
def saudacao():
    print('10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. ')
    turno = input('Em que turno você estuda?\n Digite:\n    M-matutino\n    V-Vespertino\n    N- Noturno\n Digite: ')
    if turno in ('M','m'):
        saudacao = 'Bom Dia!'
    elif turno in ('V','v'):
        saudacao = 'Boa Tarde!'
    elif turno in ('N','n'):
        saudacao = 'Boa Noite!'
    else:
        saudacao = 'Valor Inválido!'
    print('{}'.format(saudacao))
saudacao()
    
  '''11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

  Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

  * salários até R$ 280,00 (incluindo)		: aumento de 20%
  * salários entre R$ 280,00 e R$ 700,00	: aumento de 15%
  * salários entre R$ 700,00 e R$ 1500,00	: aumento de 10%
  * salários de R$ 1500,00 em diante 		: aumento de 5%

  Após o aumento ser realizado, informe na tela:

  a. o salário antes do reajuste;
  b. o percentual de aumento aplicado;
  c. o valor do aumento;
  d. o novo salário, após o aumento. '''
def reajusteSalarial():
    print('Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual')
    salarioAtual =  float(input('Qual o seu Salário Atual R$: '))
    print('\n')
    if salarioAtual >= 280:
        reajuste = 20
    elif salarioAtual > 280 and salarioAtual <= 700:
        reajuste = 15
    elif salarioAtual > 700 and salarioAtual <= 1500:
        reajuste = 10
    elif salarioAtual > 1500:
        reajuste = 5
        
    valorReajuste = salarioAtual * reajuste / 100
    salarioNovo = salarioAtual + valorReajuste
    
    print('a. o salário antes do reajuste: R$ {}'.format(salarioAtual))
    print('b. o percentual de aumento aplicado: {}%'.format(reajuste))
    print('c. o valor do aumento: R$ {}'.format(valorReajuste))
    print('d. o novo salário, após o aumento: R$ {}'.format(salarioNovo))
reajusteSalarial()
    
    

  '''12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS 
  corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
  O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês. 

  Desconto do IR:
  * Salário Bruto até 900  (inclusive)   - isento    
  * Salário Bruto até 1500 (inclusive)	- desconto de 5%
  * Salário Bruto até 2500 (inclusive)	- desconto de 10%
  * Salário Bruto acima de 2500     	- desconto de 20% 

  Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
  {{{
	Salário Bruto: (5 * 220) 	: R$ 1100,00
    (-) IR (5%)			        : R$   55,00  
	(-) INSS ( 10%)		        : R$  110,00
	FGTS (11%)			        : R$  121,00
	Total de descontos		    : R$  165,00
	Salário Liquido	            : R$  935,00
  }}} '''
def folhaPagamento():
    print('12. Faça um programa para o cálculo de uma folha de pagamento')
    valorHora = float(input('Qual o Valor da Sua Hora de Trabalho: R$ '))
    horasDeTrabalho = float(input('Quantas Horas trabalhadas esse Mes: '))
    salarioBruto = valorHora * horasDeTrabalho
    if salarioBruto <= 900:
        descontoIR = 0
    elif salarioBruto > 900 and salarioBruto <= 1500:
        descontoIR = 5
    elif salarioBruto > 1500 and salarioBruto <= 2500:
        descontoIR = 10
    elif salarioBruto > 2500:
        descontoIR = 20
        
    valorDescontoIR = salarioBruto * descontoIR / 100
    inss = salarioBruto*0.10
    fgts = salarioBruto*0.11
    totalDesc = valorDescontoIR + inss
    salarioLiguido = salarioBruto - totalDesc
    
    print('\n')
    print('Salário Bruto: ({} * {}) : R$ {}\n (-) IR ({}%)  : R$ {}\n (-) INSS ( 10%) : R$ {}\n FGTS (11%) : R$ {} \n Total de descontos : R$ {}\n Salário Liquido : R$ {}'.format(horasDeTrabalho,valorHora,salarioBruto,descontoIR,valorDescontoIR,inss,fgts,totalDesc,salarioLiguido))
folhaPagamento()
        
    

  '''13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. '''
def diaSemana():
    print('13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. ')
    dia = int(input('Digite um numero de de 1 a 7: '))
    semana = ['','Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sabado']
    if dia >= 1 and dia <= 7:
        print('O dia da Semana Correspondenden é {}'.format(semana[dia]))
    else:
        print('Numero não listado')
diaSemana()

  '''14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: 

  {{{
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0	  A
  Entre 7.5 e 9.0	  B
  Entre 6.0 e 7.5	  C
  Entre 4.0 e 6.0	  D
  Entre 4.0 e zero	  E
  }}}

  O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. '''
def mediaAluno():
    print('14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:')
    nota = []
    for i in range(2):
        nota.append(float(input('Digite a Nota {}: '.format(i+1))))
    
    media = sum(nota) / len(nota)
    
    if media >= 9 and media <= 10: 
        conceito = 'A'
    if media >= 7.5 and media < 9: 
        conceito = 'B'
    if media >=  6  and media < 7.5: 
        conceito = 'C'
    if media >=  4  and media < 6: 
        conceito = 'D'
    if media < 4:
        conceito = 'E'
        
    if conceito in ('A','B','C'):
        mensagem =  'APROVADO'
    else:
        mensagem = 'REPROVADO'
        

    print(' Notas:\n  Nota1: {}\n  Nota2: {}\n Media: {}\n Conceito: {}\n Aluno: {}'.format(nota[0],nota[1],media,conceito,mensagem))
mediaAluno()


 ''' 15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
 Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 
   Dicas:
   a. Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
   a. Triângulo Equilátero: três lados iguais;
   a. Triângulo Isósceles: quaisquer dois lados iguais;
   a. Triângulo Escaleno: três lados diferentes; '''
def triangulo():
    print('15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.')
    lado = []
    for i in range(3):
        lado.append(float(input('Digito {}º Lado: '.format(i+1))))
    if (lado[0] + lado[1]) > lado[2]:
        #verificando Equilátero
        mediaLado = sum(lado) / len(lado)
        if ((mediaLado == lado[0]) and (mediaLado == lado[1]) and (mediaLado == lado[2])):
            print('É um Trigando Equilátero')
        else:
        #verificando lados iguais
            ocorrencia = 0
            for i in range(3):
                for j in range(3):
                    if lado[i] == lado[j]:
                        ocorrencia = ocorrencia + 1
                        if ocorrencia == 2:
                            break
                break
            if ocorrencia == 2:
                print('É um Triangulo Isosceles')
            else:
                print('É um triangulo Escaleno')
    else:
        print('Não é um Triangulo')
triangulo()


  '''16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
  O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

  a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
  b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
  c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
  d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; '''
def equacaoDoSegundoGrau():
    print('16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.')
    a =  float(input('Digite o Valor do ax²: '))
    #a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    if a != 0:
        b =  float(input('Digite o Valor do bx: '))
        c =  float(input('Digite o Valor do c: '))
        #b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
        delta = b**2-4*a*c
        if delta >= 0:
            #c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
            if delta == 0:
                print('\nO valor de delta igual a 0 a equação possui apenas uma raiz real'.format(delta))
                x = -c/b
                print('Resultado:    \n    X¹: 0\n    X²: {}'.format(x))
                
            else:
                print('\nO delta {} e positivo a equação possui duas raiz reais'.format(delta))
                x1 = (-b + (delta**(0.5)))/2*a
                x2 = (-b - (delta**(0.5)))/2*a
                print('Resultado:\n    x¹: {}\n    x²: {}'.format(x1,x2))
        else:
            print('O delta {} e Negativo, por isso não possui raizes reais.\nFinalizado!!!!!'.format(delta))
        
    else:
        print('\nNão é uma Equação do Segundo Grau.\nFinalizado!!!!!')
equacaoDoSegundoGrau()
    

 ''' 17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. '''
def anoBissexto():
    print('\n17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. ')
    ano = int(input('Digite o Ano com 4 digitos: '))
    
    caso1 = ano%4   == 0
    caso2 = ano%100 == 0
    caso3 = ano%400 == 0
    #Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.
    if caso1 == True:
        #Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.
        if caso2 == True:
            #Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.
            if caso3 == True:
                #O ano é bissexto (tem 366 dias).
                print('\n{} É Bissexto'.format(ano))
            else:
                #O ano não é um ano bissexto (tem 365 dias).
                print('\n{} NÃO é Bissexto'.format(ano))
        else:
            #O ano é bissexto (tem 366 dias).
            print('\n{} É Bissexto'.format(ano))
    else:
        #O ano não é um ano bissexto (tem 365 dias).
        print('\n{} NÃO é Bissexto'.format(ano))
anoBissexto()


  '''18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. '''
def dataValida():
    print('18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. ')
    data = input('Digite uma data no formato dd/mm/aaaa: ')
    diaInput = int(data.split('/')[0])
    mesInput = int(data.split('/')[1])
    anoInput = int(data.split('/')[2])
    #Criando Variaveis
    dia = False
    mes = False
    #Determinando ano bissexto
    anoBissexto = ((anoInput%4 == 0 and anoInput%100 == 0 and anoInput%400 == 0) or (anoInput%4 == 0 and anoInput%100 != 0)) == True
    mes31 = [1,3,5,7,8,10,12]
    if mesInput >=1 and mesInput <= 12:
        mes = True
        if (mesInput in mes31) and diaInput >=1 and diaInput <= 31:
            dia = True
        else:
            if mesInput == 2:
                if anoBissexto == True and diaInput >=1 and diaInput <= 29:
                    dia = True
                else:
                    if diaInput >=1 and diaInput <= 28:
                        dia = True
            else:
                if diaInput >= 1 and diaInput <= 30:
                    dia = True
        if mes == True and dia == True:
            print('A data {} É valida'.format(data))
        else:
            print('A data {} NÃO é valida'.format(data))
    else:
        print('O mes {} NÃO e Valido'.format(mesInput))

dataValida()


  '''19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.  
  Observando os termos no plural a colocação do "e", da vírgula entre outros.
 
  Exemplo:
  a. 326 = 3 centenas, 2 dezenas e 6 unidades
  a. 12  = 1 dezena e 2 unidades   Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 '''
def lerNumerosInteiros():
    print('19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo. Observando os termos no plural a colocação do "e", da vírgula entre outros.')
    numero = input('Digite um numero inteiro menor que 1000: ')
    if len(numero) == 3:
        print('{} = {} centenas, {} dezenas e {} unidades'.format(numero,numero[0],numero[1],numero[2]))
    elif len(numero) == 2:
        print('{} = {} dezenas e {} unidades'.format(numero,numero[0],numero[1]))
    elif len(numero) == 1:
        if numero in (0,1):
            print('{} = {} unidade'.format(numero,numero[0]))
        else:
            print('{} = {} unidades'.format(numero,numero[0]))
lerNumerosInteiros()
 

 ''' 20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
  a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
  a. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
  a. A mensagem "Aprovado com Distinção", se a média for igual a 10. '''
def mediaAluno(quantidadeNotas):
    print('20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno')
    nota = []
    for i in range(quantidadeNotas):
        nota.append(float(input('Digite a {}ª Nota: '.format(i+1))))
    media = sum(nota) / len(nota)
    if media == 10:
        mensagem = 'Aprovado com Distinção'
    if media >= 7 and media < 10:
        mensagem = 'Aprovado'
    elif media < 7:
        mensagem = 'Reprovado'
    print('\n Media: {}\n {}'.format(round(media,2),mensagem))
mediaAluno(5)
    

  '''21. Faça um Programa para um caixa eletrônico. 
  O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
  O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
   a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
   a. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. '''
def caixaEletronico():
    print(' Faça um Programa para um caixa eletrônico. ')
    saque = input('Notas Disponiveis de 1, 5, 10, 50 e 100 reais\nValor do Saque: R$ ')
    qtde = ['','Uma','Duas','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove',]
    mensagem = 'Para sacar a quantia de R$ ' + saque + ' reais, o programa fornece '
    if int(saque) >=10 and int(saque) <= 600:
        if len(saque) == 3:
            centena = int(saque[0])
            
            if centena > 1:
                mensagem = mensagem + qtde[centena]+ ' notas de 100 '
            else:
                mensagem = mensagem + qtde[centena]+' nota de 100 '
        if len(saque) >= 2:
            if len(saque) == 3:
                dezena  = int(saque[1])
                unidade = int(saque[2])
            if len(saque) == 2:
                dezena  = int(saque[0])
                unidade = int(saque[1])
                
            if dezena >= 5:
                divisao_dezena1 = dezena//5
                resto_dezena1 = dezena%5
                if divisao_dezena1 > 1:
                    mensagem = ','+mensagem +  qtde[divisao_dezena1] +' notas de 50 '
                else:
                    mensagem = ','+mensagem +  qtde[divisao_dezena1] +' nota de 50 '
                
                if resto_dezena1 > 0:
                    divisao_dezena2 = resto_dezena1//1
                    if divisao_dezena2 > 1:
                        mensagem = mensagem +  ' e '+qtde[divisao_dezena2]+' notas de 10 '
                    else:
                        mensagem = mensagem +  ' e '+qtde[divisao_dezena2]+' nota de 10 '
                        
            if dezena < 5 and dezena > 0:
                if dezena > 1:
                    mensagem = mensagem +  qtde[dezena] +' notas de 10 '
                else:
                    mensagem = mensagem +  qtde[dezena] +' nota de 10 '  
        
        if unidade >= 5:
            divisao_unidade1 = unidade//5
            resto_unidade1 = unidade%5
            if divisao_unidade1 > 1:
                mensagem = mensagem + ', '+qtde[divisao_unidade]+ ' notas de 5 '
            else:
                mensagem = mensagem + ', '+qtde[divisao_unidade1]+ ' nota de 5 '
                
            if resto_unidade1 > 0:
                divisao_unidade2 = resto_unidade1//1
                if divisao_unidade2 > 1:
                    mensagem = mensagem + ' e ' + qtde[divisao_unidade2] +' notas de 1'
                else:
                    mensagem = mensagem + ' e ' + qtde[divisao_unidade2] +' nota de 1'
                    
        if unidade < 5 and unidade > 0:
            if unidade > 1:
                mensagem = ','+mensagem +  qtde[unidade] +' notas de 1'
            else:
                mensagem = ','+mensagem +  qtde[unidade] +' nota de 1'
                        
        print(mensagem)
                    
    else:
        if int(saque) < 10:
            print('Valor Inferior ou Minimo de R$10.00')
        else:
            print('Valor Superior ou Maximo de R$600.00')
    
caixaEletronico()


 ''' 22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão). '''
def par_ou_impar():
    #print(' 22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão). ')
    num =  int(input('Digite um numero: '))
    num_rest =  num%2
    if num_rest == 0:
        mensagem = 'Par'
    else:
        mensagem = 'Impar'
        
    print('O numero {} é {}'.format(num,mensagem))
par_ou_impar()

 '''23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento. '''
def inteiro_ou_decial():
     #print('23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento. ')
     num = float(input('Digite um numero: '))
     
     if round(num) == num:
         mensagem = 'Inteiro'
     else:
         mensagem = 'Decimal'
     print('O numero {} e {}'.format(num,mensagem))
inteiro_ou_decial()

 '''24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
 O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
  a. par ou ímpar;
  a. positivo ou negativo;
  a. inteiro ou decimal. '''

def qual_operacao_matematica():
    print('24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.')
    num1 = float(input('Digite o Primeiro Numero: '))
    num2 = float(input('Digite o Segundo Numero: '))
    operacao = input('Qual operação que deseja realizar: ')
    
    if operacao in ('*','vezes','multiplicação','multiplicacao'):
        result = num1 * num2
        operacao_msg = 'A multiplicação'
    
    if operacao in ('/','dividir','divisão','divisao'):
        result = num1 / num2
        operacao_msg = 'A divisão'
        
    if operacao in ('+','somar','adicao','adição','soma'):
        result = num1 + num2
        operacao_msg = 'A Adição'
        
    if operacao in ('-','subtração','menos','subtracao','subtrair'):
        result = num1 - num2
        operacao_msg = 'A Subtração'
        
    if operacao in ('**','expoente','elevado'):
        result = num1 ** num2
        operacao_msg = 'O Expoente'
        
    if result > 0:
        positivo_negativo =  'Positivo'
    elif result < 0:
        positivo_negativo =  'Negativo'
    else:
        positivo_negativo =  'Nulo'
        
    if result%2 == 0:
        par_impar = 'Par'
    else:
        par_impar = 'Impar'
        
    if round(result) == result:
        inteiro_decimal = 'Inteiro'
    else:
        inteiro_decimal = 'Decimal'
        
    print('\n{} entre {} e {}\n    Resulta em {}\n    É um numero {}, {} e {}'.format(operacao_msg,num1,num2,result,par_impar,positivo_negativo,inteiro_decimal))

qual_operacao_matematica()


    
  '''25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

  a. "Telefonou para a vítima?"
  a. "Esteve no local do crime?"
  a. "Mora perto da vítima?"
  a. "Devia para a vítima?"
  a. "Já trabalhou com a vítima?"

  O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
  Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
  Caso contrário, ele será classificado como "Inocente". '''
  
def perguntas_sobre_crime():
    print('25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.')
    perguntas = [
              "Telefonou para a vítima?",
              "Esteve no local do crime?",
              "Mora perto da vítima?",
              "Devia para a vítima?",
              "Já trabalhou com a vítima?"
            ]
    respostas = []
    for i in range(len(perguntas)):
        respostas.append(input('{}: '.format(perguntas[i])))
        
    if respostas.count('sim') == 2:
        participacao = 'Suspeita'
    elif respostas.count('sim') >= 3 and respostas.count('sim') <= 4:
        participacao = 'Cúmplice'
    elif respostas.count('sim') == 5:
        participacao = 'Assassino'
    else:
        participacao = 'Inocente'
    
    print('Respostas:\n\n')
    for x, y in zip(perguntas,respostas):
        print(' {}: {}'.format(x, y))
        
    print('\nA participacão foi indicada como: {}'.format(participacao))
    
perguntas_sobre_crime()

 ''' 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
  a. Álcool: 
  a. até 20 litros, desconto de 3% por litro 
  a. acima de 20 litros, desconto de 5% por litro
  a. Gasolina: 
  a. até 20 litros, desconto de 4% por litro
  a. acima de 20 litros, desconto de 6% por litro

  Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
  calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.  '''
  
def posto_de_combustivel():
    print(' 26. Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível')
    qtde_litros = int(input('Qual quantidade de Litros vendidos: '))
    tipo_combustivel =  input('Qual o tipo de combustivel digite A-álcool, G-gasolina: ')
    
    if tipo_combustivel == 'A':
        preco = 1.90
        preco_total = preco * qtde_litros
        combustivel = 'Álcool'
        
        if qtde_litros <= 20:
            desconto =  (preco*0.03)
        if qtde_litros > 20:
            desconto =  (preco*0.05)
    
    if tipo_combustivel == 'G':
        preco = 2.50
        preco_total = preco * qtde_litros
        combustivel = 'Gazolina'
        
        if qtde_litros <= 20:
            desconto =  (preco*0.04)
        if qtde_litros > 20:
            desconto =  (preco*0.06)
            
    preco_com_desconto = preco - desconto
    valor_a_pagar = preco_com_desconto * qtde_litros
    
    print('\nAbastecimento: {}l\n Valor {}: R${}\n desconto: R${}\n Valor a pagar por litro: R${}\n Total a Pagar: R${}'.format(qtde_litros,combustivel,preco,desconto,preco_com_desconto,valor_a_pagar))
        
posto_de_combustivel()
  

 ''' 27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
  {{{
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
  }}}

  Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
  Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.  '''
def fruteira():
    morango = int(input('Quantos kg de Morangos Deseja comprar: '))
    maca = int(input('Quantos kg de Maças Deseja comprar: '))
    total_de_kg = morango + maca
    desconto = 0

    if total_de_kg <= 5:
        preco_morango = 2.50
        preco_maca = 1.80
    else:
        preco_morango = 2.20
        preco_maca = 1.50
        
    compra_de_morango = preco_morango * morango
    compra_de_maca = preco_maca * maca
    total_compra = compra_de_morango + compra_de_maca
    
    if total_de_kg > 8 or total_compra > 25:
        desconto = total_compra * 0.1
    
    total_a_pagar = total_compra - desconto
    
    
        
    print('\nQtde Morango: {} Valor: R$ {}\
           \nQtde Maça: {} Valor: R$ {}\
           \nTotal da Compra: R$ {}\
           \nDesconto: R$ {}\
           \nValor Total a Pagar {}'.format(morango,round(compra_de_morango,2),maca,round(compra_de_maca,2)
           ,round(total_compra,2),round(desconto,2),round(total_a_pagar,2)))
fruteira()



 '''28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

  {{{
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

  }}}

  Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
  porém não há limites para a quantidade de carne por cliente. 
  Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
  Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
  contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. '''

def promocao_de_carne():
    print('Qual carne deseja comprar: \n\
             F-ile Duplo\n\
             A-lcatra\n\
             P-icanha\n')
    carne = input('Digite a primera letra da carne: ')
    kilo = float(input('Quantos Kg de Carne deseja: '))
    forma_pagamento = int(input('Qual é a forma de pagamento\n\
                               1 - Cartão Tabajara\n\
                               2 - Cartão de Credito ou Debito\n\
                               3 - Dinheiro\n\
                               Tipo:   '))
    desconto = 0
    
    if kilo <= 5:
        file_duplo = 4.90
        alcatra = 5.90
        picanha = 6.9

    if kilo > 5:
        file_duplo = 5.80
        alcatra = 6.80
        picanha = 7.80
        
        
    if carne == 'F':
        total_compra = file_duplo * kilo
        tipo_carne = 'File Duplo'
    elif carne == 'A':
        total_compra = alcatra * kilo
        tipo_carne = 'Alcatra'
    elif carne == 'P':
        total_compra = picanha * kilo
        tipo_carne = 'Picanha'
        
    if forma_pagamento == 1:
        tipo_pagamento = 'Cartão Tabajara'
        desconto = total_compra * 0.05
    elif forma_pagamento == 2:
        tipo_pagamento = 'Cartão de Credito ou Debito'
    elif forma_pagamento == 3:
        tipo_pagamento = 'Dinheiro'
    
     
        
    total_a_pagar = total_compra - desconto
        
    print('\nCupom Fiscal\n\
    Tipo da carne: {}\n\
    Preço Total: R$ {}\n\
    Tipo de Pagamento: {}\n\
    Valor do Desconto: R$ {}\n\
    Valor a pagar: R$ {}'.format(tipo_carne,round(total_compra,2)
              ,tipo_pagamento,round(desconto,2),round(total_a_pagar,2)))
promocao_de_carne()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    