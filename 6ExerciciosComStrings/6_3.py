"""
3. Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
F
U
L
A
N
O
"""
while True:

    nome = input('\nDigite seu Nome: ')
    nome = list(nome)
    for i in nome:
        print(i.upper())
