lista_palavras = []
lista_palavras_nao_repetem = []

for i in range(10):
    lista_palavras.append(input())

ocorrencia = 0

for i in lista_palavras:
    for j in lista_palavras:
        if (i == j):
            ocorrencia += 1
    if ocorrencia == 1:
        lista_palavras_nao_repetem.append(i)
    ocorrencia = 0

print('As palavras sao:')
for i in lista_palavras_nao_repetem:
    print(i)

soma_letras = 0

for i in lista_palavras_nao_repetem:
    for j in i:
        soma_letras += 1

print(f'A soma do tamanho das palavras é: {soma_letras}')

print('Estou impressionado, você me venceu, pode ir embora...')