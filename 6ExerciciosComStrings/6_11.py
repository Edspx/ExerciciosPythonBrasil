"""11. Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!
Digite uma letra: O
A palavra é: _ _ _ _ O
Digite uma letra: E
A palavra é: _ E _ _ O
Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!"""
import random
import os
arquivo = open('D:\\Eder\\OneDrive\\Scripts Biblioteca\\Python\\ExerciciosPythonBrasil\\6.ExerciciosComStrings\\6_11_jogo_da_forca.txt')
palavras = []
for i in arquivo:
    palavras.append(i.strip())

aleatorio = random.randint(1,10)

palavra_forca = palavras[aleatorio].lower()
resposta = []
for i in range(len(palavra_forca)):
    resposta.append('_')
tentativas = 1
while tentativas <= 6:
    l = input('\nDigite uma Letra: ')
    if l in str(palavra_forca):
        for c in range(len(palavra_forca)):
            if l == palavra_forca[c]:
                resposta[c] = l
        print('A palavra é: ', end=' ')
        for r in range(len(resposta)):
            print(resposta[r], end=' ')
        compara = ''
        for f in  resposta:
            compara = compara + f
        if compara == palavra_forca:
            print('\n\nParabens Você Finalizou a Forca\n\n')
            break
    else:
        print('Você errou pela {}ª vez. Tente de novo!'.format(tentativas))
        tentativas += 1
if tentativas == 7:
    print('\n\nVoce Perdeu\n\n')
