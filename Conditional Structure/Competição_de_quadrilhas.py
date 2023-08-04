nome_equipe = input()
passo1 = input()
passo2 = input()
passo3 = input()
passo4 = input()
passo5 = input()
pontuação = 0
aux = True

if passo1 == 'Cumprimento':
    pontuação += 100
elif passo1 == 'Balancê':
    pontuação += 50
elif passo1 == 'Passeio':
    pontuação += 70
elif passo1 == 'Túnel':
    pontuação -= (pontuação * 0.1)
elif passo1 == 'Serrote':
    pontuação += 100
elif passo1 == 'Casamento':
    pontuação += 0
elif passo1 == 'Despedida':
    pontuação += 0
else:
    aux = False
    pontuação += 0

if passo2 == 'Cumprimento':
    pontuação += 10
elif passo2 == 'Balancê':
    pontuação += 50
elif passo2 == 'Passeio':
    pontuação += 70
elif passo2 == 'Túnel':
    pontuação -= (pontuação * 0.1)
elif passo2 == 'Serrote':
    pontuação += 100
elif passo2 == 'Casamento':
    pontuação += 0
elif passo2 == 'Despedida':
    pontuação += 0
else:
    aux = False
    pontuação += 0

if passo3 == 'Cumprimento':
    pontuação += 10
elif passo3 == 'Balancê':
    pontuação += 50
elif passo3 == 'Passeio':
    pontuação += 70
elif passo3 == 'Túnel':
    pontuação -= (pontuação * 0.1)
elif passo3 == 'Serrote':
    pontuação += 100
elif passo3 == 'Casamento':
    pontuação += 0
elif passo3 == 'Despedida':
    pontuação += 0
else:
    aux = False
    pontuação += 0

if passo4 == 'Cumprimento':
    pontuação += 10
elif passo4 == 'Balancê':
    pontuação += 50
elif passo4 == 'Passeio':
    pontuação += 70
elif passo4 == 'Túnel':
    pontuação -= (pontuação * 0.1)
elif passo4 == 'Serrote':
    pontuação += 100
elif passo4 == 'Casamento':
    pontuação += 0
elif passo4 == 'Despedida':
    pontuação += 0
else:
    aux = False
    pontuação += 0

if passo5 == 'Cumprimento':
    pontuação += 10
elif passo5 == 'Balancê':
    pontuação += 50
elif passo5 == 'Passeio':
    pontuação += 70
elif passo5 == 'Túnel':
    pontuação -= (pontuação * 0.1)
elif passo5 == 'Serrote':
    pontuação += 100
elif passo5 == 'Casamento':
    pontuação += 0
elif passo5 == 'Despedida':
    pontuação += 35
else:
    aux = False
    pontuação += 0

if passo1 =='Casamento' or passo2 == 'casamento' or passo3 == 'Casamento' or passo4 == 'Casamento' or passo5 == 'Casamento':
    pontuação *= 2

if aux == False:
    print(f'Poxa, {nome_equipe}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.')
else:
    print(f'Parabéns, {nome_equipe}! Bela apresentação. A pontuação foi de {pontuação:.1f}!')