#Criando a função para analisar os sons.
def analisar(entrada):
  som_inseto = False 
  som_aviao = False 
  for i in entrada:
    if i == 'crcrcrcrcr' or i == 'uuuuuuuoooooo' or i == 'ooooooeeeeeeee':
      som_inseto = True 
    if i == 'ppprrrrrooon' or i == 'tutututututututu' or i == 'eeeeeeeeoooooo':
      som_aviao = True 
    
  if som_inseto and not som_aviao:
    res = 1
  elif not som_inseto and som_aviao:
    res = 2
  elif som_inseto and som_aviao:
    res = 3 
  elif not som_inseto and not som_aviao:
    res = 4
  return res
 
#Programa de fato.
fim_transmissao = False
while not fim_transmissao:
  transmissao = input().split(' ')
  if analisar(transmissao) == 1:
    print('É apenas o Mar Podre se comunicando, podemos ficar tranquilos, por enquanto…')
  elif analisar(transmissao) == 2:
    print('São sinais de aeronaves estrangeiras! Devemos preparar nossas defesas??')
  elif analisar(transmissao) == 3:
    print('A transmissão sugere que tropas estrangeiras e as criaturas do Mar Podre irão se confrontar! Precisamos impedi-los antes que mais mortes desnecessárias ocorram!')
  elif analisar(transmissao) == 4:
    print('Não é possível determinar a origem da transmissão… Isso deverá levar mais algum tempo.')
    fim_transmissao = True  