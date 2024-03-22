def maior_venda(tabela_vendas):
    mais_vendido = 0
    nome_lanche = ''
    for lanche in tabela_vendas:
        if tabela_vendas[lanche] > mais_vendido:
            mais_vendido = tabela_vendas[lanche]
            nome_lanche = lanche
    return nome_lanche

tabela = {'trigo': 3, 'fermento': 2, 'manteiga': 6, 'ovos': 2, 'batata': 4, 'arroz': 3, 'siri': 8, 'pao': 2, 'tomate': 2, 'alface': 1, 'picles': 3, 'queijo': 5, 'hamburguer de siri': 24, 'pizza de siri': 42, 'siri frito': 15, 'siri a parmegiana': 24}

qunt_ingredientes = {'trigo': 5, 'fermento': 5, 'manteiga': 5, 'ovos': 5, 'batata': 5, 'arroz': 5, 'siri': 5, 'pao': 5, 'tomate': 5, 'alface': 5, 'picles': 5, 'queijo': 5}

receitas = {'hamburguer de siri': ('siri', 'pao', 'alface', 'tomate', 'queijo', 'picles'), 'pizza de siri': ('siri', 'trigo', 'fermento', 'ovos', 'queijo'), 'siri frito': ('siri', 'manteiga'), 'siri a parmegiana': ('siri', 'trigo', 'ovos', 'queijo', 'tomate')}

vendas = {'hamburguer de siri': 0, 'pizza de siri': 0, 'siri frito': 0, 'siri a parmegiana': 0}

pedidos_nao_incluidos = {}

caixa = 40

fim = False 

vendas_hamb_siri = 0 

while not fim:
    try:
        pedido = input() 
        if pedido in receitas:
            print(f'{pedido} saindo...')
            vendas.update({pedido: vendas[pedido] + 1})
            caixa += tabela[pedido]
            for ingrediente in receitas[pedido]:
                if qunt_ingredientes[ingrediente] <= 0:
                    qunt_ingredientes.update({ingrediente: qunt_ingredientes[ingrediente] + 4})
                    caixa -= 4 * tabela[ingrediente]
                    qunt_ingredientes.update({ingrediente: qunt_ingredientes[ingrediente] - 1})
                else:
                    qunt_ingredientes.update({ingrediente: qunt_ingredientes[ingrediente] - 1})
        else:
            if pedido in pedidos_nao_incluidos:
                if pedidos_nao_incluidos[pedido] == 1:
                    print(f'Atendendo demandas, {pedido} é a mais nova adição ao cardápio do Siri Cascudo.')
                    ingredientes = input().split(' ')
                    ingredientes = tuple(ingredientes)
                    receitas.update({pedido: ingredientes})
                    preco = 0 
                    for ingrediente in ingredientes:
                        preco += tabela[ingrediente]
                    preco += 5 
                    tabela.update({pedido: preco})
                    vendas.update({pedido: 0})
                else:
                    print(f'{pedido} ainda não é uma opção disponível.')
                    pedidos_nao_incluidos.update({pedido: pedidos_nao_incluidos[pedido] + 1})
            else:
                print(f'{pedido} ainda não é uma opção disponível.')
                pedidos_nao_incluidos.update({pedido: 0})

    
    
    except EOFError:
        print('##### Fim do expediente #####')
        fim = True 

print(f'O lucro obtido no dia de hoje foi de R${caixa - 40}.')
if maior_venda(vendas) == 'hamburguer de siri':
  print('O bom e tradicional hambúrguer de siri, líder em vendas, nunca será superado!')
else:
  print(f'{maior_venda(vendas).capitalize()} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário hambúrguer de siri.')
