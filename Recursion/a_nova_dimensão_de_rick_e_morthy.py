#Função recursiva de cálculo de fatorial.
def fatorial(numero):
    if numero <= 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

#Função recursiva para encontrar a quantidade de letras minúsculas e maiúsculas.
def verificador(entrada, cont1, cont2):
    if len(entrada) == 0:
        return cont1, cont2
    else:
        if entrada[-1].isupper() == True:
            cont1  += 1
        elif entrada[-1].islower() == True:
            cont2 += 1
        return verificador(entrada[:-1], cont1, cont2)

#Recebendo a entrada.
entrada = input()

#Definindo os contadores para as letras.
contador_maiuscula = 0
contador_minuscula = 0

#Colocando os valores da função 'verificar' nos contadores.
contador_maiuscula = verificador(entrada, contador_maiuscula, contador_minuscula)[0]
contador_minuscula = verificador(entrada, contador_maiuscula, contador_minuscula)[1]

#Definindo qual tipo de letra está em maior quantidade.
maior = 0
if contador_maiuscula > contador_minuscula:
    maior = contador_maiuscula
else:
    maior = contador_minuscula

#Estabelecendo a combinação.
combinacao = int((fatorial(contador_maiuscula + contador_minuscula))/(fatorial(maior) * (fatorial((contador_maiuscula + contador_minuscula) - maior))))

#encontrando CHAR.
posicao_letra = combinacao % maior

letra = entrada[posicao_letra]



if letra.islower() == True:
    print(f'Oh geez, Rick!!! Eu não sei se ir pra dimensão {letra}-{combinacao} é uma boa ideia... Eu estou com medo, Rick!!! Oh geez!!!')
elif letra.isupper() == True:
    print(f'Morty!!! Morty!!! Vamos para a dimensão {letra}-{combinacao}, Morty!!! Vai ser legal, Morty!!! Rick e Morty na dimensão {letra}-{combinacao} para sempre, Morty!!! Wubba lubba dub dub!!!')