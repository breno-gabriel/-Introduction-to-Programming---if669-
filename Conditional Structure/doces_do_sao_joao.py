doce1 = input()
quant_doce1 = int(input())
doce2 = input()
quant_doce2 = int(input())
doce3 = input()
quant_doce3 = int(input())

faturamento_doce1 = quant_doce1 * 2
faturamento_doce2 = quant_doce2 * 5
faturamento_doce3 = quant_doce3 * 3

if faturamento_doce2 == faturamento_doce2 == faturamento_doce3 == 0:
    print('A ideia foi peba! Acho melhor encontrar um novo jeito de ganhar dinheiro...')
else:
  if faturamento_doce1 > faturamento_doce2 and faturamento_doce1 == faturamento_doce3:
    print(f'Oxe! Você ganhou {faturamento_doce1} reais vendendo {doce1}. O povo gostou, visse?!')
  elif faturamento_doce2 > faturamento_doce1 and faturamento_doce2 == faturamento_doce3:
    print(f'Oxe! Você ganhou {faturamento_doce3} reais vendendo {doce3}. O povo gostou, visse?!')
  elif faturamento_doce3 > faturamento_doce1 and faturamento_doce3 == faturamento_doce2:
    print(f'Oxe! Você ganhou {faturamento_doce2} reais vendendo {doce2}. O povo gostou, visse?!')

if faturamento_doce1 > faturamento_doce2 and faturamento_doce1 > faturamento_doce3:
    print(f'Oxe! Você ganhou {faturamento_doce1} reais vendendo {doce1}. O povo gostou, visse?!')
elif faturamento_doce2 > faturamento_doce1 and faturamento_doce2 > faturamento_doce3:
    print(f'Oxe! Você ganhou {faturamento_doce2} reais vendendo {doce2}. O povo gostou, visse?!')
elif faturamento_doce3 > faturamento_doce1 and faturamento_doce3 > faturamento_doce2:
    print(f'Oxe! Você ganhou {faturamento_doce3} reais vendendo {doce3}. O povo gostou, visse?!')

    

