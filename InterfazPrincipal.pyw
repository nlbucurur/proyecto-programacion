# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:17:25 2020

@author: Ronald
"""

from tkinter import *
from tkinter import messagebox
import InterfacesSecundarias
           
          #--------------Transformacion
lista_nom=["A1Z26","Ascii","Atbash","Bacon","Base64",
           "Binary","Digraph","Keyboard code","Morse","Tap",
          #--------------Clave
          "Columnar","Multiplicativo","Playfair","Rot","Transposition","Vigenere",
          #--------------Imagen
           "Braille","Dorabella","Rosicrucian"]

root=Tk()
root.title("Proyecto programación | Encriptado y Desencriptado") #Nombre que aparece en la ventana
root.iconbitmap("img\VCypher.ico")  #Permite elegir el icono de la esquina superior izquierda
root.resizable(0,0)
root.geometry("600x400") #Tamaño por defecto de la ventana principal

root.config(bg="#26C6DA",bd="15",relief="groove") #Color de fondo, tamaño del borde y 
#tipo de borde de la raíz de la interfaz respectivamente
frame1=Frame()
frame1.config(bg="#D0ECE7",width="450",
              height="450")
#Me gusta #26C6DA
#D0ECE7
frame1.pack()
#frame1.grid(row=0,column=5,columnspan=1)
#Texto inicial
l1=Label(frame1,text="                             Por favor elige el método de encriptado segun la preferencia                             ")
l1.grid(row=0,column=0,columnspan=5) 
l1.config(bg="gray")
Label(frame1,text="                                                                    Transformacion                                                                    ").grid(
    row=1,column=0,columnspan=5)
Label(frame1,text="                                                     Métodos que requieren una llave                                                     ").grid(
    row=4,column=0,columnspan=5)
Label(frame1,text="                                           Métodos que involucran el uso de símbolos                                            ").grid(
    row=7,column=0,columnspan=5)


#-------------Menu----------------------------------------------
def infoAdicional():
    messagebox.showinfo("Barra superior","Cuadro interior")
def avisoAdvertencia():
    messagebox.showwarning("Barra superior","error x")
def Terminar():
    valor=messagebox.askquestion("Salir","Desea salir de la aplicación?")
    if valor=="yes":
        root.destroy()
#Con messagebox.askquestion("a","b") aparece "si" o "no"
#Con .askokcancel aparece "ok" o "cancel" pero esto
#retorna 1 o 0 respectivamente
#.askretrycancel retorna 1 o 0 (True or False)

#Con filedialog se buscará codificar o descodificar documentos

barraMenu=Menu(root)
root.config(menu=barraMenu)
#Con root.config parametro menu construye el menu

archivoMenu=Menu(barraMenu, tearoff=0)
#Con tearoff=0 desaparece el separador de la pestaña de una opcion
archivoMenu.add_command(label="Op1",command=infoAdicional)
archivoMenu.add_command(label="Op2",command=avisoAdvertencia)
archivoMenu.add_command(label="Op3")

#Separador
archivoMenu.add_separator()

archivoMenu.add_command(label="Salir",command=Terminar)
#con esto especificamos que el menu la opcion
#archivo perteneza a otro menu
archivoEdicion=Menu(barraMenu)
archivoHerramientas=Menu(barraMenu)
archivoAyuda=Menu(barraMenu)

barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
#Primer parametro, texto que va a tener el primer elemento del menu
#Segundo parametro que elemento alberga este archivo
barraMenu.add_cascade(label="Edicion",menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)

#-------------radiobuttons---------------------------------------------------

metodoElegido=IntVar()

#---------Transformaciones

R_A1Z26=Radiobutton(frame1,text="A1Z26",variable=metodoElegido,value=1)
R_A1Z26.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_A1Z26.grid(row=2,column=0)

R_Ascii=Radiobutton(frame1,text="Ascii",variable=metodoElegido,value=2)
R_Ascii.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Ascii.grid(row=2,column=1)

R_Atbash=Radiobutton(frame1,text="Atbash",variable=metodoElegido,value=3)
R_Atbash.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Atbash.grid(row=2,column=2)

R_Bacon=Radiobutton(frame1,text="Bacon",variable=metodoElegido,value=4)
R_Bacon.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Bacon.grid(row=2,column=3)

R_Base64=Radiobutton(frame1,text="Base64",variable=metodoElegido,value=5)
R_Base64.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Base64.grid(row=2,column=4)

R_Binary=Radiobutton(frame1,text="Binary",variable=metodoElegido,value=6)
R_Binary.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Binary.grid(row=3,column=0)

R_Digraph=Radiobutton(frame1,text="Digraph",variable=metodoElegido,value=7)
R_Digraph.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Digraph.grid(row=3,column=1)

R_Keyboard=Radiobutton(frame1,text="Keyboard",variable=metodoElegido,value=8)
R_Keyboard.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Keyboard.grid(row=3,column=2)

R_Morse=Radiobutton(frame1,text="Morse",variable=metodoElegido,value=9)
R_Morse.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Morse.grid(row=3,column=3)

R_Tap=Radiobutton(frame1,text="Tap",variable=metodoElegido,value=10)
R_Tap.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Tap.grid(row=3,column=4)

#----------Clave

R_Columnar=Radiobutton(frame1,text="Columnar",variable=metodoElegido,value=11)
R_Columnar.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Columnar.grid(row=5,column=0)

R_Multiplicativo=Radiobutton(frame1,text="Multiplicativo",variable=metodoElegido,value=12)
R_Multiplicativo.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Multiplicativo.grid(row=5,column=2)

R_Playfair=Radiobutton(frame1,text="Playfair",variable=metodoElegido,value=13)
R_Playfair.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Playfair.grid(row=5,column=4)


R_Rot=Radiobutton(frame1,text="   Rot   ",variable=metodoElegido,value=14)
R_Rot.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Rot.grid(row=6,column=0)

R_Transposition=Radiobutton(frame1,text="Transposition",variable=metodoElegido,value=15)
R_Transposition.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Transposition.grid(row=6,column=2)

R_Vigerene=Radiobutton(frame1,text="Vigenere",variable=metodoElegido,value=16)
R_Vigerene.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Vigerene.grid(row=6,column=4)

#-------------Imagenes

R_Braille=Radiobutton(frame1,text="Braille",variable=metodoElegido,value=17)
R_Braille.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Braille.grid(row=8,column=0)

R_Dorabella=Radiobutton(frame1,text="Dorabella",variable=metodoElegido,value=18)
R_Dorabella.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Dorabella.grid(row=8,column=2)

R_Rosicrucian=Radiobutton(frame1,text="Rosicrucian",variable=metodoElegido,value=19)
R_Rosicrucian.config(cursor="hand2",padx=10,pady=10,bg="#D0ECE7");R_Rosicrucian.grid(row=8,column=4)

#------------Lista que almacena IntVar()----------

ve1=IntVar()
ve2=IntVar()
ve1.set(1)

VarEntera=[ve1,ve2]

#------------Lista de imagenes para método Braille

ImageA=PhotoImage(file="img\Braille\A.png")    
ImageB=PhotoImage(file="img\Braille\B.png")  
ImageC=PhotoImage(file="img\Braille\C.png")   
ImageD=PhotoImage(file="img\Braille\D.png")   
ImageE=PhotoImage(file="img\Braille\E.png")   
ImageF=PhotoImage(file="img\Braille\F.png")   
ImageG=PhotoImage(file="img\Braille\G.png")   
ImageH=PhotoImage(file="img\Braille\H.png")   
ImageI=PhotoImage(file="img\Braille\I.png")   
ImageJ=PhotoImage(file="img\Braille\J.png")   
ImageK=PhotoImage(file="img\Braille\K.png")   
ImageL=PhotoImage(file="img\Braille\L.png")   
ImageM=PhotoImage(file="img\Braille\M.png")   
ImageN=PhotoImage(file="img\Braille\M_N.png")   
ImageO=PhotoImage(file="img\Braille\O.png")   
ImageP=PhotoImage(file="img\Braille\P.png")   
ImageQ=PhotoImage(file="img\Braille\Q.png")  
ImageR=PhotoImage(file="img\Braille\R.png")   
ImageS=PhotoImage(file="img\Braille\S.png")   
ImageT=PhotoImage(file="img\Braille\T.png")   
ImageU=PhotoImage(file="img\Braille\T_U.png")   
ImageV=PhotoImage(file="img\Braille\V.png")   
ImageW=PhotoImage(file="img\Braille\W.png")   
ImageX=PhotoImage(file="img\Braille\X.png")
ImageY=PhotoImage(file="img\Braille\Y.png")   
ImageZ=PhotoImage(file="img\Braille\Z.png")
img_list=[ImageA,ImageB,ImageC,ImageD,ImageE,ImageF,ImageG,
          ImageH,ImageI,ImageJ,ImageK,ImageL,ImageM,ImageN,
          ImageO,ImageP,ImageQ,ImageR,ImageS,ImageT,ImageU,
          ImageV,ImageW,ImageX,ImageY,ImageZ]


#------------Lista de imagenes para método Dorabella
ImageA1=PhotoImage(file="img\Dorabella\A.png")    
ImageB1=PhotoImage(file="img\Dorabella\B.png")  
ImageC1=PhotoImage(file="img\Dorabella\C.png")   
ImageD1=PhotoImage(file="img\Dorabella\D.png")   
ImageE1=PhotoImage(file="img\Dorabella\E.png")   
ImageF1=PhotoImage(file="img\Dorabella\F.png")   
ImageG1=PhotoImage(file="img\Dorabella\G.png")   
ImageH1=PhotoImage(file="img\Dorabella\H.png")   
ImageI_J1=PhotoImage(file="img\Dorabella\I_J.png")    
ImageK1=PhotoImage(file="img\Dorabella\K.png")  
ImageL1=PhotoImage(file="img\Dorabella\L.png")   
ImageM1=PhotoImage(file="img\Dorabella\M.png")   
ImageN1=PhotoImage(file="img\Dorabella\mN.png")   
ImageO1=PhotoImage(file="img\Dorabella\O.png")   
ImageP1=PhotoImage(file="img\Dorabella\P.png")   
ImageQ1=PhotoImage(file="img\Dorabella\Q.png")
ImageR1=PhotoImage(file="img\Dorabella\R.png")    
ImageS1=PhotoImage(file="img\Dorabella\S.png")  
ImageT1=PhotoImage(file="img\Dorabella\T.png")   
ImageU_V1=PhotoImage(file="img\Dorabella\V_U.png")   
ImageW1=PhotoImage(file="img\Dorabella\W.png")   
ImageX1=PhotoImage(file="img\Dorabella\X.png")   
ImageY1=PhotoImage(file="img\Dorabella\Y.png")   
ImageZ1=PhotoImage(file="img\Dorabella\Z.png")
img_list1=[ImageA1,ImageB1,ImageC1,ImageD1,ImageE1,ImageF1,ImageG1,
          ImageH1,ImageI_J1,ImageK1,ImageL1,ImageM1,ImageN1,
          ImageO1,ImageP1,ImageQ1,ImageR1,ImageS1,ImageT1,ImageU_V1,
          ImageW1,ImageX1,ImageY1,ImageZ1]  

#--------Lista de imagenes para método Rosicrucian

ImageA2=PhotoImage(file="img\Rosicrucian\A.png").subsample(10)
ImageB2=PhotoImage(file="img\Rosicrucian\B.png").subsample(10)
ImageC2=PhotoImage(file="img\Rosicrucian\C.png").subsample(10)
ImageD2=PhotoImage(file="img\Rosicrucian\D.png").subsample(10)
ImageE2=PhotoImage(file="img\Rosicrucian\E.png").subsample(10)
ImageF2=PhotoImage(file="img\Rosicrucian\F.png").subsample(10)
ImageG2=PhotoImage(file="img\Rosicrucian\G.png").subsample(10)
ImageH2=PhotoImage(file="img\Rosicrucian\H.png").subsample(10)
ImageI2=PhotoImage(file="img\Rosicrucian\I.png").subsample(10)
ImageJ2=PhotoImage(file="img\Rosicrucian\J.png").subsample(10)
ImageK2=PhotoImage(file="img\Rosicrucian\K.png").subsample(10)
ImageL2=PhotoImage(file="img\Rosicrucian\L.png").subsample(10)
ImageM2=PhotoImage(file="img\Rosicrucian\M.png").subsample(10)
ImageN2=PhotoImage(file="img\Rosicrucian\M_N.png").subsample(10)
ImageO2=PhotoImage(file="img\Rosicrucian\O.png").subsample(10)
ImageP2=PhotoImage(file="img\Rosicrucian\P.png").subsample(10)
ImageQ2=PhotoImage(file="img\Rosicrucian\Q.png").subsample(10)
ImageR2=PhotoImage(file="img\Rosicrucian\R.png").subsample(10)
ImageS2=PhotoImage(file="img\Rosicrucian\S.png").subsample(10)
ImageT2=PhotoImage(file="img\Rosicrucian\T.png").subsample(10)
ImageU2=PhotoImage(file="img\Rosicrucian\T_U.png").subsample(10)
ImageV2=PhotoImage(file="img\Rosicrucian\V.png").subsample(10)
ImageW2=PhotoImage(file="img\Rosicrucian\W.png").subsample(10)
ImageX2=PhotoImage(file="img\Rosicrucian\X.png").subsample(10)
ImageY2=PhotoImage(file="img\Rosicrucian\Y.png").subsample(10)
ImageZ2=PhotoImage(file="img\Rosicrucian\Z.png").subsample(10)
img_list2=[ImageA2,ImageB2,ImageC2,ImageD2,ImageE2,ImageF2,ImageG2,
          ImageH2,ImageI2,ImageJ2,ImageK2,ImageL2,ImageM2,ImageN2,
          ImageO2,ImageP2,ImageQ2,ImageR2,ImageS2,ImageT2,ImageU2,
          ImageV2,ImageW2,ImageX2,ImageY2,ImageZ2]

#------------Botón para llamar un método de cifrado----------------------


boton_metodo=Button(root,text="Listo",command=lambda:InterfacesSecundarias.VentanaCifrado(root,
                                        metodoElegido,lista_nom,ve1,ve2,img_list,img_list1,img_list2))
boton_metodo.config(cursor="hand2",height=2,width=10)
boton_metodo.pack()#grid(row=7,column=1)


root.mainloop()
