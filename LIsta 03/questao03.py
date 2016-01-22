# -*- coding: utf-8 -*- 

hab_a = 80000
hab_b = 200000

cont = 0
while hab_a <= hab_b:
	cres_a = hab_a * 3 / 100
	cres_b = hab_b * 1.5 / 100
	
	hab_a += cres_a
	hab_b += cres_b
	
	cont += 1
	#print ("%d -- %3.2f %3.2f"%(cont, hab_a, hab_b))
	
print ("São necessários %d anos para que A ultrapasse B" %cont)