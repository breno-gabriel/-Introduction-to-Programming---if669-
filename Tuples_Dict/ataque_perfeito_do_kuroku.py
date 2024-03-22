posicoes_companheiros = input()

num_alvo = int(input())

nova_posicao_companheiro = ''

for i in posicoes_companheiros:
    if i != '[' and i != ']':
        nova_posicao_companheiro += i 

nova_posicao_companheiro = nova_posicao_companheiro.split(',')

for i in range(len(nova_posicao_companheiro)):
    nova_posicao_companheiro[i] = int(nova_posicao_companheiro[i])

dicionario = {}

for i in range(len(nova_posicao_companheiro)):
    dicionario.update({i : nova_posicao_companheiro[i]})

soma = 0

lista_posicoes = []

for i in dicionario:
    for j in dicionario:
        if i != j:
            soma = dicionario[i] + dicionario[j]
            if soma == num_alvo and len(lista_posicoes) == 0:
                lista_posicoes.append(i)
                lista_posicoes.append(j)
                

print(lista_posicoes)