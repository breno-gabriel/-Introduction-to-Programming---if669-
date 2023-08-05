saida = True
batida = 0
chamado = 0
cont = 0

while saida:
  batida = input()
  if batida == 'Boa noite':
    print('Boa noite Penny')
    saida = False
  elif batida != 'toc-toc-toc':
    print('Não pode entrar, se identifique!!!')
    cont = 0
  else:
    for c in range(1, 3):
      if batida == 'toc-toc-toc':
        batida = input()
        if batida != 'Penny':
          print('Não pode entrar, se identifique!!!')
          cont = 0
        elif batida == 'Penny':
          cont += 1
          print(cont)
      if cont == 3:
        cont = 0
        print('Pode entrar Sheldon')
    

