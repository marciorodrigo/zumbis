# -*- coding: utf-8 -*- 


qtd = int(input("Informe a quantidade de cigarros fumados por dia: "))
anos = int(input("Informe a quanto tempo fuma: "))

total = (float(qtd) / 144.0) * (anos * 365)

print "O total de dias perdidos é de %d" %total