"""6. Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com
o nome do mês por extenso.
Data de Nascimento: 29/10/1973
Você nasceu em 29 de Outubro de 1973."""

while True:
    nascimento = input('\nDigite a dia, mes e ano 00/00/000 do seu Nascimento: ')

    mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

    nasc = nascimento.split('/')

    dia = nasc[0]
    mes = mes[int(nasc[1]) - 1]
    ano = nasc[2]

    print('Você nasceu em {} de {} de {}.'.format(dia,mes,ano))
