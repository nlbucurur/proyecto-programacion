# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 16:39:18 2020

@author: S
"""

def cifrar_bin(mensaje):
    MAYUSCULA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minuscula = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    simbolos = '!"#$%&´()*+,-./'
    palabras = mensaje.split(" ")
    print(palabras)
    mensaje_cifrado = []
    

    for palabra in palabras:

        palabra_cifrada = " "
        for letra in palabra:

            if letra in MAYUSCULA:
                palabra_cifrada = "010" + bin(MAYUSCULA.index(letra)+1)[2:].zfill(5)
            elif letra in minuscula:
                palabra_cifrada = "011" + bin(minuscula.index(letra)+1)[2:].zfill(5)
            elif letra in numeros:
                palabra_cifrada = "0011" + bin(numeros.index(letra)+1)[2:].zfill(4)
            elif letra in simbolos:
                palabra_cifrada = "0010" + bin(simbolos.index(letra)+1)[2:].zfill(4)
            else:
                palabra_cifrada = "[caracter no definido]"
            mensaje_cifrado.append(palabra_cifrada) 
        
        if len(palabras) > 1:
           mensaje_cifrado.append("00100000")  


    return ' '.join(mensaje_cifrado)


def cifrar_base64(mensaje):
  TABLA = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  binario = cifrar_bin(mensaje)
  cadena_1 = "".join(binario.split(" "))
  bits_6 = []
  mensaje_cifrado=[]
  
  for index in range(0,len(cadena_1), 6):    
     bits_6.append(cadena_1[index: index+6])
  
  
  for letra in bits_6:
    
     index = list(letra)
     
     while len(index) < 6:
        index.append("0")
    
     index_64 = int(str("".join(index)), 2)
     mensaje_cifrado.append(TABLA[index_64])      
        
         
  for i in range(0, len(bits_6)):

               
     if 2*i == len(bits_6):
        a = "=="
     elif 3*i ==len(bits_6):
        a = "="   

  mensaje_cifrado.append(a)         
        
  return "".join(mensaje_cifrado), print(bits_6)
