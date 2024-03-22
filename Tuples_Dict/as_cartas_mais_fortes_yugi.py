#Criando um dicionário para usar na questão.
deck = {}

#Recebendo a quantidade de cartas.
qnt_cartas = int(input())

#Recebendo as cartas e colocando nos dicionários.
for i in range(qnt_cartas):
    carta = input().split(' ')

    #Armazenando o nome das cartas em um variável.

    lista_palavras_nome_carta = carta[:-2]

    nome_carta = ' '.join(lista_palavras_nome_carta)

    #Armazenando os valores de ataque e defesa em uma tupla.

    valores = carta[-2:]

    for num in range(2):
        valores[num] = int(valores[num])

    tupla_status = tuple(valores)

    #Armazenando o nome da carta e o seus status em um dicionario.

    deck.update({nome_carta: tupla_status})

#Verificando qual carta tem maior ataque.

maior_ataque = 0
nome_carta_maior_ataque = ''

for ataque in deck:
    if deck[ataque][0] > maior_ataque:
        maior_ataque = deck[ataque][0]
        nome_carta_maior_ataque = ataque

#Verificando qual carta tem a maior defesa.

maior_defesa = 0 
nome_carta_maior_defesa = ''

for defesa in deck:
    if deck[defesa][1] > maior_defesa:
        maior_defesa = deck[defesa][1]
        nome_carta_maior_defesa = defesa

#Imprimindo resultados.

print(f'Carta com maior poder de ataque: {nome_carta_maior_ataque}')
print(f'Ataque: {maior_ataque}')
print('')
print(f'Carta com maior poder de defesa: {nome_carta_maior_defesa}')
print(f'Defesa: {maior_defesa}')


    

    
