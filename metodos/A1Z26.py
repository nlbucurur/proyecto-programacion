cif_dic = {"A": "1", "B": "2", "C": "3", "D": "4", "E": "5",
           "F": "6", "G": "7", "H": "8", "I": "9", "J": "10",
           "K": "11", "L": "12", "M": "13", "N": "14", "O": "15",
           "P": "16", "Q": "17", "R": "18", "S": "19", "T": "20",
           "U": "21", "V": "22", "W": "23", "X": "24", "Y": "25",
           "Z": "26"}

descif_dic = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "E",
              "6": "F", "7": "G", "8": "H", "9": "I", "10": "J",
              "11": "K", "12": "L", "13": "M", "14": "N", "15": "O",
              "16": "P", "17": "Q", "18": "R", "19": "S", "20": "T",
              "21": "U", "22": "V", "23": "W", "24": "X", "25": "Y",
              "26": "Z"}


def cifrar(mensaje):
    mensaje = mensaje.upper()
    mensaje_cifrado = ""

    first_w = True
    for palabra in mensaje.split():
        if not first_w:
            mensaje_cifrado += " "
        else:
            first_w = False

        first_l = True
        for letra in palabra:
            if not first_l:
                mensaje_cifrado += "-"
            else:
                first_l = False

            mensaje_cifrado += cif_dic[letra]
    return mensaje_cifrado


def descifrar(mensaje):
    mensaje_descifrado = ""

    first_w = True
    for palabra in mensaje.split():
        if not first_w:
            mensaje_descifrado += " "
        else:
            first_w = False

        for letra in palabra.split("-"):
            mensaje_descifrado += descif_dic[letra]

    return mensaje_descifrado
