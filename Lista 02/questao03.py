# -*- coding: utf-8 -*- 

peso = float(input("Informe o peso de peixes pesado: "))

excesso = peso - 50

if excesso > 0:
	multa = excesso * 4
else:
	multa = 0
	excesso = 0

print "O excesso de peso é de %.3f e a multa é de R$ %.2f" %(excesso, multa)