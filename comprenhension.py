# -*- coding: UTF-8 -*-

def run():
	pares = [num for num in range(1, 31) if num % 2 == 0]
	print("Pares: {}".format(pares))

	cuadrado = {num: num**2 for num in range(1,11)}
	for numero, cuadradin in cuadrado.items():
		print("Cuadrado de {}: {}".format(numero, cuadradin)) 

if __name__ == '__main__':
	run()