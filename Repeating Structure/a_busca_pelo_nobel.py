saida = True 
avancos = 0 
insultos = 0
caminho_certo = 0 
validacao_bazinga = False 

while saida:
  passos = input()
  if passos == 'É o fim da Estrada pra Sheldon Cooper':
    saida = False
    
  elif passos == 'Começou a Trabalhar na Caltech':
    if caminho_certo == 0:
      avancos = 1
      caminho_certo += 1
      validacao_bazinga = True 
  elif passos == 'Trabalho sobre a String Theory':
    if caminho_certo == 1:
      avancos = 2
      caminho_certo += 1
      validacao_bazinga = True
  elif passos == 'Ganhar o Chancellor de ciência':
    if caminho_certo == 2:
      avancos = 3
      caminho_certo += 1
      validacao_bazinga = True
  elif passos == 'Pensar na Teoria de Cooper-Hofstader':
    if caminho_certo == 3:
      avancos = 4
      caminho_certo += 1
      validacao_bazinga = True
  elif passos == 'Criou a Super Assimetria':
    if caminho_certo == 4:
      avancos = 5 
      caminho_certo += 1
      validacao_bazinga = True
  elif passos == 'Ganhar o Nobel':
    if caminho_certo == 5:
      avancos = 6 
      caminho_certo += 1
      validacao_bazinga = True 
      saida = False
  elif passos == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or passos == 'Leonard seu anão covarde' or passos == 'Tu é muito burro Raj':
    insultos += 1
    validacao_bazinga = False 
  elif passos == 'Bazinga' and validacao_bazinga == True:
    avancos -= 1
    validacao_bazinga = False 
  else:
    validacao_bazinga = False 

for c in range(insultos):
  print('Não xingue seus amigos Sheldon!')
  
if avancos == 0:
  print('Que potencial desperdiçado...')
elif avancos== 1 or avancos == 2:
  print('Tão perto, mas tão longe')
elif avancos == 3 or avancos == 4:
  print('Não desista Sheldon, você ainda têm muito para alcançar!')
elif avancos == 5:
  print('Nãoooooo, esse momento ia ser seu Sheldon')
elif avancos == 6:
  print('Você conseguiu Sheldon, o Nobel é seu!!!')