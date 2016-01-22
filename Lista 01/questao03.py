# -*- coding: utf-8 -*- 


dias = int(input("Informe o número de dias: "))
horas = int(input("Informe o número de horas: "))
minutos = int(input("Informe o número de minutos: "))
segundos = int(input("Informe o número de segundos: "))


total = segundos + (minutos * 60) + (horas * 3600) + (dias * 86400)
print "O total de segundos é %ld" %total