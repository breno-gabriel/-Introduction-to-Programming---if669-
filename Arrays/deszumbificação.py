num_frascos = int(input())

num_entradas = int(input())

lista_nome_elementos = []

lista_qunt_elementos = []

soma = 0

for i in range(num_entradas):
    entrada = input().split(' ')
    lista_nome_elementos.append(entrada[0])
    lista_qunt_elementos.append(entrada[1])

for i in range(len(lista_qunt_elementos)):
    lista_qunt_elementos[i] = int(lista_qunt_elementos[i])

lista = []

lista2 = []

cura = False

flag = False

nome_elementos = ''

for i in range(len(lista_qunt_elementos)):
    if lista_qunt_elementos[i] == num_frascos:
        nome_elementos += ' ' + lista_nome_elementos[i]
        cura = True
        break
    else:
        soma += lista_qunt_elementos[i]
        lista.append(lista_qunt_elementos[i])
        lista2.append(lista_nome_elementos[i])
        if soma == num_frascos:
            cura = True
            flag = True
            break
        elif soma > num_frascos:
            soma -= lista[0]
            del lista[0]
            del lista2[0]

if flag == True:
    for i in lista2:
        nome_elementos += ' ' + i

if cura == True:
    print(f'Vencemos a batalha e a humanidade foi restaurada!{nome_elementos} foram usados para deszumbificar')
elif cura == False:
    print('Estou sentido algo estranho... será que também vou virar zumbi?')


