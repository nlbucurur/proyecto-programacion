def cifrar(mensaje):
    mensaje_cifrado = []
    for a in mensaje:
        b=a
        b=str(ord(b))
        mensaje_cifrado.append(b)
    return ' '.join(mensaje_cifrado)


def descifrar(mensaje):
    crip = mensaje.split()

    mensaje_descifrado = chr(int(crip[0]))
    l=len(crip); i=1
    while i<l:
        b=chr(int(crip[i]))
        mensaje_descifrado=mensaje_descifrado+b
        #mensaje_descifrado.append(b)
        i+=1

    return mensaje_descifrado
