dor_cabeca = 0
insonia = 0
pesadelos = 0
suor_frio = 0
visoes = 0

saida = True 
perigo_max = False 
possiveis_vitimas = 0 
lista_nomes_possiveis_vitimas = []

while saida:
    entrada = input()
    if entrada == 'descobrir':
        saida = False 
    else:
        dor_cabeca = 0
        insonia = 0
        pesadelos = 0
        suor_frio = 0
        visoes = 0
        lista_sintomas_aluno = entrada.split(',')
        for sintoma in lista_sintomas_aluno[1::]:
          if sintoma == ' dor de cabeca':
            dor_cabeca = 1
          elif sintoma == ' insonia':
            insonia = 1
          elif sintoma == ' pesadelos':
            pesadelos = 1
          elif sintoma == ' suor frio':
            suor_frio = 1
          elif sintoma == ' visoes':
            visoes = 1
            
        soma = dor_cabeca + insonia + pesadelos + suor_frio + visoes
        
        if soma == 5 and lista_sintomas_aluno[0] == 'Max':
          perigo_max = True 
        elif soma == 5 and lista_sintomas_aluno[0] != 'Max':
          possiveis_vitimas += 1 
          lista_nomes_possiveis_vitimas.append(lista_sintomas_aluno[0])

nomes_possiveis_vitimas = ''

for i in range(len(lista_nomes_possiveis_vitimas)):
    if  i == (len(lista_nomes_possiveis_vitimas) - 1):
        nomes_possiveis_vitimas += 'e ' + lista_nomes_possiveis_vitimas[i]
    else:
        nomes_possiveis_vitimas += lista_nomes_possiveis_vitimas[i] + ', '

nomes_possiveis_vitimas = nomes_possiveis_vitimas.replace(', e',' e')

if possiveis_vitimas == 0 and perigo_max == False:
    print('Não conseguimos encontrar ninguém com esses sintomas, o próximo ataque do Vecna será imprevisível.')
elif perigo_max == True and possiveis_vitimas == 0:
    print("Oh não, Max está em perigo! Let's run up that hill com a Kate Bush e ajudar nossa amiga.")
elif perigo_max == True and possiveis_vitimas == 1:
    print("Oh não, Max está em perigo! Let's run up that hill com a Kate Bush e ajudar nossa amiga.")
    print(f"Além dela, tem mais {possiveis_vitimas} pessoa(s) na mira do Vecna!")
    print(f"Precisamos avisar {lista_nomes_possiveis_vitimas[0]} para preparar sua música favorita.")
elif perigo_max == True and possiveis_vitimas > 1:
    print("Oh não, Max está em perigo! Let's run up that hill com a Kate Bush e ajudar nossa amiga.")
    print(f"Além dela, tem mais {possiveis_vitimas} pessoa(s) na mira do Vecna!")
    print(f'Precisamos avisar {nomes_possiveis_vitimas} para prepararem suas músicas favoritas.')
elif perigo_max == False and possiveis_vitimas == 1:
    print(f'Tem {possiveis_vitimas} pessoa(s) na mira do Vecna!')
    print(f'Precisamos avisar {lista_nomes_possiveis_vitimas[0]} para preparar sua música favorita.')
elif perigo_max == False and possiveis_vitimas > 1:
     print(f'Tem {possiveis_vitimas} pessoa(s) na mira do Vecna!')
     print(f'Precisamos avisar {nomes_possiveis_vitimas} para prepararem suas músicas favoritas.')

        
        
        