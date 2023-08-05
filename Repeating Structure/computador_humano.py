entrada = int(input())
acerto = 0 
erro = 0 

for i in range(entrada):
  conversao = input()
  if conversao == 'DEC':
    binario = input()
    palpite = int(input())
    cont = 0
    soma = 0 
    for c in binario:
      cont += 1
      
    expoente = cont - 1 
    
    for f in binario:
      valor = int(f) * 2**expoente
      expoente -= 1 
      soma += valor 
      
    if soma == palpite: 
      acerto += 1
    else:
      print(f'Palpite Incorreto, o valor {binario} = {soma}')
      erro += 1
  elif conversao == 'BIN':
    decimal = int(input())
    palpite = input()
    numero_para_printar = decimal
    binario = ''
    
    if decimal == 0:
      binario = '0'
    else:
      while decimal > 1:
        resto = decimal % 2
        decimal = decimal // 2
        binario += str(resto)
      binario += '1'
      binario = binario[::-1]
    
    if palpite != binario:
      print(f'Palpite Incorreto, o valor {numero_para_printar} = {binario}')
      erro += 1
    else:
      acerto += 1 
      
porcentagem = (acerto * 100)/ (acerto + erro)

if porcentagem > 50:
  print('Bazinga! Quem realizou esses cálculos foi o computador??')
else:
  print('Parece que realizar conversões em binário não é o seu forte')