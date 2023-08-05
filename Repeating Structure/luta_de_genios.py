local = int(input())
soma = 0
saida = True

while saida:
    numero = int(input())
    if numero >= 0:
      for i in range(1, numero + 1):
        soma += i
    else:
      saida = False    
    
if local == soma:
  print('Parabéns!!! Você é o mais inteligente')
elif local < soma:
  if soma < 20 * local:
    print('Parece que o gêniozinho passou um pouco do local...')
  elif 20 * local <= soma <= 100 * local:
    print('Acho que sua grande inteligência fez você se perder um pouco no caminho, onde estamos?')
  elif soma > 100 * local:
    print('Hum... acho que o gêniozinho não tem mesmo doutorado ein...')
elif local > soma:
  print('Ainda falta um pouco...')


