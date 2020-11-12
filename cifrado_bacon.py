KEYS = {
    'a': 'AAAAA',
    'b': 'AAAAB',
    'c': 'AAABA',
    'd': 'AAABB',
    'e': 'AABAA',
    'f': 'AABAB',
    'g': 'AABBA',
    'h': 'AABBB',
    'i': 'ABAAA',
    'j': 'ABAAB',
    'k': 'ABABA',
    'l': 'ABABB',
    'm': 'ABBAA',
    'n': 'ABBAB',
    'o': 'ABBBA',
    'p': 'ABBBB',
    'q': 'BAAAA',
    'r': 'BAAAB',
    's': 'BAABA',
    't': 'BAABB',
    'u': 'BABAA',
    'v': 'BABAB',
    'w': 'BABBA',
    'x': 'BABBB',
    'y': 'BBAAA',
    'z': 'BBAAB',
}

def cifrar(mensaje):
    palabras = mensaje.split(' ')
    mensaje_cifrado = []

    for palabra in palabras:
        palabra_cifrada = ''
        for letra in palabra:
            palabra_cifrada = palabra_cifrada + KEYS[letra] + ' '
        mensaje_cifrado.append(palabra_cifrada)

    return ' '.join(mensaje_cifrado)


def descifrar_letras(mensaje):
    palabras = mensaje.split(' ')
    mensaje_descifrado = []
    palabra_descifrada = ''
    for palabra in palabras:
        for key, value in KEYS.items():
            if value == palabra:
                palabra_descifrada = palabra_descifrada + key + ' '
    mensaje_descifrado.append(palabra_descifrada)
    return ' '.join(mensaje_descifrado)

def run():

    while True:

        opcion = str(input('''Bienvenido al cifrador por sustitución de Francis Bacons. Te avisamos que este programa funciona con la segunda versión del alfabeto creado para este métodod e cifrado. ¿Qué deseas hacer? Pulsa la tecla correspondiente:

            [c]ifrar
            [d]escifrar
            [s]alir

            '''))
        
        if opcion == 'c':
            mensaje = str(input('Ingresa el mensaje que deseas cifrar: '))
            mensaje_cifrado = cifrar(mensaje.lower())
            print(mensaje_cifrado)

        elif opcion == 'd':
            mensaje = str(input('Ingresa la oracion que deseas descifrar (Ten en cuenta que esta debe estar ingresada letra por letra en mayúsculas): '))
            mensaje_descifrado = descifrar_letras(mensaje)
            print(mensaje_descifrado)

        elif opcion == 's':
            print('¡Gracias por jugar, vuelve pronto!')
            break

        else:
            print('No has seleccionado ninguna opción valida. Ejecuta el programa nuevamente.')
            break

if __name__ == '__main__':
    run()
