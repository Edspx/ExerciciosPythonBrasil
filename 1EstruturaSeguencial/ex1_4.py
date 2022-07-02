'''4.Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''

'''notas = []
#input de notas
for i in range(4):
    notas.append(float(input('Digite a Nota %d do Aluno: ' %i)))
        
#calculando media
media = sum(notas) / len(notas)
print('As notas registradas foram %.2f, %.2f, %.2f e %.2f e a Media e %.2f'%(notas[0],notas[1],notas[2],notas[3],media))'''


def  media(a, b, c, d):
    notas = [a, b, c, d]
    r = sum(notas) / len(notas)
    return r

