# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 13:24:26 2020

@author: S
"""

def cifrar(mensaje, s):
    MAYUSCULA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minuscula = "abcdefghijklmnopqrstuvwxyz"
    palabras = mensaje.split(" ")
    mensaje_cifrado = []

    MAYUSCULA_ROT = MAYUSCULA[s:]+MAYUSCULA[:s]
    minuscula_ROT = minuscula[s:]+minuscula[:s]


    for palabra in palabras:
        palabra_cifrada = []
        for letra in palabra:
            if letra in MAYUSCULA:
                palabra_cifrada.append(MAYUSCULA_ROT[MAYUSCULA.index(letra)])

            if letra in minuscula:
                palabra_cifrada.append(minuscula_ROT[minuscula.index(letra)])

            palabra_unida= ''.join(palabra_cifrada)

        mensaje_cifrado.append(palabra_unida)


    return ' '.join(mensaje_cifrado)

def descifrar(mensaje, s):
    MAYUSCULA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minuscula = "abcdefghijklmnopqrstuvwxyz"
    palabras = mensaje.split(" ")
    mensaje_descifrado = []

    s_dec = -1*s
    MAYUSCULA_ROT = MAYUSCULA[s_dec:]+MAYUSCULA[:s_dec]
    minuscula_ROT = minuscula[s_dec:]+minuscula[:s_dec]


    for palabra in palabras:
        palabra_descifrada = []
        for letra in palabra:
            if letra in MAYUSCULA:
                palabra_descifrada.append(MAYUSCULA_ROT[MAYUSCULA.index(letra)])

            if letra in minuscula:
                palabra_descifrada.append(minuscula_ROT[minuscula.index(letra)])

            palabra_unida= ''.join(palabra_descifrada)

        mensaje_descifrado.append(palabra_unida)


    return ' '.join(mensaje_descifrado)


def descifrar_todo(mensaje):
    for s in range(0,27):
        print("Con ", s, " rotaciones, se tiene el mensaje: ", descifrar(mensaje, s))

    return
