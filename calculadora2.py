# -*- coding: UTF-8 -*-

resumencito = {}

def solicitar():
	numero = []
	veces = int(input("¿Cuántos numeros quieres operar?\n"))
	for i in range(veces):
		numero.append(float(input("Dame un número: ")))
	return numero

def resumir():
	for llave, valor in resumencito.items():
		print("{}: {}".format(llave, valor))
	return "_____________"
	
def agregar_dic(llave, valor):
	if llave not in resumencito:
		valor = [valor]
		resumencito[llave] = valor
	elif llave in resumencito:
		res = resumencito.get(llave)
		res.append(valor)
		resumencito[llave] = res

def sumar():
	numero = solicitar()
	suma = 0

	for num in numero:
		suma = suma + num

	agregar_dic("Sumas", suma)
	return suma

def restar():
	numero = solicitar()
	resta = numero[0]*2

	for num in numero:
		resta = resta - num

	agregar_dic("Restas", resta)
	return resta

def multiplicar():
	numero = solicitar()
	mult = 1

	for num in numero:
		mult = mult * num

	agregar_dic("Multiplicaciones", mult)
	return mult

def dividir():
	numero = solicitar()
	div = 1

	for num in numero:
		if num == numero[0]:
			div = num
		else:
			div = div / num

	agregar_dic("Divisiones", div)
	return div

def menu():
	while True:
		print("__________________________________________")
		print("Bienvenido a la Calculadora")
		print("¿Qué quieres calcular?")
		opcion = int(input("1 - Sumar\n2 - Restar\n3 - Multiplicar\n4 - Dividir\n5 - Resumen\n"))
		print("__________________________________________")

		if opcion == 1:
			resultado = sumar()
		elif opcion == 2:
			resultado = restar()
		elif opcion == 3:
			resultado = multiplicar()
		elif opcion == 4:
			resultado = dividir()
		elif opcion == 5:
			resultado = resumir()
		else:
			print("opción incorrecta")

		print(resultado)

		print("__________________________________________")
		opcion = int(input("¿Quieres regresar al menú?\n1 - Sí\n2 - No\n"))

		if opcion == 2:
			break

if __name__ == '__main__':
	menu()