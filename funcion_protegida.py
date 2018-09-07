# -*- coding: utf-8 -*-

def protected(protected_func):

	def wrapper(password):

		if password == "Platzi":
			protected_func()
		else:
			print("Contraseña incorrecta")
	return wrapper


@protected
def protected_func():
	print("Tu contraseña es correcta.")


if __name__ == '__main__':
	password = str(input("Ingresa tu contraseña: "))

	protected_func(password)