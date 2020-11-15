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

def run():

    while True:

        opcion = str(input('''Bienvenido al cifrador binario. ¿Qué deseas hacer? Pulsa la tecla correspondiente:

            [c]ifrar
            [d]escifrar
            [s]alir

            '''))

        if opcion == 'c':
            mensaje = str(input('Ingresa el mensaje que deseas cifrar: '))
            s = int(input("Ingresa una clave de cifrado (Número de rotación): "))
            mensaje_cifrado = cifrar(mensaje,s)
            print(mensaje_cifrado)

        elif opcion == 'd':
            
                while True:

                        opcion = str(input(''' ¿Conoces la clave de cifrado (Número de rotación))
                
                            [s]i (Debes introducir una clave de cifrado)
                            [n]o (Se realizara un descifrado para las 26 rotaciones posibles)
                            [a]tras
                
                            '''))
            
                        if opcion == 's':
                            mensaje = str(input('Ingresa el mensaje que deseas descifrar: '))
                            s = int(input("Ingresa una clave de cifrado (Número de rotación): "))
                            mensaje_descifrado = descifrar(mensaje,s)
                            print(mensaje_descifrado)
        
                        elif opcion == 'n':
                            mensaje = str(input('Ingresa el mensaje que deseas descifrar: '))
                            mensaje_descifrado = descifrar_todo(mensaje)
                            print(mensaje_descifrado)
        
                        elif opcion == 'a':
                            break
                
                        else:
                            print('No has seleccionado ninguna opción valida. Ejecuta el programa nuevamente.')
                            break
    
        
        
        
        elif opcion == 's':
            print('¡Gracias por jugar, vuelve pronto!')
            break

        else:
            print('No has seleccionado ninguna opción valida. Ejecuta el programa nuevamente.')
            break

if __name__ == '__main__':
    run()