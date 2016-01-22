# -*- coding: utf-8 -*- 


sal = float(input("Informe o valor da hora trabalhada: "))
horas = float(input("Informe a quantidade de horas trabalhadas no mês: "))


sal *= horas
print("+Salário Bruto: R$ %.2f" %sal)

ir = sal * 11 / 100
print("-IR (11%%): R$ %.2f" %ir)
inss = sal * 8 / 100
print("-INSS (8%%): R$ %.2f" %inss)
sind = sal * 5 / 100
print("-Sindicato (5%%): R$ %.2f" %sind)

total = sal - (ir + inss + sind)
print "=Salário Líquido: R$ %.2f" %total