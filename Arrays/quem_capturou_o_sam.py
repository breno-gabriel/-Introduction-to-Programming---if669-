# Criando a lista.
lista_suspeitos = input().split(',')

# Realizando as operações na lista.
while len(lista_suspeitos) > 1:
    ordem = input()
    if ordem == 'Não encontrei nada no primeiro suspeito':
        del lista_suspeitos[0]
    elif ordem == 'O último da lista está limpo':
        del lista_suspeitos[-1]
    elif ordem == 'Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita':
        del lista_suspeitos[(len(lista_suspeitos)//2)]
    elif ordem == 'Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:':
        posicao_suspeito = int(input())
        del lista_suspeitos[posicao_suspeito]
    elif ordem == 'Acho que temos mais uma opção a ser analisada…':
        nome_novo_suspeito = input()
        lista_suspeitos.append(nome_novo_suspeito)
    else:
        print('Isso não estava no combinado, a lista vai permanecer do mesmo jeito')

# Imprimindo o resultado. 
print(f'Acho que encontramos o suspeito. O seu nome é {lista_suspeitos[0]}, vamos salvar o Sam!')
    