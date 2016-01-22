# -*- coding: utf-8 -*- 

nota = float(input("Informe a nota: "))
while ((nota < 0.0) or (nota > 10.0)):
	print ("A nota deve estar entre 0 e 10.")
	nota = float(input("Informe a nota: "))

print ("Valor %3.2f válido" %nota)