talisma = {'Carneiro': ('Adormecer', 'Imortalidade'), 'Cao': ('Imortalidade', 'Forca descomunal'), 'Cobra': ('Invisibilidade', 'Equilibrio espiritual'), 'Coelho':('Alta velocidade', 'Metamorfose animal'), 'Tigre': ('Equilibrio espiritual', 'Adormecer'), 'Dragao': ('Fogo', 'Cura'), 'Cavalo': ('Cura', 'Levitacao'), 'Macaco': ('Metamorfose animal', 'Raio laser'), 'Galo': ('Levitacao', 'Animar objeto'), 'Porco': ('Raio laser', 'Fogo'), 'Rato': ('Animar objeto', 'Alta velocidade'), 'Touro': ('Forca descomunal', 'Invisibilidade')}

qnt_talismas = int(input())

lista_talismas_jack = []

for i in range(qnt_talismas):
    entrada = input()
    lista_talismas_jack.append(entrada)

qnt_inimigos = int(input())

lista_talismas_inimigo = []

for i in range(qnt_inimigos):
    entrada = input()
    lista_talismas_inimigo.append(entrada)

inimigos_restantes = qnt_inimigos


for i in lista_talismas_inimigo:
    vitoria = False
    for j in lista_talismas_jack:
        if talisma[i][1] == talisma[j][0]:
            vitoria = True 
            inimigos_restantes -= 1 
            print(f'Boa! O talisma do {i} vai ser nosso!')
            lista_talismas_jack.append(i)
    if not vitoria:
        for k in talisma:
            if talisma[k][0] == talisma[i][1]:
                print(f'Nao vai dar, melhor ir atras do talisma do {k} antes.')
        
if inimigos_restantes == 0:
    print('Esse plano funciona, vamos agora!')
else:
    print('Que mau dia!! Melhor pensarmos num plano de fuga.')

