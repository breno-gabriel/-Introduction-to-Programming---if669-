def somadigitos(numero):
    if len(numero) == 1:
        return int(numero)
    else:
        return int(numero[-1]) + somadigitos(numero[:-1])

def mdc(m, n):
    if n == 0:
        return m
    else:
        return mdc(n, m % n)

lista_digitos_somados = []

for i in range(3):
    entrada = input()
    lista_digitos_somados.append(somadigitos(entrada))

resultado = mdc(lista_digitos_somados[0], lista_digitos_somados[1])

resultado = mdc(resultado, lista_digitos_somados[2])

print(f'O MDC obtido é: {resultado}')




