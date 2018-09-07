# -*- coding: UTF-8 -*-

def run(cadena):
	cadena.split()
	respuesta = False
	for letra in cadena:
		i = 0
		for letra2 in cadena:
			if letra == letra2:
				i += 1
		if i == 1:
			print("La letra {} se encuentra una sola vez".format(letra))
			respuesta = True
			break
	if respuesta == False:
		print("Ninguna letra se encuentra una sola vez.")
	

if __name__ == '__main__':
	cadena = str(input("Ingresa una cadena de texto"))
	run(cadena)




