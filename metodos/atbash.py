KEYS = {
    'a': 'z',
    'b': 'y',
    'c': 'x',
    'd': 'w',
    'e': 'v',
    'f': 'u',
    'g': 't',
    'h': 's',
    'i': 'r',
    'j': 'q',
    'k': 'p',
    'l': 'o',
    'm': 'n',
    'n': 'm',
    'o': 'l',
    'p': 'k',
    'q': 'j',
    'r': 'i',
    's': 'h',
    't': 'g',
    'u': 'f',
    'v': 'e',
    'w': 'd',
    'x': 'c',
    'y': 'b',
    'z': 'a',
    'A': 'Z',
    'B': 'Y',
    'C': 'X',
    'D': 'W',
    'E': 'V',
    'F': 'U',
    'G': 'T',
    'H': 'S',
    'I': 'R',
    'J': 'Q',
    'K': 'P',
    'L': 'O',
    'M': 'N',
    'N': 'M',
    'O': 'L',
    'P': 'K',
    'Q': 'J',
    'R': 'I',
    'S': 'H',
    'T': 'G',
    'U': 'F',
    'V': 'E',
    'W': 'D',
    'X': 'C',
    'Y': 'B',
    'Z': 'A',

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
