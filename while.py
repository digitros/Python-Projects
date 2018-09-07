# -*- coding: utf-8 -*-
import random
import factorial

def run():
	try:
		number_found = False
		numeronio = int(input("Entre cuantos numeros quieres adivinar? "))
		random_number = random.randint(0,numeronio)

		while not number_found: 
			number = int(input("intenta un número "))

			if number == random_number:
				print("Felicidades. Encontraste el número")
				number_found = True

			elif number > random_number:
				print("El número es más pequeño")

			else:
				print("El número es más grande")	
	except: 
		print("Ocurrio un error, intenta de nuevo")	

	else: 
		print("Proceso exitoso")

	finally:
		print("Jijiji")


if __name__ == "__main__":
	run()