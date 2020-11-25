# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 18:10:23 2020

@author: S
"""

#-----------> Se genera la tabla de Vigenere


def cifrar(mensaje, clave):
    
    mensaje_cifrado = []
    mensaje1 = mensaje.split()
    mensaje2 = ''.join(mensaje1)
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mensaje_upper = list(mensaje2.upper())
    clave_upper = list(clave.upper())

    index = 0
    
    while len(clave_upper) != len(mensaje_upper):
        clave_upper.append(clave_upper[index])
        index = index + 1
    

    for i in range(0, len(clave_upper)):
        tabla_vigenere =[]

        tabla_vigenere.append(alfabeto[alfabeto.index(clave_upper[i]):]+alfabeto[:alfabeto.index(clave_upper[i])])
        buscar = list(tabla_vigenere)
        fila = list(buscar[0])
        letra_cifrada = fila[alfabeto.index(mensaje_upper[i])]
        mensaje_cifrado.append(letra_cifrada)
     
    return ''.join(mensaje_cifrado)


def descifrar(mensaje, clave):
    mensaje_descifrado = []
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mensaje_upper = list(mensaje.upper())
    clave_upper = list(clave.upper())

    index = 0
    while len(clave_upper) != len(mensaje_upper):
            clave_upper.append(clave_upper[index])
            index = index + 1


    for i in range(0, len(clave_upper)):
        tabla_vigenere =[]
    
        tabla_vigenere.append(alfabeto[alfabeto.index(clave_upper[i]):]+alfabeto[:alfabeto.index(clave_upper[-i])])
        buscar = list(tabla_vigenere)
        fila = list(buscar[0])
        letra_descifrada = alfabeto[fila.index(mensaje_upper[i])]
        mensaje_descifrado.append(letra_descifrada)
     
    return ''.join(mensaje_descifrado)  
    
    
    