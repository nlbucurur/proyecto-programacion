# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:27:42 2020

@author: Ronald
"""
from tkinter import *
from metodos import A1Z26, ascii, atbash, bacon, base64, binary, columnar
from metodos import digraph, morse, rot, transposition
lista_met=[A1Z26,ascii,atbash,bacon,base64,binary,columnar,digraph,morse,rot,transposition]
#------------------Funcion que ejecuta la funcion de cifrado o descifrado-------------
def CypherOrDecypher(textoCom1,textoCom2,metodoElegido,ve1):
        

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
            
def CorD_braille(textoCom,LabelImg,metodoElegido,ve1):
        
    if ve1.get()==1:
        men_cif=textoCom.get("1.0",'end-1c') #el -1c es para eliminar un \n extra que toma el .get()
        LabelImg.delete("1.0","end")
        LabelImg.insert("1.0",lista_met[metodoElegido.get()-1].cifrar(men_cif))
            
    else:
        men_decif=textoCom.get("1.0",'end-1c')
            
        #Text no tiene método .set por lo que se usará
        #.delete para borrar el contenido del cuadro
        #y luego se utilizará .insert para poner el mensaje
        LabelImg.delete(1.0,"end")
        LabelImg.insert(1.0,lista_met[metodoElegido.get()-1].descifrar(men_decif))

        
#---------------Funcion que abre una nueva ventana donde se cifra y descifra un mensaje------------



def VentanaCifrado(root,metodoElegido,lista_met,lista_nom,ve1,ve2): 
    
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
            frameI1.config(bg="red",width=500,height=200)
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
            
            botonCorD=Button(frameButton,text="Ejecutar",command=lambda:CypherOrDecypher(textoCom1,textoCom2,metodoElegido,ve1))
            botonCorD.config(cursor="hand2")
            botonCorD.pack()
        #---------------------Caso Braille------------------------
        elif metodoElegido.get()==12:
            
            croot.config(bg="#D6DBDF")
            #Tamaño de la nueva ventana
            croot.geometry("1000x600")
            #-----------------Frames----------------
            frameI1=Frame(croot,width=500,height=200)
            frameI1.config(bg="light blue",width=500,height=200)
            frameI1.grid(row=0,column=0)#,columnspan=3)
            
            frameIText=Frame(croot,width=200,height=300)
            frameIText.config(bg="red")
            frameIText.grid(row=1,column=0)
            
            frameIImg=Frame(croot,width=200,height=300)
            frameIImg.config(bg="green")
            frameIImg.grid(row=2,column=0)
            
            frameButton=Frame(croot)
            frameButton.grid(row=3,column=0)#,columnspan=3)
            
            #----------------Cuadros de texto----------------
            Label(frameI1,text="       Por favor elige una de las opciones           ").grid(row=0,column=0,columnspan=2)
            
            textoCom=Text(frameIText,width=40,height=10)
            textoCom.grid(row=1,column=0,padx=10,pady=10)

            LabelImg=Text(frameIImg,width=40,height=10)
            LabelImg.grid(row=1,column=0,padx=10,pady=10)
            
            #-------------Barras de scroll------------
            
            #Para agregar una barra de scrollbar al texto
            scrollTexto=Scrollbar(frameIText,command=textoCom.yview)
            #.yview es para la vista vertical
            scrollTexto.grid(row=1,column=1,sticky="nsew")
            #Con sticky="nscw" se adapta al tamaño del widgeth al que pertenece
            textoCom.config(yscrollcommand=scrollTexto.set)
            
            #----------------Radiobuttons-----------
            
            RbC=Radiobutton(frameI1,text="Cifrar",variable=ve1,value=1)
            RbC.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC")
            RbC.grid(row=1,column=0)

            RbD=Radiobutton(frameI1,text="Descifrar",variable=ve1,value=2)
            RbD.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");
            RbD.grid(row=1,column=1)
            
            #-------------Button---------------
            
            botonCorD=Button(frameButton,text="Ejecutar",command=lambda:CorD_braille(textoCom,LabelImg,metodoElegido,ve1))
            botonCorD.config(cursor="hand2")
            botonCorD.grid(row=5,column=0)
        
        else:
            print("Cifrado con Imagenes")

        


