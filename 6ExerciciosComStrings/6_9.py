"""9. Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de
formatação."""
while True:
    cpf_digitado = input('\ndigite o CPF: ')
    cpf = ''
    for i in cpf_digitado:
        if i not in [' ','.','-']:
            cpf = cpf+i
    if len(cpf) == 11:
        cpfn9_invertido = str(cpf)[-3::-1]

        
        multiplicador = 2
        l = []
        for i in range(len(cpfn9_invertido)):
            l.append(multiplicador * int(cpfn9_invertido[i]))
            multiplicador += 1
        resto = sum(l)%11
        if resto < 2:
            primeiro_dig = 0
        else:
            primeiro_dig = 11 - resto

        cpfn10_invertido = str(primeiro_dig)+cpfn9_invertido

        multiplicador = 2
        l = []
        for i in range(len(cpfn10_invertido)):
            l.append(multiplicador * int(cpfn10_invertido[i]))
            multiplicador += 1
        resto = sum(l)%11
        if resto < 2:
            segundo_dig = 0
        else:
            segundo_dig = 11 - resto

        digito_verificador = cpf[9:11]
        digito_calculado = str(primeiro_dig)+str(segundo_dig)

        if digito_verificador == digito_calculado:
            print('CPF: {} e Valido'.format(cpf_digitado))
        else:
    
            print('CPF: {} não e Valido'.format(cpf_digitado))
        
    else:
        print('Numero de CPF fora do padrão de 11 digitos')

