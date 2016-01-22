# -*- coding: utf-8 -*- 


preco = float(input("Informe o preço do produto: "))
porcentagem = float(input("Informe o porcentual de desconto: "))

desconto = preco * porcentagem / 100
print "O desconto é de %3.2f e o novo preço vai ser de %3.2f" %(desconto, preco - desconto)