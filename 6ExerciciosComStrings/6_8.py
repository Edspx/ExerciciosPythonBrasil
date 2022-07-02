"""8. Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou
vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são
ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um
programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
09/10/2020 ExerciciosComStrings - PythonBrasil
https://wiki.python.org.br/ExerciciosComStrings 2/2"""

frase = input('\nDigite uma Frase ou palavra: ')
frase_sem_espaco = ''
frase_invertida = str(frase)[::-1]
for l in frase:
    if l != ' ':
        frase_sem_espaco = frase_sem_espaco+l
fase_sem_espaco_invertida = str(frase_sem_espaco)[::-1]
print(frase_sem_espaco,fase_sem_espaco_invertida)
if frase_sem_espaco == fase_sem_espaco_invertida:
    print('A "{}" e seu inverso "{}" são Palindromos'.format(frase,frase_invertida))
else:
    print('A "{}" e seu inverso "{}" não são Palindromos'.format(frase,frase_invertida))