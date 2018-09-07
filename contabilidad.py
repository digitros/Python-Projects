# -*- coding: UTF-8 -*-
catalogo = {}

def main():
	ventas = int(input("¿Cuántas ventas deseas agregar?"))
	total = 0
	for venta in range(ventas):
		producto = str(input("Nombre de producto {}: ".format(venta+1)))
		valor = int(input("\nValor de {}: ".format(producto)))
		total += valor

		catalogo[producto] = valor
	iva = total*0.16

	opcion = int(input("¿Deseas generar un archivo? 1-Sí o 2-No: "))

	if opcion == 1:
		with open("contabilidad.txt", "w") as f:
			f.write('Contabilidad de ventas\n')
			f.write('Producto/Precio\n')

			for llave, valor in catalogo.items():
				f.write("{}: ${}\n".format(llave, valor))

			f.write("\nTotal: {}\n".format(total))
			f.write("\nIva total: {}".format(iva))
		print("Archivo creado")
	else:
		print("Adiós")

if __name__ == '__main__':
	main()