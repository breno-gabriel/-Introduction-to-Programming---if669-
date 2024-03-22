def fibonnaci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonnaci(num - 1) + fibonnaci(num - 2)

def fatorial(num):
    if num <= 0:
        return 1
    else:
        return num * fatorial(num - 1)


senha_alterada = input()

qunt_palavras = int(input())

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

senha_encontrada = False 

for i in range(qunt_palavras):
    palavra =input()
    senha = ''
    for i in palavra:
        posicao = alfabeto.index(i)
        sequencia_fibo = []
        sequencia_fat = []
        mod = posicao % 11
        for j in range(mod):
            sequencia_fibo.append(fibonnaci(j))
        for k in range(mod):
            sequencia_fat.append(fatorial(k))
        if mod == 0:
            senha += '1'
        elif mod % 2 == 0:
            for l in range(mod):
                res = sequencia_fibo[l] + sequencia_fat[l]
                if res > 26:
                    res %= 26
                senha += alfabeto[res]
        else:
            for l in range(mod):
                res = sequencia_fibo[l] * sequencia_fat[l]
                if res > 26:
                    res %= 26
                senha += alfabeto[res]
    
    if senha == senha_alterada:
        senha_encontrada = True 

if senha_encontrada:
    print('Achamos! Achamos a senha.')
else:
    print('É... Temos que procurar mais.')
        





            
        
