'''51. Faça um programa que mostre os n termos da Série a seguir:
 S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.'''
dividendo = 1
divisor = 1
dividendo_soma = []
divisor_soma = []

print('S = ', end= ' ')
for i in range(10):
    print('{}/{}'.format(dividendo,divisor), end=' + ')
    dividendo_soma.append(dividendo)
    divisor_soma.append(divisor)
    dividendo += 1
    divisor += 2

dividendo_soma = sum(dividendo_soma)
divisor_soma = sum(divisor_soma)
total = (1 + dividendo_soma)/divisor_soma

print('{}/{}'.format(dividendo,divisor), end=' => ')
print('{}/{} = {}'.format(dividendo_soma,divisor_soma,round(total,2)), end=' ')

