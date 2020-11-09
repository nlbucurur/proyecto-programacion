

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

        elif opcion == 'd':
            mensaje = str(input('Ingresa la oracion que deseas descifrar: '))
            mensaje_descifrado = descifrar(mensaje)
            print(mensaje_descifrado)

        elif opcion == 's':
            print('¡Gracias por jugar, vuelve pronto!')
            break

        else:
            print('No has seleccionado ninguna opción valida. Ejecuta el programa nuevamente.')
            break

if __name__ == '__main__':
    run()
    
    
    