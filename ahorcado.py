# -*- coding: utf-8 -*-
import random

#Interfaz del ahorcado:
IMAGES = ["""

    +---+
    |   |
        |
        |
        |
        |
        ========""", """

    +---+
    |   |
    0   |
        |
        |
        |
        ========""", """

    +---+
    |   |
    0   |
    |   |
        |
        |
        ========""", """

    +---+
    |   |
    0   |
   /|   |
        |
        |
        ========""", """

    +---+
    |   |
    0   |
   /|\  |
        |
        |
        ========""", """

    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
        ========""", """

    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
        ========"""]

#Palabras para seleccionar una al azar:
WORDS = [
	"lavadora",
	"secadora",
	"sofa",
	"gobierno",
	"diputado",
	"democracia",
	"computadora",
	"teclado"]


#Verifica si el usuario ha ganado:
def win_verify(hidden_word, tries, word):
	try:
		hidden_word.index("-")
	except ValueError:
		display_board(hidden_word, tries)
		print("")
		print("¡Felicidades! Ganaste. La palabra es: {}".format(word))
		seguir = False


#Genera una palabra al azar:
def random_word():
	idx = random.randint(0, len(WORDS) - 1)
	return WORDS[idx]

#Genera la interfaz de ahorcado:
def display_board(hidden_word, tries):
	print(IMAGES[tries])
	print("")
	print(hidden_word)
	print("--- * --- * --- * --- * --- * ---")

def run():
	word = random_word()
	hidden_word = ["-"] * len(word)
	tries = 0
	pasadas = []


	while seguir == True:
		display_board(hidden_word, tries)
		current_letter = str(input("Escoge una letra: "))
		repetida = False

		#verifica si la letra ingresada ya ha sido usada:
		for i in range(len(pasadas)):
			if current_letter == pasadas[i]:
				repetida = True
				print("Esa letra ya había sido usada")
				break

		if repetida == True:
			continue

		#Confirmar si el usuario escribió la palabra correcta en un intento:
		if current_letter.upper() == word.upper():
			print("Felicidades, la palabra es: {}".format(word))
			break

		#confirmar si el usuario escribió más de una letra:
		if len(current_letter) > 1:
			print("Esta es más de una letra")
			continue
		else:
			pasadas.append(current_letter) #Si es sólo una letra, entonces añadirla a una lista de letras ya usadas


		#Verifica que la letra escrita se encuentre dentro de la palabra generada al azar, sino, usa un intento:
		letter_indexes = []
		for idx in range(len(word)):
			if word[idx].upper() == current_letter.upper():
				letter_indexes.append(idx)

		if len(letter_indexes) == 0:
			tries += 1

			if tries == 6:
				display_board(hidden_word, tries)
				print("")
				print("¡Perdiste! La palabra correcta era: {}".format(word))
				break

		else:
			for idx in letter_indexes:
				hidden_word[idx] = current_letter

			letter_indexes = []

		#Verifica si el usuario a completado la palabra:
		win_verify(hidden_word, tries, word)



if __name__ == "__main__":
	seguir = True	
	print("B I E N V E N I D O S  A  A H O R C A D O S")
	run()


