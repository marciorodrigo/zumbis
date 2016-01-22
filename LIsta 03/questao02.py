# -*- coding: utf-8 -*- 
import sys


def get_line(string):
	sys.stdout.write(string)
	sys.stdout.flush()
	line = sys.stdin.readline()
	if line:
		return line[:-1]


nome = get_line("Informe o nome do usuário: ")
senha = get_line("Informe a senha: ")

while senha == nome:
	print ("A senha não deve ser igual ao nome do usuário")
	nome = get_line("Informe o nome do usuário: ")
	senha = get_line("Informe a senha: ")

print ("Nome de usuário e senha válidos")