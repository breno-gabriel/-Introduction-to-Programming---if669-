#Função para calcular a gorjeta do serviço de Pedras Quentes.
def pedras(a, c):
    gorjeta_gerada = int((a + c)/2)
    return gorjeta_gerada

#Função para calcular a gorjeta do serviço de Massagem nos Pes.
def pes(a):
    if a % 2 == 0:
        gorjeta_gerada = int((a % 7)*6)
    else:
        gorjeta_gerada = int((a % 7)**2)
    return gorjeta_gerada

#Função para calcular a gorjeta do serviço de Refeição.
def refeicao(a):
    if a % 10 == 0:
        receita_gerada = 5
        return receita_gerada
    else:
        receita_gerada = 0
        while a % 10 != 0:
            a += 1
            receita_gerada += 1
        return receita_gerada

#Função para calcular a gorjeta do serviço de Massagem Completa.
def completa(a):
    a = str(a)
    soma = 0
    for i in a:
        i = int(i)
        soma += i
    receita_gerada = soma
    return receita_gerada

#Recendo as entrada, usando as funções e Imprimindo as mensagens para cada serviço.
gorjeta = 10
tempo = 120
tempo_decorrido = 0
fim_expediente = False
while not fim_expediente:
    servico = input()
    if servico == 'pedras':
        nome_serviço = 'Pedras Quentes'
        gorjeta += pedras(gorjeta, tempo_decorrido)
        tempo -= 20
        tempo_decorrido += 20
        print(f'Voce concluiu o servico de {nome_serviço} e agora possui {gorjeta} gorjetas.')
    elif servico == 'pes':
        nome_serviço = 'Massagem nos Pes'
        gorjeta += pes(gorjeta)
        tempo -= 30
        tempo_decorrido += 30
        print(f'Voce concluiu o servico de {nome_serviço} e agora possui {gorjeta} gorjetas.')
    elif servico == 'refeicao':
        nome_serviço = 'Servir Refeicao'
        gorjeta += refeicao(gorjeta)
        tempo -= 15
        tempo_decorrido += 15
        print(f'Voce concluiu o servico de {nome_serviço} e agora possui {gorjeta} gorjetas.')
    elif servico == 'completa':
        nome_serviço = 'Massagem Completa'
        gorjeta += completa(gorjeta)
        tempo -= 50
        tempo_decorrido += 50
        print(f'Voce concluiu o servico de {nome_serviço} e agora possui {gorjeta} gorjetas.')
    else:
        tempo -= 5
        tempo_decorrido += 5
        print(f'O cliente fez voce perder tempo, voce ainda possui {gorjeta} gorjetas.')

    if tempo <= 0:
        fim_expediente = True

#Imprimindo resultado final.
if gorjeta >= 50:
    print(f'Você acumulou {gorjeta} gorjetas, com essa quantidade voce conseguira comprar sua passagem de saida e salvar seus pais.')
else:
    print('Voce nao conseguiu o minimo necessario para comprar a passagem de saida desse mundo e salvar seus pais.')
