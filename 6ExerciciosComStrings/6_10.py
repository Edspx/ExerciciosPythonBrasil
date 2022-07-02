"""10. Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela
por extenso."""
while True:
    numeros = ['Zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove']
    dezena = [None,None,'Vinte','Trinta','Quarenta','Cinquenta','Sessenta','Setenta','Oitenta','Noventa']
    digito = int(input('\nDigite um Numero de 0 a 99: '))

    if digito <= 19:
        print('O numero digitado é : {}'.format(numeros[digito]))
    if digito >= 20:
        dezena_s = str(digito)[0]
        unidade_s = str(digito)[1]
        if unidade_s == '0':
            print('O Numero digitado é: {}'.format(dezena[int(dezena_s)]))
        else:
            print('O Numero digitado é: {} e {}'.format(dezena[int(dezena_s)],numeros[int(unidade_s)]))
