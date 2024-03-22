#Criando função recursiva para analisar os dados.
def contador_niveis(niveis, cont_baixo, cont_medio, cont_alto):
    if len(niveis) == 0:
        return cont_baixo, cont_medio, cont_alto
    else:
        if niveis[-1] <= 4:
            cont_baixo += 1
        elif  4 < niveis[-1] <= 6:
            cont_medio += 1 
        elif niveis[-1] > 6:
            cont_alto += 1 
        return contador_niveis(niveis[:-1], cont_baixo, cont_medio, cont_alto)
   

#Recebendo as entradas.
num_eventos = int(input())
lista_nivel = input().split(',')
lista_data = input().split(',')
lista_acontecimento = input().split(', ')
data_atual = input()

#Removendo o ponto das datas.
for i in range(num_eventos):
    lista_data[i] = lista_data[i].split('.')

data_atual = data_atual.split('.')

#Convertendo as entradas de string para inteiro.
for i in range(num_eventos):
    lista_nivel[i] = int(lista_nivel[i])
    for j in range(len(lista_data[i])):
        lista_data[i][j] = int(lista_data[i][j])

for i in range(2):
    data_atual[i] = int(data_atual[i])

lista_meses = []
lista_anos = []

#Calculando o gap.
for i in range(num_eventos):
    res1 = (lista_data[i][0] + 12*lista_data[i][1])
    res2 = (data_atual[0] + 12*data_atual[1])
    res3 = res2 - res1
    res4 = res3 // 12
    res5 = res3 % 12
    lista_anos.append(res4)
    lista_meses.append(res5)

#estabelecendo os contadores de niveis de relevância. 
contador_baixo = 0 
contador_medio = 0 
contador_alto = 0
contador_baixo = contador_niveis(lista_nivel, contador_baixo, contador_medio, contador_alto)[0]
contador_medio = contador_niveis(lista_nivel, contador_baixo, contador_medio, contador_alto)[1]
contador_alto = contador_niveis(lista_nivel, contador_baixo, contador_medio, contador_alto)[2]

#Substituindo os niveis de relevância de acordo com as datas. 
for i in range(num_eventos):
    if lista_meses[i] + 12*lista_anos[i] >= 54:
        contador_alto += 1 

#Calculo da insegurança.
if contador_medio + contador_baixo == 0:
  inseguranca = 0 
else:
  inseguranca = int((contador_medio/(contador_medio + contador_baixo)) * 100)

#Imprimindo os resultados 
if contador_alto > 0:
    print('Realizar essa operação é um grande erro. A humanidade pode entrar em colapso.')
    print(f'Há {contador_alto} acontecimento(s) relevante(s). Se as consequências das suas ações anularem algum desses eventos, teremos sérios problemas.')
else:
    if inseguranca > 20:
        print("Os cálculos mostram que é possível acessar essa linha do tempo sem que haja muitos danos.")
        print(f'Mas é necessário termos cuidado, a taxa de insegurança é de {inseguranca}%')
    elif inseguranca <= 20:
        print('Os cálculos mostram que é possível acessar essa linha do tempo sem que haja muitos danos.')
        print('A chance de sucesso é muito alta. Mudaremos o mundo mais uma vez, dr. Helena Smith.')

print('')

print('Aqui estão os dados dos acontecimentos:')
for i in range(num_eventos):
    print(f'{lista_acontecimento[i]} | gap: {lista_anos[i]} anos e {lista_meses[i]} meses | nível de relevância: {lista_nivel[i]}')
