# -*- coding: utf-8 -*- 

area = float(input("Informe o tamanho da área a ser pintada: "))

total = int(area / 54) + 1
preco = total * 80

print "Total de lataas a serem compradas: %d - Preço: R$ %.2f" %(total, preco)