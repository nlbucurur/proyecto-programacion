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