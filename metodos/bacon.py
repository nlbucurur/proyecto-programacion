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
