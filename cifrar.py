KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

def cifrar(mensaje):
    palabras = mensaje.split(' ')
    mensaje_cifrado = []

    for palabra in palabras:
        palabra_cifrada = ''
        for letra in palabra:
            palabra_cifrada += KEYS[letra]
        mensaje_cifrado.append(palabra_cifrada)

    return ' '.join(mensaje_cifrado)


def descifrar(mensaje):
    palabras = mensaje.split(' ')
    mensaje_descifrado = []

    for palabra in palabras:
        palabra_descifrada = ''
        for letra in palabra:
            for key, value in KEYS.items():
                if value == letra:
                    palabra_descifrada += key
        mensaje_descifrado.append(palabra_descifrada)
    return ' '.join(mensaje_descifrado)

def run():

    while True:

        opcion = str(input('''Bienvenido al cifrador. ¿Qué deseas hacer? Pulsa la tecla correspondiente:

            [c]ifrar
            [d]escifrar
            [s]alir

            '''))

        if opcion == 'c':
            mensaje = str(input('Ingresa el mensaje que deseas cifrar: '))
            mensaje_cifrado = cifrar(mensaje)
            print(mensaje_cifrado)

        elif opcion == 'd':
            mensaje = str(input('Ingresa la oracion que deseas descifrar: '))
            mensaje_descifrado = descifrar(mensaje)
            print(mensaje_descifrado)

        elif opcion == 's':
            print('¡Gracias por jugar, vuelve pronto!')
            break

        else:
            print('No has seleccionado ninguna opción valida. Ejecuta el programa nuevamente.')
            break

if __name__ == '__main__':
    run()
