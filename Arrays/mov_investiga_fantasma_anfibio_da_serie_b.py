lista_resultado_jogos = input().split(' ')

lista_interferencias = input().split(' ')

for i in range(12):
    if lista_resultado_jogos[i] == 'V' and lista_interferencias[i] == '1':
        print('O maldito sapo interferiu no resultado! O que parecia uma vitória garantida terminou em um empate.')
    elif lista_resultado_jogos[i] == 'E' and lista_interferencias[i] == '1':
        print('O anfíbio da maldição interferiu no resultado! Um empate tranquilo virou uma frustrante derrota.')
    elif lista_resultado_jogos[i] == 'D' and lista_interferencias[i] == '1':
        print('O que já era ruim, se tornou uma humilhante derrota. Desgraçado desse sapo!')

lista_fatias = [lista_resultado_jogos[0: 4], lista_resultado_jogos[4: 8], lista_resultado_jogos[8: 12]]
soma_pontos_primeira_parte = 0
primeira_parte_lista_resultado = lista_resultado_jogos[0: 4]
primeira_parte_lista_interferencias = lista_interferencias[0: 4]
for i in range(4):
    if primeira_parte_lista_resultado[i] == 'V' and primeira_parte_lista_interferencias[i] == '1':
        soma_pontos_primeira_parte += 1
    elif primeira_parte_lista_resultado[i] == 'E' and primeira_parte_lista_interferencias[i] == '1':
        soma_pontos_primeira_parte += 0
    elif primeira_parte_lista_resultado[i] == 'V' and primeira_parte_lista_interferencias[i] == '0':
        soma_pontos_primeira_parte += 3
    elif primeira_parte_lista_resultado[i] == 'E' and primeira_parte_lista_interferencias[i] == '0':
        soma_pontos_primeira_parte += 1
        
numero_rodada = 1

if soma_pontos_primeira_parte == 7:
    print(f'A pontuação na {numero_rodada}ª fatia de 4 jogos está dentro do planejado.')
elif soma_pontos_primeira_parte > 7:
    print(f'A pontuação na {numero_rodada}ª fatia de 4 jogos está com uma gordurinha de {soma_pontos_primeira_parte - 7} pontos.')
elif soma_pontos_primeira_parte < 7:
    print(f'A pontuação na {numero_rodada}ª fatia de 4 jogos está abaixo da planejada em {7 - soma_pontos_primeira_parte} pontos.')

soma_pontos_segunda_parte = 0
segunda_parte_lista_resultado = lista_resultado_jogos[4: 8]
segunda_parte_lista_interferencias = lista_interferencias[4: 8]
for i in range(4):
    if segunda_parte_lista_resultado[i] == 'V' and segunda_parte_lista_interferencias[i] == '1':
        soma_pontos_segunda_parte += 1
    elif segunda_parte_lista_resultado[i] == 'E' and segunda_parte_lista_interferencias[i] == '1':
        soma_pontos_segunda_parte += 0
    elif segunda_parte_lista_resultado[i] == 'V' and segunda_parte_lista_interferencias[i] == '0':
        soma_pontos_segunda_parte += 3
    elif segunda_parte_lista_resultado[i] == 'E' and segunda_parte_lista_interferencias[i] == '0':
        soma_pontos_segunda_parte += 1

numero_rodada = 2

if soma_pontos_segunda_parte == 7:
    print(f'A pontuação na {numero_rodada}ª fatia de 4 jogos está dentro do planejado.')
elif soma_pontos_segunda_parte > 7:
    print(f'A pontuação na {numero_rodada}ª fatia de 4 jogos está com uma gordurinha de {soma_pontos_segunda_parte - 7} pontos.')
elif soma_pontos_segunda_parte < 7:
    print(f'A pontuação na {numero_rodada}ª fatia de 4 jogos está abaixo da planejada em {7 - soma_pontos_segunda_parte} pontos.')

soma_pontos_terceira_parte = 0
terceira_parte_lista_resultado = lista_resultado_jogos[8: 12]
terceira_parte_lista_interferencias = lista_interferencias[8: 12]
for i in range(4):
    if terceira_parte_lista_resultado[i] == 'V' and terceira_parte_lista_interferencias[i] == '1':
        soma_pontos_terceira_parte += 1
    elif terceira_parte_lista_resultado[i] == 'E' and terceira_parte_lista_interferencias[i] == '1':
        soma_pontos_terceira_parte += 0
    elif terceira_parte_lista_resultado[i] == 'V' and terceira_parte_lista_interferencias[i] == '0':
        soma_pontos_terceira_parte += 3
    elif terceira_parte_lista_resultado[i] == 'E' and terceira_parte_lista_interferencias[i] == '0':
        soma_pontos_terceira_parte += 1
        
numero_rodada = 3

if soma_pontos_terceira_parte == 7:
    print(f'A pontuação na {numero_rodada}ª fatia de 4 jogos está dentro do planejado.')
elif soma_pontos_terceira_parte > 7:
    print(f'A pontuação na {numero_rodada}ª fatia de 4 jogos está com uma gordurinha de {soma_pontos_terceira_parte - 7} pontos.')
elif soma_pontos_terceira_parte < 7:
    print(f'A pontuação na {numero_rodada}ª fatia de 4 jogos está abaixo da planejada em {7 - soma_pontos_terceira_parte} pontos.')

soma_total_pontos  = soma_pontos_primeira_parte + soma_pontos_segunda_parte + soma_pontos_terceira_parte

soma_pontos_esperados_totais = 0

for i in range(12):
    if lista_resultado_jogos[i] == 'V':
        soma_pontos_esperados_totais += 3
    elif lista_resultado_jogos[i] == 'E':
        soma_pontos_esperados_totais += 1

pontos_perdidos = soma_pontos_esperados_totais - soma_total_pontos

if pontos_perdidos > 0:
    print(f'A maldição do sapo fez o Vascão perder {pontos_perdidos} pontos. Um número preocupante, que pode fazer diferença.')
else:
    print('A maldição parece que não teve impacto relevante! Não houve nenhuma perda de pontos.')

n_vitorias = 0
n_empates = 0
n_derrotas = 0

for i in range(12):
    if lista_resultado_jogos[i] == 'V' and lista_interferencias[i] == '1':
        n_empates += 1
    elif lista_resultado_jogos[i] == 'E' and lista_interferencias[i] == '1':
        n_derrotas += 1
    elif lista_resultado_jogos[i] == 'D' and lista_interferencias[i] == '1':
        n_derrotas += 1
    elif lista_resultado_jogos[i] == 'V' and lista_interferencias[i] == '0':
        n_vitorias += 1
    elif lista_resultado_jogos[i] == 'E' and lista_interferencias[i] == '0':
        n_empates += 1
    elif lista_resultado_jogos[i] == 'D' and lista_interferencias[i] == '0':
        n_derrotas += 1

if soma_total_pontos >= 21:
    print(f'Na reta final do campeonato, o Vasco garantiu um total de {soma_total_pontos} pontos, com {n_vitorias} vitórias, {n_empates} empates e {n_derrotas} derrotas, e alcançou o tão esperado acesso. O Clube do Fomento Corporal vibra num SJ lotado!')
else:
    print(f'Na reta final do campeonato, o Vasco fez somente {soma_total_pontos} pontos, com {n_vitorias} vitórias, {n_empates} empates e {n_derrotas} derrotas, e não conseguiu o acesso. Mais um ano de série B e sofrimento. Mob, o clube e a torcida estão completamente desolados.')
