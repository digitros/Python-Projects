# -*- coding: UTF-8 -*-

countries = {
	"mexico": 122,
	"colombia": 49,
	"argentina": 43,
	"chile": 12,
	"peru": 31
}


def main():
	while True:
		country = str(input("Escribe el nombre de un país: ")).lower()
		try:
			print("La población de {} es: {} millones".format(country, countries[country]))
		except KeyError:
			print("No tenemos el dato de la población de: {}".format(country))
		else:
			pass
		finally:
			pass
		

if __name__ == '__main__':
	main()