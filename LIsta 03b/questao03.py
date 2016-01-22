# -*- coding: utf-8 -*-

from math import sqrt


n = int(input('Digite um número para verificar se ele é primo: '))
while(n<=0):
	n = int(input('Digite um número para verificar se ele é primo: '))

primo = True

if (n != 2) and (n % 2 == 0):
	primo = False
	print("Não é um número primo!")
else:
	for i in range(3, int(sqrt(n)) + 1, 2):
		if n % i == 0:
			primo = False
			print('Não é um número primo!')
			break
				
if primo:
	print('É um número primo!') 
