# -*- coding: utf-8 -*- 

def fib (num):
	if (num < 2):
		return 1
	else:
		return fib (num - 1) + fib (num - 2)


num = int(input("Informe o primeiro lado: "))
print ("O número de Fibonacci para %d é %d" %(num, fib(num)))