# -*- coding: utf-8 -*- 


notas = [50, 20, 10, 5, 2, 1]

total = int(input("Informe o total da conta: "))
pago = int(input("Informe o valor pago: "))

troco = int(pago - total)
print ("Troco a ser dado %d" %troco)

i = 0
cont = 0
trocado = []
while troco:
	
	if troco < notas[i]:
		trocado.append(cont)
		
		i += 1
		cont = 0
		if i > len(notas):
			break
		
	else:
		cont += 1
		troco -= notas[i]

for i in range(0, len(trocado)):
	if trocado[i] != 0:
		print ("Notas de %d: %d" % (notas[i], trocado[i]))