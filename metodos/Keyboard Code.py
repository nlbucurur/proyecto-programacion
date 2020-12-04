keyboard = {'a':'q', 'b':'w', 'c':'e', 'd':'r', 'e':'t', 'f':'y', 'g':'u', 'h':'i', 'i':'o', 'j':'p', 'k':'a', 'l':'s',
            'm':'d', 'n':'f', 'o':'g', 'p':'h', 'q':'j', 'r':'k', 's':'l', 't':'z', 'u':'x', 'v':'c', 'w':'v', 'x':'b',
            'y':'n', 'z':'m',
            '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '0':'0', ' ':' ', ',':',',
            '.':'.', '?':'?', '/':'/', '-':'-', '(':'(', ')':')'}


def cifrar(mensaje):
    mensaje_cifrado = ''
    for letra in mensaje:
            mensaje_cifrado += keyboard[letra.lower()]
    return mensaje_cifrado


def descifrar(mensaje):
    palabras = mensaje.split(' ')
    mensaje_descifrado = []

    for palabra in palabras:
        palabra_descifrada = ''
        for letra in palabra:
            for i, j in keyboard.items():
                if j == letra:
                    palabra_descifrada += i
        mensaje_descifrado.append(palabra_descifrada)
    return ' '.join(mensaje_descifrado)

