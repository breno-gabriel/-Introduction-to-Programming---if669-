nome1 = input()
pontuacao1 = int(input())
nome2 = input()
pontuacao2 = int(input())
nome3 = input()
pontuacao3 = int(input())

if pontuacao1 < pontuacao2 and pontuacao1 < pontuacao3:
    nome_primeiro = nome1
    pontuacao_primeiro = pontuacao1
    if pontuacao2 < pontuacao3:
        nome_segundo = nome2
        pontuacao_segundo = pontuacao2
        nome_terceiro = nome3
        pontuacao_terceiro = pontuacao3
    else:
        nome_segundo = nome3
        pontuacao_segundo = pontuacao3
        nome_terceiro = nome2
        pontuacao_terceiro = pontuacao2

if pontuacao2 < pontuacao1 and pontuacao2 < pontuacao3:
    nome_primeiro = nome2
    pontuacao_primeiro = pontuacao2
    if pontuacao1 < pontuacao3:
        nome_segundo = nome1
        pontuacao_segundo = pontuacao1
        nome_terceiro = nome3
        pontuacao_terceiro = pontuacao3
    else:
        nome_segundo = nome3
        pontuacao_segundo = pontuacao3
        nome_terceiro = nome1
        pontuacao_terceiro = pontuacao1

if pontuacao3 < pontuacao1 and pontuacao3 < pontuacao2:
    nome_primeiro = nome3
    pontuacao_primeiro = pontuacao3
    if pontuacao1 < pontuacao2:
        nome_segundo = nome1
        pontuacao_segundo = pontuacao1
        nome_terceiro = nome2
        pontuacao_terceiro = pontuacao2
    else:
        nome_segundo = nome2
        pontuacao_segundo = pontuacao2
        nome_terceiro = nome1
        pontuacao_terceiro = pontuacao1

if pontuacao1 < pontuacao3 and pontuacao1 == pontuacao2:
    if nome1 < nome2:
        nome_primeiro = nome1
        pontuacao_primeiro = pontuacao1
        nome_segundo = nome2
        pontuacao_segundo = pontuacao2
        nome_terceiro = nome3
        pontuacao_terceiro = pontuacao3
    else:
        nome_primeiro = nome2
        pontuacao_primeiro = pontuacao2
        nome_segundo = nome1
        pontuacao_segundo = pontuacao1
        nome_terceiro = nome3
        pontuacao_terceiro = pontuacao3

if pontuacao1 < pontuacao2 and pontuacao1 == pontuacao3:
    if nome1 < nome3:
        nome_primeiro = nome1
        pontuacao_primeiro = pontuacao1
        nome_segundo = nome3
        pontuacao_segundo = pontuacao3
        nome_terceiro = nome2
        pontuacao_terceiro = pontuacao2
    else:
        nome_primeiro = nome3
        pontuacao_primeiro = pontuacao3
        nome_segundo = nome1
        pontuacao_segundo = pontuacao1
        nome_terceiro = nome2
        pontuacao_terceiro = pontuacao2

if pontuacao3 < pontuacao1 and pontuacao3 == pontuacao2:
    if nome3 < nome2:
        nome_primeiro = nome3
        pontuacao_primeiro = pontuacao3
        nome_segundo = nome2
        pontuacao_segundo = pontuacao2
        nome_terceiro = nome1
        pontuacao_terceiro = pontuacao1
    else:
        nome_primeiro = nome2
        pontuacao_primeiro = pontuacao2
        nome_segundo = nome3
        pontuacao_segundo = pontuacao3
        nome_terceiro = nome1
        pontuacao_terceiro = pontuacao1

if pontuacao1 == pontuacao2 == pontuacao3:
    if nome1 < nome2 and nome1 < nome3:
        nome_primeiro = nome1
        pontuacao_primeiro = pontuacao1
        if nome2 < nome3:
            nome_segundo = nome2
            pontuacao_segundo = pontuacao2
            nome_terceiro = nome3
            pontuacao_terceiro = pontuacao3
        else:
            nome_segundo = nome3
            pontuacao_segundo = pontuacao3
            nome_terceiro = nome2
            pontuacao_terceiro = pontuacao2
    if nome2 < nome1 and nome2 < nome3:
        nome_primeiro = nome2
        pontuacao_primeiro = pontuacao2
        if nome1 < nome3:
            nome_segundo = nome1
            pontuacao_segundo = pontuacao1
            nome_terceiro = nome3
            pontuacao_terceiro = pontuacao3
        else:
            nome_segundo = nome3
            pontuacao_segundo = pontuacao3
            nome_terceiro = nome2
            pontuacao_terceiro = pontuacao2
    if nome3 < nome1 and nome3 < nome2:
        nome_primeiro = nome3
        pontuacao_primeiro = pontuacao3
        if nome1 < nome2:
            nome_segundo = nome1
            pontuacao_segundo = pontuacao1
            nome_terceiro = nome2
            pontuacao_terceiro = pontuacao2
        else:
            nome_segundo = nome3
            pontuacao_segundo = pontuacao2
            nome_terceiro = nome1
            pontuacao_terceiro = pontuacao1

print(nome_primeiro, pontuacao_primeiro)
print(nome_segundo, pontuacao_segundo)
print(nome_terceiro, pontuacao_terceiro)