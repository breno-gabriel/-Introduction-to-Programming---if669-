nome_fogo = input()
decibeis_felipe = int(input())
decibeis_caruaru = int(input())
decibeis_campina = int(input())
if decibeis_felipe <= decibeis_caruaru and decibeis_felipe <= decibeis_campina:
  print(f'Boa Felipe, o {nome_fogo} será um sucesso em Campina Grande e Caruaru!')
elif decibeis_caruaru < decibeis_felipe <= decibeis_campina:
  print(f'Infelizmente em Caruaru não vai rolar, mas em Campina Grande o {nome_fogo} vai ser extouro!')
elif decibeis_caruaru >= decibeis_felipe > decibeis_campina:
    print(f'Infelizmente em Campina Grande não vai rolar, mas em Caruaru o {nome_fogo} vai ser extouro!')
else:
    print(f'Poxa Felipe, não vai ser dessa vez que {nome_fogo} fará um sucesso pelas festas juninas do Brasil')

