# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:17:25 2020

@author: Ronald
"""

from tkinter import *
from metodos import A1Z26, ascii, atbash, bacon, base64, binary, columnar
from metodos import digraph, morse, rot, transposition
import InterfacesSecundarias
lista_met=[A1Z26,ascii,atbash,bacon,base64,binary,columnar,digraph,morse,rot,transposition]
lista_nom=["A1Z26","Ascii","Atbash","Bacon","Base64","Binary","Columnar","Digraph"
           ,"Morse","Rot","Transposition","Braille"]

root=Tk()
root.title("Proyecto programación | Encriptado y Desencriptado") #Nombre que aparece en la ventana
#root.iconbitmap("img\VCypher.ico")  #Permite elegir el icono de la esquina superior izquierda
root.resizable(0,0)
root.geometry("500x360") #Tamaño por defecto de la ventana principal

root.config(bg="#D0ECE7",bd="15",relief="groove") #Color de fondo, tamaño del borde y 
#tipo de borde de la raíz de la interfaz respectivamente
frame1=Frame()
frame1.config(bg="#F6DDCC",width="450",
              height="450")
frame1.pack()
#frame1.grid(row=0,column=5,columnspan=1)
#Texto inicial
Label(frame1,text="          Por favor elige el método de encriptado          ").grid(row=0,column=0,columnspan=3) 


#-------------radiobuttons---------------

metodoElegido=IntVar()

R1=Radiobutton(frame1,text="A1Z26",variable=metodoElegido,value=1)
R1.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R1.grid(row=1,column=0)

R2=Radiobutton(frame1,text="Ascii",variable=metodoElegido,value=2)
R2.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R2.grid(row=2,column=0)

R3=Radiobutton(frame1,text="Atbash",variable=metodoElegido,value=3)
R3.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R3.grid(row=3,column=0)

R4=Radiobutton(frame1,text="Bacon",variable=metodoElegido,value=4)
R4.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R4.grid(row=4,column=0)

R5=Radiobutton(frame1,text="Base64",variable=metodoElegido,value=5)
R5.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R5.grid(row=5,column=0)

R6=Radiobutton(frame1,text="Binary",variable=metodoElegido,value=6)
R6.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R6.grid(row=6,column=0)

R7=Radiobutton(frame1,text="Columnar",variable=metodoElegido,value=7)
R7.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R7.grid(row=1,column=2)

R8=Radiobutton(frame1,text="Digraph",variable=metodoElegido,value=8)
R8.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R8.grid(row=2,column=2)

R9=Radiobutton(frame1,text="Morse",variable=metodoElegido,value=9)
R9.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R9.grid(row=3,column=2)

R10=Radiobutton(frame1,text="Rot",variable=metodoElegido,value=10)
R10.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R10.grid(row=4,column=2)

R11=Radiobutton(frame1,text="Transposition",variable=metodoElegido,value=11)
R11.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R11.grid(row=5,column=2)

R11=Radiobutton(frame1,text="Braille",variable=metodoElegido,value=12)
R11.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R11.grid(row=6,column=2)

#------------Lista que almacena IntVar()----------

ve1=IntVar()
ve2=IntVar()
ve1.set(1)
VarEntera=[ve1,ve2]


#------------Botón para llamar un método de cifrado----------------------


boton_metodo=Button(root,text="Listo",command=lambda:InterfacesSecundarias.VentanaCifrado(root,
                                        metodoElegido,lista_met,lista_nom,ve1,ve2))
boton_metodo.config(cursor="hand2")
boton_metodo.pack()#grid(row=7,column=1)


root.mainloop()