# -*- coding: utf-8 -*-

def run():
	palabra = str(input("Dame una palabra: "))
	mayuscula = palabra.upper()
	mayuscula = mayuscula.replace(" ","")


	if mayuscula == mayuscula[::-1]:
		print("{} es un palindromo!".format(palabra))

	else:
		print("{} NO es un palindromo!".format(palabra))


if __name__ == "__main__":
	run()