"""1. Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente."""

string1 = input('Digite a Primeira Frase: ')
string2 = input('Digite a Segunda Frase: ')
print('\n')
print('String 1: {}\nString 2: {}'.format(string1,string2))
print('Tamanho de "{}": {} caracteres'.format(string1,len(string1)))
print('Tamanho de "{}": {} caracteres'.format(string2,len(string2)))

tamanho = len(string1) == len(string2)
conteudo = string1 == string2

if tamanho == True:
    print('As duas strings são de tamanhos Iguais')
else:
    print('As duas strings são de tamanhos Diferentes')

if conteudo == True:
    print('As duas strings possuem conteúdo Iguais')
else:
    print('As duas strings possuem conteúdo diferente')
print('\n')

