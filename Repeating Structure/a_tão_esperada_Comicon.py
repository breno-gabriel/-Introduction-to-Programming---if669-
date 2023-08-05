positivo = 0 
negativo = 0 

instrucoes = input()
if instrucoes == '0001':
  instrucoes = 1 
elif instrucoes == '0010':
  instrucoes = 2
elif instrucoes == '0011':
  instrucoes = 3
elif instrucoes == '0100':
  instrucoes = 4
  
for c in range(instrucoes):
  tipo_corpo = input()
  if tipo_corpo == '0101':
    beleza = 0 
    temperatura = 0 
    luas = 0 
    agua = 0 
    vida = 0 
    saida = True 
    while saida:
      informacao = input()
      if informacao == 'End':
        saida = False 
      elif informacao == 'Beleza':
        valor = input()
        if valor == '1':
          beleza = 1
        else:
          beleza = 0 
      elif informacao == 'Possibilidade de vida extraterrestre':
        valor = input()
        if valor == '1':
          vida = 1
        else:
          vida = 0 
      elif informacao == 'Agua aparente':
        valor = input()
        if valor == '1':
          agua = 1
        else:
          agua = 0 
      elif informacao == 'Temperatura adequada':
        valor = input()
        if valor == '1':
          temperatura = 1
        else:
          temperatura = 0 
      elif informacao == 'Quantidade de luas':
        qnt_luas = input()
        if qnt_luas == '0001':
          qnt_luas = 1 
        elif qnt_luas == '0010':
          qnt_luas = 2
        elif qnt_luas == '0011':
          qnt_luas = 3
    if agua == 1 and temperatura == 1 and vida == 1 and beleza == 1:
      print(f'Achamos o planeta ideal e ainda tem {qnt_luas} lua(s)!')
      print('Parece bom demais pra ser verdade, que tipo de vida sera que nos aguarda?')
    elif agua == 1 and temperatura == 1 and beleza == 1 and vida == 0:
      print('Ainda nao sabemos se o planeta e habitavel, parece nao haver vida')
    elif agua == 1 and temperatura == 1 and vida == 1 and beleza == 0:
      print(f'O planeta e possivelmente habitavel porem olha essa aparencia, mesmo que tenha {qnt_luas} lua(s) vamos omitir esse do relatorio!')
    else:
      print('Vish! Esse nao satisfaz nem as condicoes basicas, nao perderemos tempo')    
  elif tipo_corpo == '1101':
    qunt_planetas = input()
    if qunt_planetas == '01100100':
      qunt_planetas = 100 
    elif qunt_planetas == '11001000':
      qunt_planetas = 200
    elif qunt_planetas == '100101100':
      qunt_planetas = 300
    buraco_super = input()
    if buraco_super == '1':
      print(f'Ha um buraco negro supermassivo nesta galaxia, demais! Alem da existencia de cerca de {qunt_planetas} milhoes de planetas')
    else:
      print(f'Aparentemente nao ha nenhum buraco negro supermassivo no centro dessa galaxia, jurava que todas tinham! Nao importa, ainda temos {qunt_planetas} milhoes de planetas para observar algum deve apresentar possiblidade de vida')
  elif tipo_corpo == '0000':
    massa = input()
    if massa == '0101':
      massa = 5
    elif massa == '1010':
      massa = 10 
    elif massa == '1111':
      massa = 15 
    spin = input()
    if spin == '0':
      spin = 0
    elif spin == '1':
      spin = 1
    carga = input()
    if carga == '0000':
      carga = 0
    elif carga == '0001':
      carga = 1
    else: 
      carga = 2 
    print('Conseguimos todas informacoes necessarias para classificar este buraco negro no nosso banco de dados!')
    print('De acordo com as analises, o buraco negro:')
    print(f'- Tem massa de aproximadamente {massa} milhoes massas solares')
    print(f'- Possui em media {spin} rotacao(oes) por segundo')
    if carga == 0:
      print('- Apresenta carga inexistente ou nula')
    elif carga == 1:
      print('- Apresenta carga positiva')
    elif carga == 2:
      print('- Apresenta carga negativa')
    
