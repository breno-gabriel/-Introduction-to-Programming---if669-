def verificador(expressao, cont1, cont2):
    if len(expressao) == 0:
        return cont1, cont2
    else:
        if expressao[-1] == '(':
          cont1 += 1
        elif expressao[-1] == ')':
          cont2 += 1 
        return verificador(expressao[:-1], cont1, cont2)
        
        
num = int(input())

for i in range(num):
    entrada = input()
    contador1 = 0 
    contador2 = 0 
    resultado = verificador(entrada, contador1, contador2)
    if resultado[0] == resultado[1]:
        print('Essa sentença está com os parênteses balanceados, HOORAY!')
    elif resultado[0] > resultado[1]:
        print("A quantidade de parênteses '(' está maior que a de ')', vamos descartá-la")
    else:
        print("A quantidade de parênteses ')' está maior que a de '(', vamos descartá-la")
    