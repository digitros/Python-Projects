
"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def first_not_repeating_char(char_sequence):
    seen_letters = {}

    for idx, letter in enumerate(char_sequence): #enumerate sustituye a range(len()) guarda iterador en idx y elemento en letter
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

    final_letters = []
    for llave, valor in seen_letters.items():
        if valor[1] == 1:
            final_letters.append( (llave, valor[0]) )
            print(llave, valor[0])


    not_repeated_letters = sorted(final_letters, key=lambda valores: valor[0])
    print(type(not_repeated_letters))

    if not_repeated_letters:
        return not_repeated_letters[0][0] #retorna el indice 0 de la tupla contenida en el indice 0 de la lista.
    else:
        return '_'


if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))

        #mimamamema




