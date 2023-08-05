nome = input()

qunt_filmes = int(input())

lista_filmes = []

for i in range(qunt_filmes):
    lista_filmes.append(input().split(' - '))

for i in range(qunt_filmes):
    lista_filmes[i][1] = float(lista_filmes[i][1])

for i in range(len(lista_filmes)):
    for j in range(len(lista_filmes) - 1):
        if lista_filmes[j][1] < lista_filmes[j + 1][1]:
            lista_filmes[j], lista_filmes[j + 1] = lista_filmes[j + 1], lista_filmes[j]


if nome == 'João':
    print('Os filmes sugeridos por João são:')
elif nome == 'Bonna':
    print('Os filmes sugeridos por Bonna são:')
for i in range(qunt_filmes):
    print(f'{lista_filmes[i][0]} - {lista_filmes[i][1]}')



