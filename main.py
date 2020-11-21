from metodos import A1Z26, ascii, atbash, bacon, base64, binary, columnar, multiplicativo
from metodos import digraph, morse, rot, transposition

print("Bienvenido al cifrador")


def show_help():
    print("""
Acude al read me para encontrar información del cifrado y decifrado de textos
usando diferentes métodos:

https://github.com/nlbucurur/proyecto-programacion/blob/master/README.md
""")


def comando_invalido():
    print("""
No has seleccionado ninguna opción valida.
""")


def quit():
    exit(0)


methods = {"A": A1Z26, "as": ascii, "at": atbash, "bac": bacon, "bas": base64,
           "bi": binary, "c": columnar, "d": digraph, "m": morse, "r": rot,
           "t": transposition,"mul": multiplicativo, "s": quit, "ay": show_help}


def run():

    while True:

        metodo = input("""
¿Qué método deseas usar hoy?

[A]1Z26 \t [as]cii \t [at]bash
[bac]on \t [bas]e64 \t [bi]nary
[c]olumnar \t [d]igraph \t [m]orse
[r]ot \t [mul]tiplicativo\t [t]ransposition 

[ay]uda \t [s]alir

>>> """).strip()

        if metodo in ["ay", "s"]:
            methods[metodo]()
            continue
        elif metodo in methods.keys():
            metodo = methods[metodo]
        else:
            comando_invalido()
            continue

        opcion = input("""
¿Qué deseas hacer?

[c]ifrar
[d]escifrar
[v]olver
[s]alir

>>> """).strip()

        if opcion == 'c':
            mensaje = input('Ingresa el mensaje que deseas cifrar: ').strip()
            mensaje_cifrado = metodo.cifrar(mensaje)
            print(f"""
Este es el mensaje cifrado:

{mensaje_cifrado}
""")

        elif opcion == 'd':
            mensaje = input('Ingresa la oracion que deseas descifrar: ').strip()
            mensaje_descifrado = metodo.descifrar(mensaje)
            print(f"""
Este es el mensaje descifrado:

{mensaje_descifrado}
""")

        elif opcion == 'v':
            continue

        elif opcion == 's':
            print('¡Gracias, vuelve pronto!')
            break

        else:
            comando_invalido()
            continue

if __name__ == '__main__':
    run()
