#Definindo a função de soma.
def soma():
    soma = 0 
    for i in lista_numeros:
        soma += i 
    print(soma)

#Definindo a função de subtração.
def subtração():
    subtracao = lista_numeros[0]
    for i in lista_numeros[1:]:
        subtracao -= i 
    print(subtracao)

#Definindo a função de multiplicação.
def multiplicação():
    multiplicacao = 1
    for i in lista_numeros:
        multiplicacao *= i 
    print(multiplicacao)

#Definindo a função de divisão.
def divisão():
    divisao = lista_numeros[0]
    for i in lista_numeros[1:]:
        divisao /= i 
    print(divisao)

#Looping onde ocoerrerá o cálculo(Aqui é que começa o programa de fato).
verificacao = '1'
while verificacao == '1':
    # criando uma lista para armazenar os números que será operados.
    lista_numeros = []
    #Tipo de operação.
    tipo_operacao = input()

    #Recebendo a entrada com a quantidade de números a serem trabalhados.
    qunt_num = int(input())

    #Recebendo os números que serão operados.
    for i in range(qunt_num):
        numero = int(input())
        lista_numeros.append(numero)

    #Recebendo o número que irá determinar a contiuidade ou termino da operação.
    verificacao = input()

    #Definindo qual função será usada, de acordo com o tipo de operação.
    if tipo_operacao == 'M':
        multiplicação()
    elif tipo_operacao == 'S':
        soma()
    elif tipo_operacao == 'sub':
        subtração()
    elif tipo_operacao == 'D':
        divisão()