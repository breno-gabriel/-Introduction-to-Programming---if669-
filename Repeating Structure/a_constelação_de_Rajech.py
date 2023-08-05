estrelas = int(input())
contador_fibonacci = 0 
soma_primo = 0 
contador_primo = 0 
primo = True 

if estrelas <= 0:
  print('Isso está quebrado, acho que Howard pode me ajudar.')
elif 0 < estrelas < 3:
  print('Acho que bebi demais, eu juro que tinha mais estrelas!')
else:
  x1 = int(input())
  y1 = int(input())
  for i in range(estrelas - 1):
    x2 = int(input())
    y2 = int(input())
    dist = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
    soma_primo += dist
    x1 = x2 
    y1 = y2
    print(f'Distância [star{i + 1} <-> star{i + 2}]: {int(dist)}')
    
    primeiro = 0 
    segundo = 1 
    terceiro = 0 
    fibo = True 
    
    while dist >= terceiro:
      if dist == terceiro:
        fibo = True
        contador_fibonacci += 1 
        
      else:
        fibo = False 
        
      terceiro = primeiro + segundo
      primeiro = segundo 
      segundo = terceiro 
    
  for c in range(1, soma_primo + 1):
    if soma_primo % c == 0:
      contador_primo += 1 
        
  if contador_primo == 2:
    primo = True 
  else:
    primo = False 
    
  if contador_fibonacci == estrelas - 1 and primo == False:
    print('Yes! Eu consegui!')
  elif contador_fibonacci == estrelas -1  and primo == True:
    print('Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!')
  elif contador_fibonacci == estrelas - 2:
    print('Oh, não! Eu quase consegui!')
  elif contador_fibonacci < estrelas - 2 and primo == False:
    print('Eu vou acabar como o Stuart :/')
  elif contador_fibonacci < estrelas - 2 and primo == True:
    print('Pelo menos o programa está funcionando...')
      
  
