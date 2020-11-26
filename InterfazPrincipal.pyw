# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:17:25 2020

@author: Ronald
"""

from tkinter import *
from tkinter import messagebox
from metodos import A1Z26, ascii, atbash, bacon, base64, binary,braille, columnar
from metodos import digraph, morse,multiplicativo, rot, transposition
import InterfacesSecundarias
#lista_met=[A1Z26,ascii,atbash,bacon,base64,binary,braille,columnar,
           #digraph,morse,multiplicativo,rot,transposition,braille]
lista_nom=["A1Z26","Ascii","Atbash","Bacon","Base64","Binary","Columnar",
           "Digraph","Morse","Multiplicativo","Rot","Tap","Transposition","Vigenere","Braille","Dorabella"]

root=Tk()
root.title("Proyecto programación | Encriptado y Desencriptado") #Nombre que aparece en la ventana
root.iconbitmap("img\VCypher.ico")  #Permite elegir el icono de la esquina superior izquierda
root.resizable(0,0)
root.geometry("500x450") #Tamaño por defecto de la ventana principal

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

R_A1Z26=Radiobutton(frame1,text="A1Z26",variable=metodoElegido,value=1)
R_A1Z26.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R_A1Z26.grid(row=1,column=0)
#pack
R_Ascii=Radiobutton(frame1,text="Ascii",variable=metodoElegido,value=2)
R_Ascii.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R_Ascii.grid(row=2,column=0)

R_Atbash=Radiobutton(frame1,text="Atbash",variable=metodoElegido,value=3)
R_Atbash.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R_Atbash.grid(row=3,column=0)

R_Bacon=Radiobutton(frame1,text="Bacon",variable=metodoElegido,value=4)
R_Bacon.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R_Bacon.grid(row=4,column=0)

R_Base64=Radiobutton(frame1,text="Base64",variable=metodoElegido,value=5)
R_Base64.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R_Base64.grid(row=5,column=0)

R_Binary=Radiobutton(frame1,text="Binary",variable=metodoElegido,value=6)
R_Binary.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R_Binary.grid(row=6,column=0)

R_Braille=Radiobutton(frame1,text="Braille",variable=metodoElegido,value=15)
R_Braille.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R_Braille.grid(row=7,column=0)

R_Columnar=Radiobutton(frame1,text="Columnar",variable=metodoElegido,value=7)
R_Columnar.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R_Columnar.grid(row=8,column=0)

R_Digraph=Radiobutton(frame1,text="Digraph",variable=metodoElegido,value=8)
R_Digraph.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R_Digraph.grid(row=1,column=2)

R_Dorabella=Radiobutton(frame1,text="Dorabella",variable=metodoElegido,value=16)
R_Dorabella.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R_Dorabella.grid(row=2,column=2)

R_Morse=Radiobutton(frame1,text="Morse",variable=metodoElegido,value=9)
R_Morse.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R_Morse.grid(row=3,column=2)

R_Multiplicativo=Radiobutton(frame1,text="Multiplicativo",variable=metodoElegido,value=10)
R_Multiplicativo.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R_Multiplicativo.grid(row=4,column=2)

R_Rot=Radiobutton(frame1,text="Rot",variable=metodoElegido,value=11)
R_Rot.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R_Rot.grid(row=5,column=2)

R_Tap=Radiobutton(frame1,text="Tap",variable=metodoElegido,value=12)
R_Tap.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R_Tap.grid(row=6,column=2)

R_Transposition=Radiobutton(frame1,text="Transposition",variable=metodoElegido,value=13)
R_Transposition.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R_Transposition.grid(row=7,column=2)

R_Vigerene=Radiobutton(frame1,text="Vigenere",variable=metodoElegido,value=14)
R_Vigerene.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");R_Vigerene.grid(row=8,column=2)


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
#------------Botón para llamar un método de cifrado----------------------


boton_metodo=Button(root,text="Listo",command=lambda:InterfacesSecundarias.VentanaCifrado(root,
                                        metodoElegido,lista_nom,ve1,ve2,img_list))
boton_metodo.config(cursor="hand2")
boton_metodo.pack()#grid(row=7,column=1)


root.mainloop()
