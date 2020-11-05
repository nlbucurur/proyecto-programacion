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



def descifrar_bin(mensaje):
    MAYUSCULA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minuscula = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    simbolos = '!"#$%&´()*+,-./'
    letras = mensaje.split(" ")
    mensaje_desifrado=[]
    for letra in letras:
         if letra != "00100000":
             sub_letra = list(letra)
             if sub_letra[1] == "1":
                 
                  if sub_letra[2] == "0":
                      bin_index = sub_letra[3:len(letra)]
                      index = "".join(bin_index)
                      mensaje_desifrado.append(MAYUSCULA[int(str(index),2 )-1])
                  elif sub_letra[2] == "1":
                      bin_index = sub_letra[3:len(letra)]
                      index = "".join(bin_index)
                      mensaje_desifrado.append(minuscula[int(str(index),2 )-1])

                  
                  
             if sub_letra[1] == "0":
                 
                  if sub_letra[3] == "0":
                      bin_index = sub_letra[4:len(letra)]
                      index = "".join(bin_index)
                      mensaje_desifrado.append(simbolos[int(str(index),2 )-1])
                  elif sub_letra[3] == "1":
                      bin_index = sub_letra[4:len(letra)]
                      index = "".join(bin_index)
                      mensaje_desifrado.append(numeros[int(str(index),2 )-1])


         if letra == "00100000":
             mensaje_desifrado.append(" ")

    return ''.join(mensaje_desifrado)


def run():

    while True:

        opcion = str(input('''Bienvenido al cifrador binario. ¿Qué deseas hacer? Pulsa la tecla correspondiente:

            [c]ifrar
            [d]escifrar
            [s]alir

            '''))

        if opcion == 'c':
            mensaje = str(input('Ingresa el mensaje que deseas cifrar: '))
            mensaje_cifrado = cifrar_bin(mensaje)
            print(mensaje_cifrado)

        elif opcion == 'd':
            mensaje = str(input('Ingresa la oracion que deseas descifrar: '))
            mensaje_descifrado = descifrar_bin(mensaje)
            print(mensaje_descifrado)

        elif opcion == 's':
            print('¡Gracias por jugar, vuelve pronto!')
            break

        else:
            print('No has seleccionado ninguna opción valida. Ejecuta el programa nuevamente.')
            break

if __name__ == '__main__':
    run()
