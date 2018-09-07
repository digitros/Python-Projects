# -*- coding: UTF-8 -*-

def materias():
	calificaciones = {}
	promedio = 0

	for i in range(5):
		materia = input("Ingresa una materia: ")
		calificacion = float(input("Ingresa su calificación: "))
		calificaciones[materia] = calificacion

	for calificacion in calificaciones.values():
		promedio += calificacion

	for materia, calificacion in calificaciones.items():
		print("{}: {}".format(materia, calificacion))

	print("Promedio: {}".format(promedio/len(calificaciones.values())))

if __name__ == '__main__':
	materias()



























































































































	