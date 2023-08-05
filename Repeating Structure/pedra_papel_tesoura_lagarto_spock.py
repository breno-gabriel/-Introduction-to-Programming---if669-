rodadas = int(input())
escolha_sheldon = 0
escolha_raj = 0
vitorias_sheldon = 0
vitorias_raj = 0
cont = 0

while cont < rodadas:
    escolha_sheldon = input()
    escolha_raj = input()
    if escolha_sheldon == 'lagarto' and escolha_raj == 'tesoura' or escolha_sheldon == 'tesoura' and escolha_raj == 'spock' or escolha_sheldon == 'spock' and escolha_raj == 'lagarto':
        vitorias_raj += 1
        cont += 1
    elif escolha_sheldon == 'tesoura' and escolha_raj == 'lagarto' or escolha_sheldon == 'spock' and escolha_raj == 'tesoura' or escolha_sheldon == 'lagarto' and escolha_raj == 'spock':
        vitorias_sheldon += 1
        cont += 1
    else:
        vitorias_sheldon += 0
        vitorias_raj += 0
        cont += 1
if vitorias_sheldon > vitorias_raj:
    print('BAZINGA! EU SOU O SENHOR DA SALA!')
elif vitorias_raj > vitorias_sheldon:
    print('ENGOLE ESSA, SHELDON!')
else:
    print('Oh não, precisamos de outra rodada.')


