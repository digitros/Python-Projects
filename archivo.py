# -*- coding: utf-8 -*-

import turtle

def main():
	windows = turtle.Screen()
	figura = turtle.Turtle()
	choice = int(input("1.- Triangulo \n2.- Cuadrado "))
	longitud = int(input("Tamaño de linea: "))

	if choice == 1 :
		make_triangle(figura, longitud)

	elif choice == 2 :
		make_square(figura, longitud)

	turtle.mainloop()


def make_triangle(figura, longitud):

	for i in range(3):
		make_line_and_turn(figura, longitud, 120)


def make_square(figura, longitud):
	for i in range(4):
		make_line_and_turn(figura, longitud, 90)


def make_line_and_turn(figura, longitud, grados):
	figura.forward(longitud)
	figura.left(grados)



if __name__ == "__main__":
	main()
