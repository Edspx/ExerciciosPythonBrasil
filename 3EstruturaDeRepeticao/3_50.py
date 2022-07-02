'''50. Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.'''
dividendo = 1
divisor = 2
dividendo_soma = []
divisor_soma = []

print('H = 1 +', end= ' ')
for i in range(8):
    print('{}/{}'.format(dividendo,divisor), end=' + ')
    dividendo_soma.append(dividendo)
    divisor_soma.append(divisor)
    divisor += 1

dividendo_soma = sum(dividendo_soma)
divisor_soma = sum(divisor_soma)
total = (1 + dividendo_soma)/divisor_soma

print('{}/{}'.format(dividendo,divisor), end=' => ')
print('{}/{} = {}'.format(dividendo_soma+1,divisor_soma,round(total,2)), end=' ')

