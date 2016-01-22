# -*- coding: utf-8 -*- 


dst = float(input("Informe a distância percorrida (km/h): "))
dias = int(input("Informe a quantidade de dias que o carro ficou alugado: "))

total = 60 * dias + dst * 0.15

print "O total a ser pago é de %3.2f" %total