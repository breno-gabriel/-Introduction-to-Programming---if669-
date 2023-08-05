planetas = int(input())
saida = True
melhor = 0
nome_melhor_planeta = ''

while saida:
    if planetas < 2:
        print('Número inválido, tente novamente')
        planetas = int(input())
    else:
        saida = False

for i in range(planetas):
    nome = input()
    raio = float(input())
    massa = float(input())
    temperatura = float(input())
    indice_habitabilidade = (raio + massa + (temperatura / 288)) / 3
    modulo = abs(1 - indice_habitabilidade)
    if i == 0:
      melhor_modulo = modulo
      nome_melhor_planeta = nome
      indice_melhor = indice_habitabilidade
    if modulo < melhor_modulo:
      melhor_modulo = modulo
      nome_melhor_planeta = nome 
      indice_melhor = indice_habitabilidade
if indice_melhor == 1:
    print(f'{nome_melhor_planeta} é perfeito!')
elif indice_melhor > 1:
    print(f'{nome_melhor_planeta} vai ter que servir')
elif indice_melhor < 1:
    print(f'{nome_melhor_planeta} vai dar pro gasto')