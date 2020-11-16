Morse = { 'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---',
          'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
          'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
          '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..',
          '9':'----.', '0':'-----', ' ':' ',
          ',':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}


def cifrar(mensaje):
    mensaje_cifrado = ''
    for letra in mensaje:
        if letra == ' ':
            mensaje_cifrado += Morse[letra.lower()]
        else:
            mensaje_cifrado += Morse[letra.lower()] + ' '
    return mensaje_cifrado


def descifrar(mensaje):
   mensaje_descifrado = ''
   texto = ''
   for letra in mensaje:
      if letra != ' ' :
         x = 0
         texto += letra
      else:
         x += 1
         if x == 2:
            mensaje_descifrado += ' '
         else:
            mensaje_descifrado += list(Morse.keys())[list(Morse.values()).index(texto)]
            texto = ''
   return mensaje_descifrado
