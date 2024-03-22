artistas = input().split(' - ')
lista_musicas = []
lista_comentarios = []
possiveis_notas = [' 0', ' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' 10']
cont_dean = 0
cont_sam = 0
soma_notas = 0
lista_soma_notas = []
maior_nota = 0
a = 0
b = 0
voto_sam = False
voto_dean = False

for i in artistas:
    musica = input().split(' - ')
    lista_musicas.append(musica[:])
    for j in musica:
        voto_sam = False
        voto_dean = False
        while not voto_sam and not voto_dean:
            saida1 = False
            saida2 = False
            cont = 0
            while not saida1:
                    comentario1 = input().split(':')
                    for k in possiveis_notas:
                        if comentario1[1] == k:
                            if comentario1[0] == 'Dean':
                                a = int(comentario1[1])
                                saida1 = True
                                voto_dean = True
                            elif comentario1[0] == 'Sam':
                                saida1 = True
                                a = int(comentario1[1])
                                voto_sam = True
            while not saida2:
                    comentario2 = input().split(':')
                    for l in possiveis_notas:
                        if l in comentario2[1] == l:
                            if comentario2[0] == 'Dean' and voto_sam:
                                b = int(comentario2[1])
                                saida2 = True
                                voto_dean = True
                            elif comentario2[0] == 'Sam' and voto_dean:
                                b = int(comentario2[1])
                                saida2 = True
                                voto_sam = True
                            elif comentario2[0] == 'Dean' and not voto_sam:
                                a = int(comentario2[1])
                                saida = True
                                voto_dean = True
                            elif comentario2[0] == 'Sam' and not voto_dean:
                                a = int(comentario2[1])
                                saida = True
                                voto_sam = True

        soma = a + b
        lista_soma_notas.append(soma)
        if soma > maior_nota:
          maior_nota = soma

comentario_final = input().split(': ')
segundo_comentario_final = comentario_final[1].split(' - ')

index1 = artistas.index(segundo_comentario_final[0])


index2 = lista_musicas[index1].index(segundo_comentario_final[1])



if lista_soma_notas[index2] == maior_nota and segundo_comentario_final[0] == artistas[index1]:
    print(f'Caraca {comentario_final[0]} mandou bem! Essa música é a mais braba, com a nota {maior_nota}')
else:
    diferenca = maior_nota - lista_soma_notas[index2] 
    print(f'Podia ter escolhido outra música, {comentario_final[0]}. Essa é boa, mas perde em {diferenca} pontos pra a música com a melhor nota')
