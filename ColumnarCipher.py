def asignar_numero(palabra): #Le asigna un numero a cada letra de la palabra clave en orden alfabético
    letras = "abcdefghijklmnopqrstuvwxyz"
    numero = list(range(len(palabra)))
    x = 0
    for i in range(len(letras)):
        for j in range(len(palabra)):
            if letras[i] == palabra[j]:
                x += 1
                numero[j] = x
    return numero

def ubicacion(palabra, lista_de_numeros): #Toma la ubicacion de los numeros
    posicion = ""
    for i in range(len(palabra)+1):
        for j in range(len(palabra)):
            if lista_de_numeros[j]==i:
                posicion += str(j)
    return posicion

def cifrar(mensaje):
    clave = input("Introduce una palabra clave: ")
    mensaje1 = mensaje.lower()
    numero_asignado = asignar_numero(clave)

    for i in range(len(clave)):
        print((clave[i]).upper(), end=" ")
    print('')







def run():

    while True:

        opcion = str(input('''Bienvenido al cifrador. ¿Qué deseas hacer? Pulsa la tecla correspondiente:

            [c]ifrar
            [d]escifrar
            [s]alir

            '''))

        if opcion == 'c':
            mensaje = str(input('Ingresa el mensaje que deseas cifrar: '))
            mensaje_cifrado = cifrar(mensaje)
            print(mensaje_cifrado)

        """elif opcion == 'd':
            mensaje = str(input('Ingresa la oracion que deseas descifrar: '))
            mensaje_descifrado = descifrar(mensaje)
            print(mensaje_descifrado)"""

        if opcion == 's':
            print('¡Gracias por jugar, vuelve pronto!')
            break

        else:
            print('No has seleccionado ninguna opción valida. Ejecuta el programa nuevamente.')
            break

if __name__ == '__main__':
    run()