#Função para calcular a soma das matrizes.
def soma(a, b, c):
    resultado = []
    resultado2 = []
    for i in range(a):
        for j in range(a):
            soma = b[i][j] + c[i][j]
            resultado.append(soma)
        resultado2.append(resultado[:])
        resultado.clear()
    return resultado2

#Função para calcular a subtração das matrizes.
def subtracao(a, b, c):
    resultado = []
    resultado2 = []
    for i in range(a):
        for j in range(a):
            subtracao = b[i][j] - c[i][j]
            resultado.append(subtracao)
        resultado2.append(resultado[:])
        resultado.clear()
    return resultado2

#Função para calcular a multiplicação das matrizes por escalar.
def escalar(a, b, c):
    linha = []
    for i in range(a):
        i = 0
        linha.append(i)
    matriz_resultado = []
    for i in range(a):
        matriz_resultado.append(linha[:])

    for i in range(a):
        for j in range(a):
            matriz_resultado[i][j] = c * b[i][j]
    return matriz_resultado

#Função para calcular a multiplicação das matrizes.
def multiplicacao(a, b, c):
    linha = []
    for i in range(c):
        i = 0
        linha.append(i)
    matriz_resultado = []
    for i in range(c):
        matriz_resultado.append(linha[:])

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                matriz_resultado[i][j] += int((a[i][k] * b[k][j]))
    return matriz_resultado

#Criando duas matrizes a partir de uma entrada.
tam_matriz = int(input())
lista_matrizes = []

for i in range(2):
    matriz = []
    for j in range(tam_matriz):
        matriz.append(input().split())

    for j in range(tam_matriz):
        for k in range(tam_matriz):
            matriz[j][k] = int(matriz[j][k])

    lista_matrizes.append(matriz)

m1 = lista_matrizes[0]
m2 = lista_matrizes[1]

#Recebendo a quantidade de operações a serem feitas.
qnt_operações = int(input())

#Aqui eu guardo todas as entradas recebidas para que eu possa usa-las no final do codigo.
lista_entradas = []

#Aqui são realizadas todas as operações solicitadas.
for i in range(qnt_operações):
    entrada = input().split()
    lista_entradas.append(entrada)
    if entrada[3] == '+':
        if entrada [0] == 'm1' and entrada[2] == 'm1' and entrada[4] == 'm2':
            m1 = soma(tam_matriz, m1, m2)
        elif entrada[0] == 'm2' and entrada[2] == 'm1' and entrada[4] == 'm2':
           m2 = soma(tam_matriz, m1, m2)
        elif entrada[0] == 'm1' and entrada[2] == 'm2' and entrada[4] == 'm1':
            m1 = soma(tam_matriz, m2, m1)
        elif entrada[0] == 'm2' and entrada[2] == 'm2' and entrada[4] == 'm1':
            m2 = soma(tam_matriz, m2, m1)
        elif entrada[0] == 'm1' and entrada[2] == 'm1' and entrada[4] == 'm1':
           m1 =  soma(tam_matriz, m1, m1)
        elif entrada[0] == 'm2' and entrada[2] == 'm1' and entrada[4] == 'm1':
            m2 = soma(tam_matriz, m1, m1)
        elif entrada[0] == 'm1' and entrada[2] == 'm2' and entrada[4] == 'm2':
            m1 = soma(tam_matriz, m2, m2)
        elif entrada[0] == 'm2' and entrada[2] == 'm2' and entrada[4] == 'm2':
            m2 = soma(tam_matriz, m2, m2)
    elif entrada[3] == '-':
        if entrada[0] == 'm1' and entrada[2] == 'm1' and entrada[4] == 'm2':
            m1 = subtracao(tam_matriz, m1, m2)
        elif entrada[0] == 'm2' and entrada[2] == 'm1' and entrada[4] == 'm2':
            m2 = subtracao(tam_matriz, m1, m2)
        elif entrada[0] == 'm1' and entrada[2] == 'm2' and entrada[4] == 'm1':
            m1 = subtracao(tam_matriz, m2, m1)
        elif entrada[0] == 'm1' and entrada[2] == 'm2' and entrada[4] == 'm1':
            m2 = subtracao(tam_matriz, m2, m1)
        elif entrada[0] == 'm1' and entrada[2] == 'm1' and entrada[4] == 'm1':
            m1 = subtracao(tam_matriz, m1, m1)
        elif entrada[0] == 'm2' and entrada[2] == 'm1' and entrada[4] == 'm1':
            m2 = subtracao(tam_matriz, m1, m1)
        elif entrada[0] == 'm1' and entrada[2] == 'm2' and entrada[4] == 'm2':
            m1 = subtracao(tam_matriz, m2, m2)
        elif entrada[0] == 'm2' and entrada[2] == 'm2' and entrada[4] == 'm2':
            m2 = subtracao(tam_matriz, m2, m2)
    elif entrada[3] == '*':
        if entrada[0] == 'm1' and entrada[2] == 'm1':
            m1 = escalar(tam_matriz, m1, int(entrada[4]))
        elif entrada[0] == 'm1' and entrada[2] == 'm2':
            m1 = escalar(tam_matriz, m2, int(entrada[4]))
        elif entrada[0] == 'm2' and entrada[2] == 'm1':
            m2 = escalar(tam_matriz, m1, int(entrada[4]))
        elif entrada[0] == 'm2' and entrada[2] == 'm2':
            m2 = escalar(tam_matriz, m2, int(entrada[4]))
        elif entrada[0] == 'm1' and entrada[4] == 'm1':
            m1 = escalar(tam_matriz, m1, int(entrada[2]))
        elif entrada[0] == 'm1' and entrada[4] == 'm2':
            m1 = escalar(tam_matriz, m2, int(entrada[2]))
        elif entrada[0] == 'm2' and entrada[4] == 'm1':
            m2 = escalar(tam_matriz, m1, int(entrada[2]))
        elif entrada[0] == 'm2' and entrada[4] == 'm2':
            m2 = escalar(tam_matriz, m2, int(entrada[2]))
    elif entrada[3] == '.':
        if entrada[0] == 'm1' and entrada[2] == 'm1' and entrada[4] == 'm2':
            m1 = multiplicacao(m1, m2, tam_matriz)
        elif entrada[0] == 'm2' and entrada[2] == 'm1' and entrada[4] == 'm2':
            m2 = multiplicacao(m1, m2, tam_matriz)
        elif entrada[0] == 'm1' and entrada[2] == 'm2' and entrada[4] == 'm1':
            m1 = multiplicacao(m2, m1, tam_matriz)
        elif entrada[0] == 'm2' and entrada[2] == 'm2' and entrada[4] == 'm1':
            m2 = multiplicacao( m2, m1, tam_matriz)
        elif entrada[0] == 'm1' and entrada[2] == 'm1' and entrada[4] == 'm1':
            m1 = multiplicacao(m1, m1, tam_matriz)
        elif entrada[0] == 'm2' and entrada[2] == 'm1' and entrada[4] == 'm1':
            m2 = multiplicacao(m1, m1, tam_matriz)
        elif entrada[0] == 'm1' and entrada[2] == 'm2' and entrada[4] == 'm2':
            m1 = multiplicacao(m2, m2, tam_matriz)
        elif entrada[0] == 'm2' and entrada[2] == 'm2' and entrada[4] == 'm2':
            m2 = multiplicacao(m2, m2, tam_matriz)

#Imprimindo resultado final.
if lista_entradas[-1][0] == 'm1':
    for i in m1:
        print(*i)
elif lista_entradas[-1][0] == 'm2':
    for i in m2:
        print(*i)