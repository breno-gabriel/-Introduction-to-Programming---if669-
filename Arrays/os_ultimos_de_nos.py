num_mochilas = int(input())

nome = input().split()

tamanho_mochila = []

for i in range(num_mochilas):
    tamanho_mochila.append(int(input()))

mochila = ['Lanterna', 'Omega 3 da top therm']

lista_mochilas = []

for i in range(num_mochilas):
    lista_mochilas.append(mochila[:])

qunt_itens = int(input())

for i in range(qunt_itens):
    nome_item = input()
    mochila_item = int(input())
    lista_mochilas[mochila_item].append(nome_item)

for i in range(len(tamanho_mochila)):
    saida = False 
    while not saida:
        if len(lista_mochilas[i]) > tamanho_mochila[i]:
            del lista_mochilas[i][-1]
            print('Mochila cheia. Não vai dar para levar.')
        else:
            saida = True

chegada = False

while not chegada:
    acao = input()
    if acao == 'CHEGAMOS NO CIN!':
        chegada = True
    elif acao == 'Tirar da mochila':
        item_acao = input()
        mochila_item_acao = int(input())
        if item_acao in lista_mochilas[mochila_item_acao]:
            del lista_mochilas[mochila_item_acao][lista_mochilas[mochila_item_acao].index(item_acao)]
            print(f'{item_acao} usado com sucesso da mochila {mochila_item_acao}.')
        else:
            print(f'Você não tem {item_acao} na mochila {mochila_item_acao}.')
    elif acao == 'Guardar na mochila':
        item_acao = input()
        mochila_item_acao = int(input())
        if len(lista_mochilas[mochila_item_acao]) >= tamanho_mochila[mochila_item_acao]:
            print(f'“Mochila {mochila_item_acao} cheia!')
        else:
            lista_mochilas[mochila_item_acao].append(item_acao)
            print(f'{item_acao} adicionado na mochila {mochila_item_acao}.')
    else:
        print('Ação inválida.')

for i in range(num_mochilas):
    if lista_mochilas[i] == []:
        print(f'Mochila de {nome[i]} chegou assim:')
    else:
        print(f'Mochila de {nome[i]} chegou assim:')
        for j in range(len(lista_mochilas[i])):
            print(lista_mochilas[i][j])
    



    


