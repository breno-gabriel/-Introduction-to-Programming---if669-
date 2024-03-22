pokedex = {}

parada = True 

while parada:
    try:
      nome_pokemon = input().split(' ')
    except EOFError:
      parada = False 
      break
    if nome_pokemon[0] == 'ADD':
        verificacao = pokedex.get(nome_pokemon[1])
        if verificacao == None:
            desc_pokemon = input()
            pokedex.update({nome_pokemon[1]: desc_pokemon})
            print('Pokémon adicionado com sucesso')
        else:
            print('Pokémon já adicionado na Pokédex')
    elif nome_pokemon[0] == 'DESC':
        verificacao = pokedex.get(nome_pokemon[1])
        if verificacao == None:
            print('Ainda não há registro desse Pokémon')
        else:
            print(pokedex[nome_pokemon[1]])