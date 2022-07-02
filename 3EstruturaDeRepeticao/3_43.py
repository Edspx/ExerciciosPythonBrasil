'''
43. O cardápio de uma lanchonete é o seguinte:
Especificação Código Preço
Cachorro Quente 100 R$ 1,20
Bauru Simples 101 R$ 1,30
Bauru com ovo 102 R$ 1,50
Hambúrguer 103 R$ 1,20
Cheeseburguer 104 R$ 1,30
Refrigerante 105 R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser
pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido
deve ser encerrado.
'''
def cardapio():
    cod = [100, 101, 102, 103, 104, 105]
    preco = [1.20, 1.30, 1.50, 1.20, 1.30, 1.00]
    especif = ['Cachorro Quente', 'Bauru Simples', 'Bauru', 'Hamburguer', 'Cheeseburguer', 'Refrigerante']
    pedido_cod = []
    qtde = []

    print('Especificação Código Preço\n Cachorro Quente 100 R$ 1,20\n Bauru Simples 101 R$ 1,30\n Bauru com ovo 102 R$ 1,50\n Hambúrguer 103 R$ 1,20\n Cheeseburguer 104 R$ 1,30\n Refrigerante 105 R$ 1,00')
    pedido = 1
    while pedido > 0:
        if pedido > 0:
            print('\nDigite Codigo 0 para Finalizar o Pedido')
            pedido = int(input('Digite o Codigo: '))
            if pedido > 0:
                pedido_cod.append(pedido)
                qtde.append(int(input('Digite a Quantidade: ')))
        else:
            break

    total_pedido = []
    print('\n')
    for i in range(len(pedido_cod)):
        index = cod.index(pedido_cod[i])
        preco_total_item = preco[index]*qtde[i]
        print('{}º Item - {}: R${} X {} Qtde = R$ {}'.format(i+1,especif[index],preco[index],qtde[i],preco_total_item))
        total_pedido.append(preco_total_item)

    total = sum(total_pedido)
    print('Valor Total do Pedido: R$  ',total)
    print('\n')
cardapio()



    


