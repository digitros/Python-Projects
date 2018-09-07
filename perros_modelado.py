# -*- coding: utf-8 -*-

class DogLife:
	_DOG = ['''

					 ____   ____   ____   ____
		( )         |    | |    | |    | |    |
	  ( . . )       |____| |    | |    | |____|
	 (   u   )      |      |    | |    | |
	(_________)     |      |____| |____| |

	''',
	'''
								   _    _
				   \     / |    | | \  / |
	   oooooo       \___/  |    | |  \/  |
	 oooooooooo       |    |    | |      |
	|__________|      |    |____| |      |

	''',
	'''                    
		. . .       ______   ____
	 .         .       |    |    | \     /
	.     *     .      |    |    |  \___/
	.   ** **   .      |    |    |    |
	 .   * *   .   |___|    |____|    |
		. . . 

	''',
	'''
						 ____   ____   ____
	  *~~~~~*    |    | |    | |    | |    | \     /
	( ) . . ( )  |____| |____| |____| |____|  \___/
	( )  v  ( )  |    | |    | |      |         |
	( )  u  ( )  |    | |    | |      |         |

	''',
	'''
				  ____   ____   ___
	  *~~~~~*    |      |    | |   \
	( ) . . ( )  |____  |____| |    \
	( )  v  ( )       | |    | |    /
	( )  n  ( )   ____| |    | |___/

	''',
	'''
				  ___    ____  ____   ___
	  *~~~~~*    |   \  |     |    | |   \
	( ) x x ( )  |    \ |___  |____| |    \
	( )  v  ( )  |    / |     |    | |    /
	( )  .  ( )  |___/  |____ |    | |___/

	''',
	'''

			 z   z
			   z  ____        ____  ____  ____
	  *~~~~~*    |     |     |     |     |    |
	( ) . . ( )  |___  |     |___  |___  |____|
	( )  v  ( )      | |     |     |     |
	( )  -  ( )  ____| |____ |____ |____ |


	''',
	'''
			 . . .
			_|_|_|_                  ____   ___
		 __|~ ~ ~ ~|__       |    | |    \ |   \
		|             |      |____| |  __/ |    \
	 __ |~ ~ ~ ~ ~ ~ ~|___   |    | |    \ |    /
	|                     |  |    | |____/ |___/
	|_____________________|  

	''',
	'''

	 _____________________________
	|__\__\__\__\__\__\__\__\__\__| 1O

	''',
	'''

	 __________________________
	|__\__\__\__\__\__\__\__\__| 9

	''',
	'''

	 _______________________
	|__\__\__\__\__\__\__\__| 8

	''',
	'''

	 ____________________
	|__\__\__\__\__\__\__| 7

	''',
	'''

	 _________________
	|__\__\__\__\__\__| 6

	''',
	'''

	 ______________
	|__\__\__\__\__| 5

	''',
	'''

	 ___________
	|__\__\__\__| 4

	''',
	'''

	 ________
	|__\__\__| 3

	''',
	'''

	 _____
	|__\__| 2

	''',
	'''

	 __
	|__| 1


	''']

	def __init__(self):
		self._popis = 10
		self._comida = 10
		self._sueño = 10
		self._diversion = 10
		self._vivo = True
		self._feliz= True
		self._edad = 0

	def vida(self):
		if self._comida == 10:
			print ('COMER {}'.format(self._DOG[8]))
		elif self._comida == 9:
			print ('COMER {}'.format(self._DOG[9]))
		elif self._comida == 8:
			print ('COMER {}'.format(self._DOG[10]))
		elif self._comida == 7:
			print ('COMER {}'.format(self._DOG[11]))
		elif self._comida == 6:
			print ('COMER {}'.format(self._DOG[12]))
		elif self._comida == 5:
			print ('COMER {}'.format(self._DOG[13]))
		elif self._comida == 4:
			print ('COMER {}'.format(self._DOG[14]))
		elif self._comida == 3:
			print ('COMER {}'.format(self._DOG[15]))
		elif self._comida == 2:
			print ('COMER {}'.format(self._DOG[16]))
		elif self._comida == 1:
			print ('COMER {}'.format(self._DOG[17]))

		if self._sueño == 10:
			print ('DORMIR {}'.format(self._DOG[8]))
		elif self._sueño == 9:
			print ('DORMIR {}'.format(self._DOG[9]))
		elif self._sueño == 8:
			print ('DORMIR {}'.format(self._DOG[10]))
		elif self._sueño == 7:
			print ('DORMIR {}'.format(self._DOG[11]))
		elif self._sueño == 6:
			print ('DORMIR {}'.format(self._DOG[12]))
		elif self._sueño == 5:
			print ('DORMIR {}'.format(self._DOG[13]))
		elif self._sueño == 4:
			print ('DORMIR {}'.format(self._DOG[14]))
		elif self._sueño == 3:
			print ('DORMIR {}'.format(self._DOG[15]))
		elif self._sueño == 2:
			print ('DORMIR {}'.format(self._DOG[16]))
		elif self._sueño == 1:
			print ('DORMIR {}'.format(self._DOG[17]))

		if self._popis == 10:
			print ('BAÑO {}'.format(self._DOG[8]))
		elif self._popis == 9:
			print ('BAÑO {}'.format(self._DOG[9]))
		elif self._popis == 8:
			print ('BAÑO {}'.format(self._DOG[10]))
		elif self._popis == 7:
			print ('BAÑO {}'.format(self._DOG[11]))
		elif self._popis == 6:
			print ('BAÑO {}'.format(self._DOG[12]))
		elif self._popis == 5:
			print ('BAÑO {}'.format(self._DOG[13]))
		elif self._popis == 4:
			print ('BAÑO {}'.format(self._DOG[14]))
		elif self._popis == 3:
			print ('BAÑO {}'.format(self._DOG[15]))
		elif self._popis == 2:
			print ('BAÑO {}'.format(self._DOG[16]))
		elif self._popis == 1:
			print ('BAÑO {}'.format(self._DOG[17]))

		if self._diversion == 10:
			print ('JUGAR {}'.format(self._DOG[8]))
		elif self._diversion == 9:
			print ('JUGAR {}'.format(self._DOG[9]))
		elif self._diversion == 8:
			print ('JUGAR {}'.format(self._DOG[10]))
		elif self._diversion == 7:
			print ('JUGAR {}'.format(self._DOG[11]))
		elif self._diversion == 6:
			print ('JUGAR {}'.format(self._DOG[12]))
		elif self._diversion == 5:
			print ('JUGAR {}'.format(self._DOG[13]))
		elif self._diversion == 4:
			print ('JUGAR {}'.format(self._DOG[14]))
		elif self._diversion == 3:
			print ('JUGAR {}'.format(self._DOG[15]))
		elif self._diversion == 2:
			print ('JUGAR {}'.format(self._DOG[16]))
		elif self._diversion == 1:
			print ('JUGAR {}'.format(self._DOG[17]))


	def comer(self):
		print(self._DOG[1])

		if self._comida <= 8:
			self._comida += 3
		elif self._comida == 8:
			self._comida += 2
		elif self._comida == 9:
			self._comida +=1
		else:
			self._comida = 10

		if self._popis ==2:
			self._popis -=2
		elif self._popis == 1:
			self._popis -=1
		elif self._popis <= 10 and self._popis > 2:
			self._popis -= 2

		if self._diversion == 1:
			self._diversion -= 1
		elif self._diversion <= 10 and self._diversion >= 2:
			self._diversion -= 1

		if self._sueño == 1:
			self._sueño -= 1
		elif self._sueño <= 10 and self._sueño >= 2:
			self._sueño -= 1


		self._mood()

	def dormir(self):
		print(self._DOG[6])

		self._sueño = 10

		if self._comida ==2:
			self._comida -=2
		elif self._comida == 1:
			self._comida -=1
		elif self._comida <= 10 and self._comida > 2:
			self._comida -= 2

		if self._popis ==2:
			self._popis -=2
		elif self._popis == 1:
			self._popis -=1
		elif self._popis <= 10 and self._popis > 2:
			self._popis -= 2

		if self._diversion == 1:
			self._diversion -= 1
		elif self._diversion <= 10 and self._diversion >= 2:
			self._diversion -= 1

		self._mood()

	def defecar(self):
		print(self._DOG[0])

		if self._popis <= 8:
			self._popis += 3
		elif self._popis == 8:
			self._popis += 2
		elif self._popis == 9:
			self._popis +=1
		else:
			self._popis = 10 

		if self._comida ==2:
			self._comida -=2
		elif self._comida == 1:
			self._comida -=1
		elif self._comida <= 10 and self._comida > 2:
			self._comida -= 2

		if self._diversion == 1:
			self._diversion -= 1
		elif self._diversion <= 10 and self._diversion >= 2:
			self._diversion -= 1

		if self._sueño == 1:
			self._sueño -= 1
		elif self._sueño <= 10 and self._sueño >= 2:
			self._sueño -= 1

		self._mood()

	def jugar(self):
		print(self._DOG[2])

		if self._diversion >= 5:
			self._diversion = 10
		else:
			self ._diversion += 5

		if self._comida ==3:
			self._comida -=3
		elif self._comida ==2:
			self._comida -=2
		elif self._comida == 1:
			self._comida -=1
		elif self._comida <= 10 and self._comida > 3:
			self._comida -= 3

		if self._sueño == 1:
			self._sueño -= 1
		elif self._sueño <= 10 and self._sueño >= 2:
			self._sueño -= 1

		if self._popis == 1:
			self._popis -= 1
		elif self._popis <= 10 and self._popis >= 2:
			self._popis -= 1

		self._mood()

	def _mood (self):
		if (self._popis == 0) or (self._sueño == 0) or (self._diversion == 0) or (self._comida == 0) :
			self._vivo = False
			self._dead()

		if (self._popis <= 5 and self._popis > 0) or (self._sueño <= 5 and self._sueño > 0) or (self._diversion <= 5 and self._diversion > 0) or (self._comida <= 5 and self._comida > 0):
			self._feliz = False
			self._happiness()

		if self._feliz == True:
			if (self._popis >=8) or (self._comida >=8) or (self._sueño >=8) or (self._diversion >=8):
				self._feliz = True
				self._happiness()
			 
	def _dead(self):
		if self._vivo == False:
			print(self._DOG[5])
			return False
			

	def _happiness(self):
		if self._feliz == True:
			print(self._DOG[3])
		else:
			print(self._DOG[4])

	def _crece(self):
		self._edad += 1

		if self._edad == 10:
			self._dead()
			print('\nTu amigo ha llegado a su edad máxima, pero no estes triste, vivio una vida feliz junto a ti. ')
			print('\n   G A M E   O V E R')
		else:
			self._vivo = True
			print (self._DOG[7])

def run():
	print('B I E N V E N I D O   A   T A M A G O G O    D . S .\n')
	raza = input ('Razas disponibles: \na) Chihuahua \nb) Husky \nc) Pug \nd) Labrador \n \n¿Cuál escogeras?: ')
	name = input('\n¿Cómo llamaras a tu cachorro?: ')
	print ('\n-----------------------------------------------------------------------------------------------------------------------')
	perro = DogLife()

	print ('\n¡Felicidades! Ahora tienes un nuevo amigo \n{} tendrá necesidades como dormir, jugar y alimentarse; así que asegurate de darle atención y cariño\n'.format(name))

 
	acciones = 0

	while True:

		if perro._dead()== False:
			print ('Tu amigo ha muerto')
			print('\n   G A M E   O V E R')
			break

		print ('Calidad de vida de {} \n'.format(name))
		perro.vida()

		print ('\n___________________________________________________________________________________________________________________')
		accion = input ('\nAcciones: \n[C]omer \n[J]ugar \n[D]ormir \n[B]año \n[S]alir' )
		print ('\n___________________________________________________________________________________________________________________')
		accion.lower()
		if accion == 'c':
			acciones +=1
			perro.comer()
		elif accion == 'j':
			acciones +=1
			perro.jugar()
		elif accion == 'd':
			acciones +=1
			perro.dormir()
		elif accion == 'b':
			acciones +=1
			perro.defecar()
		elif accion == 's':
			break
		else:
			print ('\nComando incorrecto, intentalo de nuevo \n')
			continue

		if acciones == 5:
			perro._crece()
			print ('¡Felicidades, {} ha crecido un año más!'.format(name))
			acciones = 0


if __name__ == '__main__':
	run()
