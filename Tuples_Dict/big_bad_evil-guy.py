#Criando os dicionarios que serão usados.
from parser import tuple2st


herois = {'Bobby': ('grande espada', 'armadura media'), 'Diana': ('dardo','armadura leve') , 'Eric': ('grande espada','armadura pesada'), 'Hank': ('espada', 'armadura media'), 'Presto' : ('cajado', 'armadura leve'), 'Sheila': ('espada', 'armadura leve'), 'Uni' : ('chifre', 'armadura leve')}
dano_armas = {'grande espada': 8, 'chifre': 2, 'cajado': 4, 'espada': 6, 'dardo': 12}
armadura = {'armadura pesada': 0, 'armadura media': 1, 'armadura leve': 3}

#Recebendo o nome do adversário.
nome_adversario = input()

#Definindo a quantidade de pontos de vida do inimigo.
if nome_adversario == 'Vingador':
    vida_adversario = 30
elif nome_adversario == 'Tiamat':
    vida_adversario = 20
elif nome_adversario == 'Vingador das sombras':
    vida_adversario = 14
else:
    vida_adversario = 9 

#Recebendo a quantidade de turnos até a derrota do grupo.
turnos = int(input())

#Variável booleana para determinar quando o jogo terminar.
fim_jogo = False

#Parte do código relacionada ao combate.
while not fim_jogo:
    atacante = input()

    turnos -= 1 

    if atacante == 'Mestre dos Magos':
        print('Muito obrigado amigo, que nos vejamos novamente um dia')
        fim_jogo = True 
    else:
        vida_adversario -= dano_armas[herois[atacante][0]]
        turnos -= armadura[herois[atacante][1]]
        nome_atacante = atacante

    if  turnos <= 0 and vida_adversario > 0 :
        print(f'Oh nao, {nome_adversario} e muito forte, este e o fim!')
        fim_jogo = True 
    elif vida_adversario <= 0:
        print(f'{nome_atacante} executou o ultimo golpe em {nome_adversario}, estamos livres!')
        fim_jogo = True 

