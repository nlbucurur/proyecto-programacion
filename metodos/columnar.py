def asignar_numero(palabra): #Le asigna un numero a cada letra de la palabra clave en orden alfabético
    letras = "abcdefghijklmnñopqrstuvwxyz"
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

def cifrar(mensaje1):
    clave = input("Introduce una palabra clave: ")
    mensaje = (mensaje1.replace(" ", "")).lower()
    numero_asignado = asignar_numero(clave)

    for i in range(len(clave)): #Imprime la palabra clave en mayusculas
        print((clave[i]).upper(), end=" ")
    print('')
    for j in range(len(clave)): #Imprime el numero asignado a cada letra debajo de cada una
        print(str(numero_asignado[j]), end=" ")
    print('')
    print('')

    adicionales = len(mensaje) % len(clave) #Mira los caracteres adicionales, en caso de que no ocupen todos los espacios en la matriz
    sobrantes = len(clave) - adicionales
    if adicionales != 0: #A los espacios sobrantes les asigna un guión
        for i in range(sobrantes):
            mensaje+= "-"


    filas = int(len(mensaje)/len(clave)) #Guarda el numero de filas que va a tener la matriz de letras
    matriz = [[0] * len(clave) for i in range(filas)] #Crea la matriz dada por el numero de filas y el número de letras de la palabra clave
    x=0
    for i in range(filas): #Ubica el mensaje dentro de la matriz
        for j in range(len(clave)):
            matriz[i][j] = mensaje[x]
            x += 1

    for i in range(filas): #Imprime la matriz con el mensaje
        for j in range(len(clave)):
            print(matriz[i][j], end=" ")
        print('')

    numero = ubicacion(clave, numero_asignado) #Asigna los puestos en los que deben ser escritas las columnas de la matriz
    #print(numero)

    mensaje_cifrado = ""
    k = 0
    for i in range(len(clave)): #Se convierte el mensaje de la matriz en texto cifrado
        if k != len(clave):
            d = int(numero[k])
        for j in range(filas):
            mensaje_cifrado += matriz[j][d]
        k += 1

    return print(mensaje_cifrado)



def descifrar(mensaje1):
    mensaje = (mensaje1.replace(" ", "")).lower()
    clave = input("Introduce la palabra clave: ").lower()
    numero_asignado = asignar_numero(clave)
    print('')
    filas = int(len(mensaje) / len(clave)) #Encuentra el numero de filas que debe haber en la matriz
    numero = ubicacion(clave, numero_asignado) #Asigna los puestos en los que deben ser escritas las columnas de la matriz
    #print(numero)
    matriz = [[0] * len(clave) for i in range(filas)] #Crea la matriz a partir del numero de letras de la palabra clave y el numero de filas

    mensaje_descifrado = ""
    x=0
    i=0
    for j in range(len(mensaje)):
        m=0
        if x != len(clave):
            m: int = int(numero[x])
        else:
            x=0

        for p in range(filas):
            matriz[p][m] = mensaje[i]
            i += 1
        if i == len(mensaje):
            break
        x += 1

    for i in range(filas):
        for j in range(len(clave)):
            mensaje_descifrado += str(matriz[i][j])

    mensaje_final=mensaje_descifrado.replace("-", "")

    return print("Mensaje descifrado: " + mensaje_final)
