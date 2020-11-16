import math

def cifrado(llave, mensaje):
    texto_cifrado = [''] * llave

    for col in range(llave):
        punto = col
        while punto < len(mensaje):
            texto_cifrado[col] += mensaje[punto]
            punto += llave
    return ''.join(texto_cifrado)

def descifrado(llave, mensaje):

    num_de_columnas = math.ceil(len(mensaje) / llave)
    num_de_filas = llave

    num_de_vacios = (num_de_columnas * num_de_filas) - len(mensaje)
    texto = [''] * num_de_columnas

    col = 0
    row = 0

    for letra in mensaje:

        texto[col] += letra
        col += 1
        if (col == num_de_columnas) or (col == num_de_columnas - 1 and row >= num_de_filas - num_de_vacios):
            col = 0
            row += 1
    return ''.join(texto)
