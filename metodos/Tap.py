# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 17:28:34 2020

@author: S
"""

def cifrar(mensaje):
    
    letrasy = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    letrasx = "AFLQVBGMRWCHNSXDIOTYEKPUZ"        
    mensaje_cifrado = []
    mensaje1 = mensaje.split()
    mensaje2 = ''.join(mensaje1)
    mensaje_upper = list(mensaje2.upper())
    acifrar = []

    for i in range(0, len(mensaje_upper)):
        
        if mensaje_upper[i] == "J":
            acifrar.append("I")
        else:
            acifrar.append(mensaje_upper[i])
            
            
    for letra in acifrar:
           

           indice1 = (1 + letrasy.index(letra)) / 5
           if indice1 <= 1:
               a = "1"
           elif indice1 > 1 and indice1 <= 2:
               a = "2"
           elif indice1 > 2 and indice1 <= 3:
               a = "3"
           elif indice1 > 3 and indice1 <= 4:
               a = "4"
           elif indice1 > 4 and indice1 <= 5:
               a = "5"              
           
           indice2 = (1 + letrasx.index(letra)) / 5
           if indice2 <= 1:
               b = "1"
           elif indice2 > 1 and indice2 <= 2:
               b = "2"
           elif indice2 > 2 and indice2 <= 3:
               b = "3"
           elif indice2 > 3 and indice2 <= 4:
               b = "4"
           elif indice2 > 4 and indice2 <= 5:
               b = "5"      
               
           mensaje_cifrado.append(a+b)
            
           
    return ' '.join(mensaje_cifrado)
