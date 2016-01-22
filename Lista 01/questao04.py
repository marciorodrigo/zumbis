# -*- coding: utf-8 -*- 


salario = float(input("Informe o salário: "))
porcentagem = float(input("Informe a porcentagem de aumento: "))

aumento = salario * porcentagem / 100
print "O salário vai ser aumentado em %3.2f e o novo valor do salário vai ser de %3.2f" %(aumento, salario + aumento)