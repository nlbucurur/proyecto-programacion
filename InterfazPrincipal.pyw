# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:17:25 2020

@author: Ronald
"""

from tkinter import *
from metodos import A1Z26, ascii, atbash, bacon, base64, binary, columnar
from metodos import digraph, morse, rot, transposition
lista_met=[A1Z26,ascii,atbash,bacon,base64,binary,columnar,digraph,morse,rot,transposition]
lista_nom=["A1Z26","Ascii","Atbash","Bacon","Base64","Binary","Columnar","Digraph","Morse","Rot","Transposition"]

root=Tk()
root.title("Proyecto programación | Encriptado y Desencriptado") #Nombre que aparece en la ventana
root.iconbitmap("img\VCypher.ico")  #Permite elegir el icono de la esquina superior izquierda
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

#------------Lista que almacena IntVar()----------

ve1=IntVar()
ve2=IntVar()
ve1.set(1)
VarEntera=[ve1,ve2]

#------------------Funcion que ejecuta la funcion de cifrado o descifrado-------------



#---------------Funcion que abre una nueva ventana donde se cifra y descifra un mensaje--------------------



def VentanaCifrado(): 
    
    def CypherOrDecypher():
        
        if ve1.get()==1:
            men_cif=textoCom1.get("1.0",'end-1c') #el -1c es para eliminar un \n extra que toma el .get()
            textoCom2.delete("1.0","end")
            textoCom2.insert("1.0",lista_met[metodoElegido.get()-1].cifrar(men_cif))
            
        else:
            men_decif=textoCom1.get("1.0",'end-1c')
            
            #Text no tiene método .set por lo que se usará
            #.delete para borrar el contenido del cuadro
            #y luego se utilizará .insert para poner el mensaje
            textoCom2.delete(1.0,"end")
            textoCom2.insert(1.0,lista_met[metodoElegido.get()-1].descifrar(men_decif))
    
    if metodoElegido.get()==0:
        messagebox.showinfo("Seleccionar","Por favor seleccione un método de cifrado")
        
    else:
        
        #Configuracion básica que tendrán todas las ventanas de cifrado
        # Objeto de la clase Toplevel y se usa como otra ventana
        croot = Toplevel(root)  
        croot.iconbitmap("img\VCypher.ico")
        croot.title((lista_nom[metodoElegido.get()-1])+" cypher") 
        
        if metodoElegido.get()<12:
            
            croot.config(bg="#D6DBDF")
            #Tamaño de la nueva ventana
            croot.geometry("1000x600")
            #-----------------Frames----------------
            frameI1=Frame(croot,width=500,height=200)
            frameI1.config(bg="light blue",width=500,height=200)
            frameI1.grid(row=0,column=0,columnspan=3)
            
            frameIText1=Frame(croot,width=200,height=300)
            frameIText1.config(bg="red")
            frameIText1.grid(row=1,column=0)
            
            frameIText2=Frame(croot,width=200,height=300)
            frameIText2.config(bg="green")
            frameIText2.grid(row=1,column=2)
            
            frameButton=Frame(croot)
            frameButton.grid(row=2,column=0,columnspan=3)
            
            #----------------Cuadros de texto----------------
            Label(frameI1,text="       Por favor elige una de las opciones           ").grid(row=0,column=0,columnspan=2)
            
            textoCom1=Text(frameIText1,width=40,height=10)
            textoCom1.grid(row=1,column=0,padx=10,pady=10)

            textoCom2=Text(frameIText2,width=40,height=10)
            textoCom2.grid(row=1,column=0,padx=10,pady=10)
            
            #-------------Barras de scroll------------
            
            #Para agregar una barra de scrollbar al texto
            scrollTexto1=Scrollbar(frameIText1,command=textoCom1.yview)
            #.yview es para la vista vertical
            scrollTexto1.grid(row=1,column=1,sticky="nsew")
            #Con sticky="nscw" se adapta al tamaño del widgeth al que pertenece
            textoCom1.config(yscrollcommand=scrollTexto1.set)
            
            scrollTexto2=Scrollbar(frameIText2,command=textoCom2.yview)
            scrollTexto2.grid(row=1,column=1,sticky="nsew")
            textoCom2.config(yscrollcommand=scrollTexto2.set)
            
            #----------------Radiobuttons-----------
            
            RbC=Radiobutton(frameI1,text="Cifrar",variable=ve1,value=1)
            RbC.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC")
            RbC.grid(row=1,column=0)

            RbD=Radiobutton(frameI1,text="Descifrar",variable=ve1,value=2)
            RbD.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");
            RbD.grid(row=1,column=1)
            
            
            
            #-------------Button---------------
            
            botonCorD=Button(frameButton,text="Ejecutar",command=CypherOrDecypher)
            botonCorD.config(cursor="hand2")
            botonCorD.pack()
        else:
            print("Cifrado con Imagenes")
        
        





#------------Botón para llamar un método de cifrado----------------------


boton_metodo=Button(root,text="Listo",command=VentanaCifrado)
boton_metodo.config(cursor="hand2")
boton_metodo.pack()#grid(row=7,column=1)


root.mainloop()