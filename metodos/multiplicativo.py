
def cifrar(mensaje, llave=7):
    mensaje_cifrado = ""
    mensaje_en_txt_plano = mensaje.strip()
    mensaje_en_txt_plano = mensaje_en_txt_plano.upper()
    k = llave
    try:
        for i in mensaje_en_txt_plano.split():
            for j in i:
                total = (((ord(j) - 65) * k) % 26)
                mensaje_cifrado = mensaje_cifrado + (chr(total + 65))
            mensaje_cifrado = mensaje_cifrado + " "
    except:
        print("Algo salió mal")
    return mensaje_cifrado

def descifrar(mensaje, llave=7):
    mensaje_en_txt_plano = ""
    mensaje_cifrado = mensaje.strip()
    mensaje_cifrado = mensaje_cifrado.upper()
    k = inverso(llave)

    try:
        if True:
            for i in mensaje_cifrado.split():
                for j in i:
                    total = (((ord(j) - 65) * k) % 26)
                    mensaje_en_txt_plano = mensaje_en_txt_plano + (chr(total + 65))
                mensaje_en_txt_plano = mensaje_en_txt_plano + " "
            print("El mensaje sin cifrar es: ", mensaje_en_txt_plano.upper())
    except:
        print("Algo salió mal")
    return mensaje_en_txt_plano

def inverso(llave):
    a = llave
    a = a % 26
    for x in range(1, 26):
        if (a * x) % 26 == 1:
            return x
    return 1
