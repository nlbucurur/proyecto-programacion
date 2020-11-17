# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:17:25 2020

@author: 57322
"""

from tkinter import *
from metodos import A1Z26, ascii, atbash, bacon, base64, binary, columnar
from metodos import digraph, morse, rot, transposition


root=Tk()
root.title("Proyecto programación | Encriptado y Desencriptado")
root.iconbitmap("img\VCypher.ico")

root.geometry("640x420")

root.config(bg="#D0ECE7",bd="15",relief="groove")
#Texto inicial

Label(root,text="Por favor elige el método de encriptación").pack()
#-------------radiobuttons---------------

metodoElegido=IntVar()

R1=Radiobutton(root,text="A1Z26",variable=metodoElegido,value=1)
R1.config(cursor="hand2");R1.pack()

R2=Radiobutton(root,text="Ascii",variable=metodoElegido,value=2)
R2.config(cursor="hand2");R2.pack()

R3=Radiobutton(root,text="Atbash",variable=metodoElegido,value=3)
R3.config(cursor="hand2");R3.pack()

R4=Radiobutton(root,text="Bacon",variable=metodoElegido,value=4)
R4.config(cursor="hand2");R4.pack()

R5=Radiobutton(root,text="Base64",variable=metodoElegido,value=5)
R5.config(cursor="hand2");R5.pack()

R6=Radiobutton(root,text="Binary",variable=metodoElegido,value=6)
R6.config(cursor="hand2");R6.pack()

R7=Radiobutton(root,text="Columnar",variable=metodoElegido,value=7)
R7.config(cursor="hand2");R7.pack()

R8=Radiobutton(root,text="Digraph",variable=metodoElegido,value=8)
R8.config(cursor="hand2");R8.pack()

R9=Radiobutton(root,text="Morse",variable=metodoElegido,value=9)
R9.config(cursor="hand2")
R9.pack()

R10=Radiobutton(root,text="Rot",variable=metodoElegido,value=10)
R10.config(cursor="hand2")
R10.pack()

R11=Radiobutton(root,text="Transposition",variable=metodoElegido,value=11)
R11.config(cursor="hand2")
R11.pack()

#------------Botón+Funcion de llamado----------------------

def abrirMetodo():
    if metodoElegido.get()!=0:   #Si no se elige ninguna de las opciones metodoElegido.get() retorna 0
        InterfazCTexto                         #por lo que al elegir
        print("adios")
        
    print("hola")
    if metodoElegido.get()==1:
        print("x")


boton_metodo=Button(root,text="Listo",command=abrirMetodo)
boton_metodo.pack()


root.mainloop()