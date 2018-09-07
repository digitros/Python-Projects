USUARIO = "Digitros"
nombre = "Diego"
apellido = "Valdez Acosta"
CONTRASENA = "12345678"
saldo = 10000
ditos = 0

def consulta():
	print("Tu saldo actual en pesos es: ${}".format(saldo))
	print("Tu saldo actual en puntos es: ${}".format(ditos))
	return validation(int(input("¿Quieres regresar al menú anterior?\n1.-Sí\n2.-No\n")))

def deposito():
	def efectivo():
		global saldo
		print("Tu saldo actual es de: ${}".format(saldo))
		nuevo = int(input("¿Cuanto deseas depositar?\n"))
		
		if nuevo >= 0:
			print("Tu nuevo saldo será de ${}.".format(saldo+nuevo))
			ans = int(input("¿Quieres realizar la operación?\n1.-Sí\n2.-No\n"))
			if ans == 1:

				saldo += nuevo
				print("Tu saldo es de: ${}\n".format(saldo))
			else:
				print("Tu saldo es de: ${}\n".format(saldo))
		else:
			print("Numero invalido.")
		
		return validation(int(input("¿Quieres regresar al menú anterior?\n1.-Sí\n2.-No\n")))

	def puntoTransfer():
		global saldo, ditos
		x = True
		while x == True:
			print("Tienes ${} pesos de saldo y ${} en puntos.".format(saldo, ditos))
			a = int(input("¿Qué acción deseas realizar?\n1.-Transferir puntos a saldo.\n2.-Salir\n"))
			if a == 1:
				b = int(input("¿Cuantos puntos deseas transferir?"))
				if (b <= ditos) and (b <= 0):
					saldo += ditos
					ditos -= b
					print("Tu nuevo saldo es de: ${}".format(saldo))
					print("Tu nuevo saldo de puntos es de: ${}".format(ditos))
					x = False
				elif b < ditos:
					print("No tienes los suficientes puntos para eso.")
					x = True
				else:
					print("Numero incorrecto.")
					x = True
			elif a == 2:
				x = False
		return validation(int(input("¿Quieres regresar al menú anterior?\n1.-Sí\n2.-No\n")))

	a = int(input("¿Qué acción deseas realizar?\n1.-Deposito efectivo\n2.-Transferencia de puntos a saldo\n3.-Regresar al menú anterior\n4.-Salir\n"))
	if a == 1:
		return efectivo()
	if a == 2:
		return puntoTransfer()
	if a == 3:
		print("")
		return True
	if a == 4:
		print("")
		return False
	else:
		print("Opción incorrecta, finalizando sesión.\n")
		return False

def retiro():
	global saldo
	print("Tu saldo actual es de: ${}".format(saldo))
	nuevo = int(input("¿Cuanto deseas retirar?\n"))
	if (nuevo <= saldo) and (nuevo > 0):
		print("Tu nuevo saldo será de ${}.".format(saldo-nuevo))
		ans = int(input("¿Quieres realizar la operación?\n1.-Sí\n2.-No\n"))
		if ans == 1:
			saldo -= nuevo
			print("Tu saldo es de: ${}\n".format(saldo))
		else:
			print("Tu saldo es de: ${}\n".format(saldo))
	elif nuevo > saldo:
		print("El numero a retirar es mayor al saldo disponible.")
	else:
		print("Numero menor a cero.")
	return validation(int(input("¿Quieres regresar al menú anterior?\n1.-Sí\n2.-No\n")))

def compra():
	global saldo, ditos
	print("Tu saldo actual es de: ${}".format(saldo))
	producto = input("¿Qué deseas comprar?\n")
	precio = int(input("¿Cuál es el precio?\n"))
	if (precio <= saldo) and (precio > 0):
		print("Tu nuevo saldo será de ${}.".format(saldo-precio))
		ans = int(input("¿Quieres realizar la operación?\n1.-Sí\n2.-No\n"))
		if ans == 1:
			saldo -= precio
			ditos += precio * .02
			print("Tu saldo es de: ${}\n".format(saldo))
			print("Tu saldo de puntos es de: ${}".format(ditos))
		else:
			print("Tu saldo es de: ${}\n".format(saldo))
	elif precio > saldo:
		print("El numero a gastar es mayor al saldo disponible.")
	else:
		print("Numero menor a cero.")
	print("Disfruta tu {}.".format(producto))
	return validation(int(input("¿Quieres regresar al menú anterior?\n1.-Sí\n2.-No\n")))

def validation(validar):
	if validar == 1:
		print("")
		return True
	elif validar == 2:
		print("")
		return False
	else:
		print("Opción incorrecta, finalizando sesión.\n")
		return False

def menu():
	
	correcto = True
	while correcto:
		print("BIENVENIDO A TU BANCA EN LINEA")
		print("")
		print("Hola {}, ¿Qué deseas hacer hoy?".format(nombre))
		opcion = int(input("1.-Consulta \n2.-Deposito\n3.-Retiro\n4.-Compra\n5.-Salir\n"))
		if opcion == 1:
			correcto = consulta()
		elif opcion == 2:
			correcto = deposito()
		elif opcion == 3:
			correcto = retiro()
		elif opcion == 4:
			correcto = compra()
		elif opcion == 5:
			break
		else:
			print("No es una opción correcta, intenta de nuevo.")


if __name__ == '__main__':
	print("BIENVENIDO A DIGIBANK")
	userkey = True
	passkey = True
	while userkey == True:
		user = input("Ingrese su usuario: ")
		if user != USUARIO:
			print("Este usuario no existe, intente de nuevo.")
		elif user == USUARIO:
			userkey = False
			while passkey == True:
				password = input("Ingrese su contraseña: ")
				if password != CONTRASENA:
					print("Esta contraseña es incorrecta, intente de nuevo.")
				elif password == CONTRASENA:
					print("")
					print("Conección correcta\n")
					passkey = False
					menu()


	
	
	
