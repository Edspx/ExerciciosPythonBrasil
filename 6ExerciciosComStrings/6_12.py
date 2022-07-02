"""12. Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso
deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço
separador.
Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
"""
telefone_digitado = input('Digite o numero de Telefone: ')
telefone_sem_formatacao = telefone_digitado.replace('-','')
if len(telefone_sem_formatacao) == 7:
    telefone_sem_formatacao = '3'+telefone_sem_formatacao
    

telefone_com_formatacao = telefone_sem_formatacao[0:4]+'-'+telefone_sem_formatacao[4:8]
print('Telefone: ',telefone_com_formatacao)
if len(telefone_digitado.replace('-','')) == 7: print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
print('Telefone corrigido sem formatação: ',telefone_sem_formatacao)
print('Telefone corrigido com formatação: ',telefone_com_formatacao)