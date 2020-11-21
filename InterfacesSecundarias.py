# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:27:42 2020

@author: Ronald
"""
from tkinter import *
from metodos import A1Z26, ascii, atbash, bacon, base64, binary, columnar
from metodos import digraph, morse, multiplicativo, rot, transposition,braille
lista_met=[A1Z26,ascii,atbash,bacon,base64,binary,columnar,digraph,morse,multiplicativo,rot,transposition]


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



def VentanaCifrado(root,metodoElegido,lista_met,lista_nom,ve1,ve2,img_list): 
    
    if metodoElegido.get()==0:
        messagebox.showinfo("Seleccionar","Por favor seleccione un método de cifrado")
        
    else:
        
        #Configuracion básica que tendrán todas las ventanas de cifrado
        # Objeto de la clase Toplevel y se usa como otra ventana
        croot = Toplevel(root)  
        croot.iconbitmap("img\VCypher.ico")
        croot.title((lista_nom[metodoElegido.get()-1])+" cypher") 
        
        if metodoElegido.get()<13:
            
            croot.config(bg="light blue")
            #Tamaño de la nueva ventana
            #croot.geometry("1000x600")
            #-----------------Frames----------------
            frameI1=Frame(croot,width=500,height=200)
            frameI1.config(bg="#EEFBFC",width=500,height=200)
            frameI1.grid(row=0,column=0,columnspan=3,padx=10,pady=5)
            
            frameIText1=Frame(croot)#,width=200,height=10)
            frameIText1.config(bg="red")
            frameIText1.grid(row=1,column=0,padx=10,pady=10)
            
            frameIText2=Frame(croot)
            frameIText2.config(bg="green")
            frameIText2.grid(row=1,column=2,padx=10,pady=10)
            
            frameButton=Frame(croot)
            frameButton.grid(row=2,column=0,padx=10,pady=15,columnspan=3)
            
            #----------------Cuadros de texto----------------
            Label(frameI1,text="       Por favor elige una de las opciones           ").grid(row=0,column=0,columnspan=2)
            
            textoCom1=Text(frameIText1,width=30,height=12)
            textoCom1.grid(row=1,column=0,padx=10,pady=10)

            textoCom2=Text(frameIText2,width=30,height=12)
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
            RbC.config(cursor="hand2",padx=10,pady=10,bg="#EEFBFC")
            RbC.grid(row=1,column=0)

            RbD=Radiobutton(frameI1,text="Descifrar",variable=ve1,value=2)
            RbD.config(cursor="hand2",padx=10,pady=10,bg="#EEFBFC");
            RbD.grid(row=1,column=1)
            
            
            
            #-------------Button---------------
            
            botonCorD=Button(frameButton,text="Ejecutar",command=lambda:CypherOrDecypher(textoCom1,textoCom2,metodoElegido,ve1))
            botonCorD.config(cursor="hand2")
            botonCorD.pack()
        #---------------------Caso Braille------------------------
        elif metodoElegido.get()==13:
            
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

            #LabelImg=Text(frameIImg,width=40,height=10)
            #LabelImg.grid(row=1,column=0,padx=10,pady=10)
            
            #-------------Barras de scroll------------
            
            #Para agregar una barra de scrollbar al texto
            scrollTexto=Scrollbar(frameIText,command=textoCom.yview)
            #.yview es para la vista vertical
            scrollTexto.grid(row=1,column=1,sticky="nsew")
            #Con sticky="nscw" se adapta al tamaño del widgeth al que pertenece
            textoCom.config(yscrollcommand=scrollTexto.set)
            
            #----------------Teclado-------------------
            
             
            #labelB=Label(frameIImg,image=ImageB)
            #labelB.grid(row=0,column=1)
 
            
            botonA=Button(frameIImg,image=img_list[0])
            botonB=Button(frameIImg,image=img_list[1])
            botonC=Button(frameIImg,image=img_list[2])
            botonD=Button(frameIImg,image=img_list[3])
            botonE=Button(frameIImg,image=img_list[4])
            botonF=Button(frameIImg,image=img_list[5])
            botonG=Button(frameIImg,image=img_list[6])
            botonH=Button(frameIImg,image=img_list[7])
            botonI=Button(frameIImg,image=img_list[8])
            botonJ=Button(frameIImg,image=img_list[9])
            botonK=Button(frameIImg,image=img_list[10])
            botonL=Button(frameIImg,image=img_list[11])
            botonM=Button(frameIImg,image=img_list[12])
            botonN=Button(frameIImg,image=img_list[13])
            botonO=Button(frameIImg,image=img_list[14])
            botonP=Button(frameIImg,image=img_list[15])
            botonQ=Button(frameIImg,image=img_list[16])
            botonR=Button(frameIImg,image=img_list[17])
            botonS=Button(frameIImg,image=img_list[18])
            botonT=Button(frameIImg,image=img_list[19])
            botonU=Button(frameIImg,image=img_list[20])
            botonV=Button(frameIImg,image=img_list[21])
            botonW=Button(frameIImg,image=img_list[22])
            botonX=Button(frameIImg,image=img_list[23])
            botonY=Button(frameIImg,image=img_list[24])
            botonZ=Button(frameIImg,image=img_list[25])
            
            botonA.config(cursor="hand2")
            botonB.config(cursor="hand2")
            botonC.config(cursor="hand2")
            botonD.config(cursor="hand2")
            botonE.config(cursor="hand2")
            botonF.config(cursor="hand2")
            botonG.config(cursor="hand2")
            botonH.config(cursor="hand2")
            botonI.config(cursor="hand2")
            botonJ.config(cursor="hand2")
            botonK.config(cursor="hand2")
            botonL.config(cursor="hand2")
            botonM.config(cursor="hand2")
            botonN.config(cursor="hand2")
            botonO.config(cursor="hand2")
            botonP.config(cursor="hand2")
            botonQ.config(cursor="hand2")
            botonR.config(cursor="hand2")
            botonS.config(cursor="hand2")
            botonT.config(cursor="hand2")
            botonU.config(cursor="hand2")
            botonV.config(cursor="hand2")
            botonW.config(cursor="hand2")
            botonX.config(cursor="hand2")
            botonY.config(cursor="hand2")
            botonZ.config(cursor="hand2")
            
            botonA.grid(row=0,column=0,padx=2,pady=2)
            botonB.grid(row=0,column=1,padx=2,pady=2)
            botonC.grid(row=0,column=2,padx=2,pady=2)
            botonD.grid(row=0,column=3,padx=2,pady=2)
            botonE.grid(row=0,column=4,padx=2,pady=2)
            botonF.grid(row=0,column=5,padx=2,pady=2)
            botonG.grid(row=0,column=6,padx=2,pady=2)
            botonH.grid(row=1,column=0,padx=2,pady=2)
            botonI.grid(row=1,column=1,padx=2,pady=2)
            botonJ.grid(row=1,column=2,padx=2,pady=2)
            botonK.grid(row=1,column=3,padx=2,pady=2)
            botonL.grid(row=1,column=4,padx=2,pady=2)
            botonM.grid(row=1,column=5,padx=2,pady=2)
            botonN.grid(row=1,column=6,padx=2,pady=2)
            botonO.grid(row=2,column=0,padx=2,pady=2)
            botonP.grid(row=2,column=1,padx=2,pady=2)
            botonQ.grid(row=2,column=2,padx=2,pady=2)
            botonR.grid(row=2,column=3,padx=2,pady=2)
            botonS.grid(row=2,column=4,padx=2,pady=2)
            botonT.grid(row=2,column=5,padx=2,pady=2)
            botonU.grid(row=2,column=6,padx=2,pady=2)
            botonV.grid(row=3,column=1,padx=2,pady=2)
            botonW.grid(row=3,column=2,padx=2,pady=2)
            botonX.grid(row=3,column=3,padx=2,pady=2)
            botonY.grid(row=3,column=4,padx=2,pady=2)
            botonZ.grid(row=3,column=5,padx=2,pady=2)
            
            
            
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
            botonCorD.grid(row=5,column=0,padx=15,pady=15)
            #nota: al poner cualquier letra existente en este punto se muestran las imagenes
            #Razón desconocida
            
        else:
            print("Cifrado con Imagenes")

        


