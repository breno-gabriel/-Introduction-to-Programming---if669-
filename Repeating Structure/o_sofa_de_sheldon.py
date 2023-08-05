temperatura = 30
fome = True
internet = 0

saida = True

while saida:
  acoes = input()
  if acoes == 'ir para o grad':
    temperatura -= 5
    internet += 300
  elif acoes == 'sair para a rua':
    temperatura += 5
  elif acoes == 'comer uma quentinha':
    fome = False
  elif acoes == 'conectar no wifi':
    internet += 100
  elif acoes == 'parar':
    saida = False 
  else:
    print('Entrada inválida')
  
if temperatura <= 25 and internet >= 300 and fome == False:
    print('Agora sim, está aconchegante')
    print('Finalmente um lugar preciso para mim!')
elif temperatura >= 30 and internet >= 100 and fome == False:
    print('A temperatura aqui não está agradável')
elif temperatura >= 30 and internet < 100 and fome == False:
    print('A temperatura aqui não está agradável')
    print('Essa conexão está horrível')
elif temperatura >= 30 and internet >= 100 and fome == True:
    print('A temperatura aqui não está agradável')
    print('Meu corpo precisa de comida')
elif temperatura <= 25 and internet >= 100 and fome == True:
    print('Agora sim, está aconchegante')
    print('Meu corpo precisa de comida')
elif temperatura <= 25 and internet < 100 and fome == False:
    print('Agora sim, está aconchegante')
    print('Essa conexão está horrível')
elif temperatura >= 30 and internet < 100 and fome == True:
    print('A temperatura aqui não está agradável')
    print('Meu corpo precisa de comida')
    print('Essa conexão está horrível')

 
