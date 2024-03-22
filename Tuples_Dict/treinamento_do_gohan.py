qunt_pedras = int(input())

seq_picollo = input().split(' ')
seq_gohan = input().split(' ')

for i in range(qunt_pedras):
    seq_picollo[i] = int(seq_picollo[i])
    seq_gohan[i] = int(seq_gohan[i])

lancamento_picollo = {}
lancamento_gohan = {}

for i in seq_picollo:
    cont_repeticao = 0
    for j in seq_picollo:
        if i == j:
            cont_repeticao += 1
    lancamento_picollo.update({i: cont_repeticao})

for i in seq_gohan:
    cont_repeticao = 0
    for j in seq_gohan:
        if i == j:
            cont_repeticao += 1
    lancamento_gohan.update({i: cont_repeticao})

if lancamento_picollo == lancamento_gohan:
    print('Dale Gohan!')
else:
    print('Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.')


