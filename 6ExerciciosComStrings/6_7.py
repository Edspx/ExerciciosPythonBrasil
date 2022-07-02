"""7. Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
a. quantos espaços em branco existem na frase.
b. quantas vezes aparecem as vogais a, e, i, o, u."""

frase = input('Digite uma Frase: ')
d = dict()
vogal = ['a','e','i','o','u']

for letra in frase.lower():
    if letra in d:
        d[letra] += 1
    else:
        d[letra] = 1

espaco_em_branco = d[' ']
vogais = d['a'] + d['e'] + d['i'] + d['o'] + d['u']

print('\nNa frase: "{}"\n Existe {} espacos em branco\n Existe {} vogais sendo:'.format(frase,espaco_em_branco,vogais))

for l in d:
    if l in vogal:
        print(' ',l, d[l])