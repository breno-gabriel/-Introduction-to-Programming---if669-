saida = True 
gostou = 0 
nao_gostou = 0 

while saida:
  piada = input()
  if piada == 'Fim do Show!':
    saida = False
  else:
    reação = input()
    if reação == 'BAZINGA!':
      gostou += 1
    elif reação != 'BAZINGA!':
      nao_gostou += 1
    
porcentagem_boas = (gostou * 100)/(gostou + nao_gostou)

porcentagem_ruins = 100 - porcentagem_boas

if porcentagem_boas > 60:
  print('BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!')
elif porcentagem_ruins <= 60 and porcentagem_boas <= 60:
  print('Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!')
else:
  print('Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!')

  