# Criando uma matriz 6x6.
linha = []
matriz = []

for i in range(6):
    linha.append('-')

for i in range(6):
    matriz.append(linha[:])

# Colocando os valores na matriz.
voceY = int(input())
voceX = int(input())
zumbiY = int(input())
zumbiX = int(input())
crachaY = int(input())
crachaX = int(input())
portaY = int(input())
portaX = int(input())

matriz[voceY][voceX] = 'V'
matriz[zumbiY][zumbiX] = 'Z'
matriz[crachaY][crachaX] = 'C'
matriz[portaY][portaX] = 'P'

# Trabalhando com os rounds.
fim_partida = False
achou_cracha = False
achou_saida = False
encurralado_zumbi = False
cont = 0

while not fim_partida:
    # Movimentaçao do zumbi.
    if voceX == zumbiX:
        if voceY < zumbiY:
            matriz[zumbiY][zumbiX] = '-'
            matriz[zumbiY - 1][zumbiX] = 'Z'
            zumbiX = zumbiX
            zumbiY = zumbiY - 1
        elif voceY > zumbiY:
            matriz[zumbiY][zumbiX] = '-'
            matriz[zumbiY + 1][zumbiX] = 'Z'
            zumbiX = zumbiX
            zumbiY = zumbiY + 1
    elif voceX < zumbiX:
        matriz[zumbiY][zumbiX] = '-'
        matriz[zumbiY][zumbiX - 1] = 'Z'
        zumbiX = zumbiX - 1
        zumbiY = zumbiY
    elif voceX > zumbiX:
        matriz[zumbiY][zumbiX] = '-'
        matriz[zumbiY][zumbiX + 1] = 'Z'
        zumbiX = zumbiX + 1
        zumbiY = zumbiY

    # Analisando se o zumbi encurralou o jogador ou não.
    if voceX == zumbiX and voceY == zumbiY:
        encurralado_zumbi = True
        fim_partida = True

    # Movimentação do jogador em busca do crachá.
    if not achou_cracha and not fim_partida:
        if crachaX == voceX:
            if crachaY < voceY:
                matriz[voceY][voceX] = '-'
                matriz[voceY - 1][voceX] = 'V'
                voceX = voceX
                voceY = voceY - 1
            elif crachaY > voceY:
                matriz[voceY][voceX] = '-'
                matriz[voceY + 1][voceX] = 'V'
                voceX = voceX
                voceY = voceY + 1
        elif voceX < crachaX:
            matriz[voceY][voceX] = '-'
            matriz[voceY][voceX + 1] = 'V'
            voceX = voceX + 1
            voceY = voceY
        elif voceX > crachaX:
            matriz[voceY][voceX] = '-'
            matriz[voceY][voceX - 1] = 'V'
            voceX = voceX - 1
            voceY = voceY

    # Verificação de posse ou não do cracha.
    if voceX == crachaX and voceY == crachaY:
        achou_cracha = True
        cont += 1

    # Movimentação do personagem em busca da porta.
    if achou_cracha and not achou_saida and cont > 2 and not encurralado_zumbi:
        if portaX == voceX:
            if portaY < voceY:
                matriz[voceY][voceX] = '-'
                matriz[voceY - 1][voceX] = 'V'
                voceX = voceX
                voceY = voceY - 1
            elif portaY > voceY:
                matriz[voceY][voceX] = '-'
                matriz[voceY + 1][voceX] = 'V'
                voceX = voceX
                voceY = voceY + 1
        elif voceX < portaX:
            matriz[voceY][voceX] = '-'
            matriz[voceY][voceX + 1] = 'V'
            voceX = voceX + 1
            voceY = voceY
        elif voceX > portaX:
            matriz[voceY][voceX] = '-'
            matriz[voceY][voceX - 1] = 'V'
            voceX = voceX - 1
            voceY = voceY

        if voceX == portaX and voceY == portaY:
            achou_saida = True
            fim_partida = True

    # Calculando a distância entre o jogador e o zumbi.
    distancia = ((voceX - zumbiX) ** 2 + (voceY - zumbiY) ** 2) ** 0.5

    # Imprimindo a matriz.
    for i in matriz:
        print(*i)

    # Imprimindo informações a respeito do crachá.
    if not fim_partida:
        if not achou_cracha:
            print('Ainda não achei o crachá')
        elif achou_cracha and cont == 1:
            print('Finalmente! Peguei o crachá')
        elif achou_cracha and cont >= 2:
            print('Já peguei o crachá')

    # Imprimindo informações a respeito da proximidade do zumbi.
    if not fim_partida:
        if int(distancia) <= 3:
            print('Preciso acelerar, o zumbi tá na minha cola!')
        elif 3 < int(distancia) <= 4:
            print('Consigo ver la longe o zumbi, mas é melhor acelerar!')
        else:
            print('O zumbi está longe, mas não posso ficar parado')

    # Pulando uma linha.
    if not fim_partida:
        print()

if fim_partida and achou_saida:
    print('Consegui achar a porta, agora é so passar na catraca e vazar daqui!')
elif fim_partida and encurralado_zumbi:
    print('Ferrou, agora vou virar um zumbi')
