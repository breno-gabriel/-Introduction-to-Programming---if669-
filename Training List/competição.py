arthur = int(input())
luiz = int(input())
pedro = int(input())
horas = int(input())
quant_arthur = (arthur * horas)
quant_luiz = (luiz * horas)
quant_pedro = (pedro * horas)
comparação = ((quant_arthur + quant_pedro + abs(quant_arthur - quant_pedro))/2)
nova_comparação = ((comparação + quant_luiz + abs(comparação - quant_luiz))/2)
print(int(nova_comparação))