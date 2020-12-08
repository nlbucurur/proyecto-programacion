# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:27:42 2020

@author: Ronald
"""
from tkinter import *
from tkinter import messagebox
from metodos import A1Z26, ascii, atbash, bacon, base64, binary, digraph, columnar,playfair
from metodos import morse, multiplicativo, rot,Tap, transposition, Vigenere,Keyboard_Code

lista_met=[A1Z26,ascii,atbash,bacon,base64,binary,digraph,Keyboard_Code,
           morse,Tap,columnar,multiplicativo,playfair,rot,transposition,Vigenere]


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
        
        
#------------------Funcion que ejecuta la funcion de cifrado o descifrado CON CLAVES-------------
def CorD_CLAVE(textoCom1,textoCom2,Clave,metodoElegido,ve1):
        

    if ve1.get()==1:
        men_cif=textoCom1.get("1.0",'end-1c') #el -1c es para eliminar un \n extra que toma el .get()
        clave=Clave.get()
        textoCom2.delete("1.0","end")
        if clave=='':
            textoCom2.insert("1.0",lista_met[metodoElegido.get()-1].cifrar(men_cif))
        else:
            textoCom2.insert("1.0",lista_met[metodoElegido.get()-1].cifrar(men_cif,clave))
            
    else:
        men_decif=textoCom1.get("1.0",'end-1c')
        clave=Clave.get()
        #Text no tiene método .set por lo que se usará
        #.delete para borrar el contenido del cuadro
        #y luego se utilizará .insert para poner el mensaje
        textoCom2.delete(1.0,"end")
        if clave=='':
            textoCom2.insert(1.0,lista_met[metodoElegido.get()-1].descifrar(men_decif))
        else:
            textoCom2.insert(1.0,lista_met[metodoElegido.get()-1].descifrar(men_decif,clave))


#---------------Funcion que abre una nueva ventana donde se cifra y descifra un mensaje------------



def VentanaCifrado(root,metodoElegido,lista_nom,ve1,ve2,img_list,img_list1,img_list2): 
    
    if metodoElegido.get()==0:
        messagebox.showinfo("Seleccionar","Por favor seleccione un método de cifrado")
        
    else:
        
        #Configuracion básica que tendrán todas las ventanas de cifrado
        # Objeto de la clase Toplevel y se usa como otra ventana
        croot = Toplevel(root)  
        croot.iconbitmap("img\VCypher.ico")
        croot.title((lista_nom[metodoElegido.get()-1])+" cypher") 
        croot.resizable(0,0)
        
        #-------------Transformacion----------------------------------------------------
        
        
        if metodoElegido.get()<11:
            
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
            
            
        #---------------------Clave------------------------------------------------------------------------
        
        
        elif metodoElegido.get()<17:
            
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
            
            frameIClave=Frame(croot)
            frameIClave.grid(row=2,column=0,padx=10,pady=10,columnspan=3)
            
            frameButton=Frame(croot)
            frameButton.grid(row=3,column=0,padx=10,pady=15,columnspan=3)
            
            #----------------Cuadros de texto----------------
            Label(frameI1,text="       Por favor elige una de las opciones           ").grid(row=0,column=0,columnspan=2)
            
            textoCom1=Text(frameIText1,width=30,height=12)
            textoCom1.grid(row=1,column=0,padx=10,pady=10)

            textoCom2=Text(frameIText2,width=30,height=12)
            textoCom2.grid(row=1,column=0,padx=10,pady=10)
            
            textoClave=Entry(frameIClave)
            textoClave.grid(row=0,column=0)
            
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
            
            botonCorD=Button(frameButton,text="Ejecutar",command=lambda:CorD_CLAVE(textoCom1,textoCom2,textoClave,
                                                                                   metodoElegido,ve1))
            botonCorD.config(cursor="hand2")
            botonCorD.pack()
        
        
        #---------------------Caso Braille-----------------------------------------------------------------------
        
        
        
        elif metodoElegido.get()<20:
            
            croot.config(bg="#D6DBDF")
            #Tamaño de la nueva ventana
            croot.geometry("680x600")
            
            
            #-----------------Frames----------------
            frameI1=Frame(croot,width=500,height=200)
            frameI1.config(bg="light blue",width=500,height=200)
            frameI1.grid(row=0,column=0)#,columnspan=3)
            
            frameIText=Frame(croot,width=200,height=300)
            frameIText.config(bg="red")
            frameIText.grid(row=1,column=0)
            
            frameIImgC=Frame(croot,width=200,height=300)
            frameIImgC.config(bg="orange")
            frameIImgC.grid(row=1,column=1)
            
            frameIImg=Frame(croot,width=200,height=300)
            frameIImg.config(bg="green")
            #frameIImg.grid(row=2,column=0)
            
            frameButton=Frame(croot)
            frameButton.grid(row=3,column=0)#,columnspan=3)
            
            #----------------Radiobuttons-----------
            
            RbC=Radiobutton(frameI1,text="Cifrar",variable=ve1,value=1,command=lambda:
                            CorD_brailleInterface(frameIImgC,frameIImg,frameButton,ve1))
            RbC.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC")
            RbC.grid(row=1,column=0)

            RbD=Radiobutton(frameI1,text="Descifrar",variable=ve1,value=2,command=lambda:
                            CorD_brailleInterface(frameIImgC,frameIImg,frameButton,ve1))
            RbD.config(cursor="hand2",padx=10,pady=10,bg="#F6DDCC");
            RbD.grid(row=1,column=1)
            
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
            
            #-------------Button---------------
            if metodoElegido.get()==17:  
                botonCorD=Button(frameButton,text="Ejecutar",command=lambda:CorD_Imgs
                             (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,0,img_list))
                botonCorD.config(cursor="hand2")
                botonCorD.grid(row=5,column=0,padx=15,pady=15)
            #nota: al poner cualquier letra existente en este punto se muestran las imagenes
            #Razón desconocida
            elif metodoElegido.get()==18:  
                botonCorD=Button(frameButton,text="Ejecutar",command=lambda:CorD_Imgs
                             (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,0,img_list1))
                botonCorD.config(cursor="hand2")
                botonCorD.grid(row=5,column=0,padx=15,pady=15)
            else:
                botonCorD=Button(frameButton,text="Ejecutar",command=lambda:CorD_Imgs
                             (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,0,img_list2))
                botonCorD.config(cursor="hand2")
                botonCorD.grid(row=5,column=0,padx=15,pady=15)
            
        
            #----------------Teclado-------------------
            
            #-----Teclado Braille
            if metodoElegido.get()==17:
 
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
        
        
                botonA.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,0,img_list))
                botonB.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,1,img_list))
                botonC.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,2,img_list))
                botonD.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,3,img_list))
                botonE.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,4,img_list))
                botonF.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,5,img_list))
                botonG.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,6,img_list))
                botonH.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,7,img_list))
                botonI.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,8,img_list))
                botonJ.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,9,img_list))
                botonK.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,10,img_list))
                botonL.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,11,img_list))
                botonM.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,12,img_list))
                botonN.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,13,img_list))
                botonO.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,14,img_list))
                botonP.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,15,img_list))
                botonQ.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,16,img_list))
                botonR.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,17,img_list))
                botonS.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,18,img_list))
                botonT.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,19,img_list))
                botonU.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,20,img_list))
                botonV.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,21,img_list))
                botonW.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,22,img_list))
                botonX.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,23,img_list))
                botonY.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,24,img_list))
                botonZ.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,25,img_list))
        
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
            
            #---------Teclado Dorabella-------
            
            elif metodoElegido.get()==18:
                botonA=Button(frameIImg,image=img_list1[0])
                botonB=Button(frameIImg,image=img_list1[1])
                botonC=Button(frameIImg,image=img_list1[2])
                botonD=Button(frameIImg,image=img_list1[3])
                botonE=Button(frameIImg,image=img_list1[4])
                botonF=Button(frameIImg,image=img_list1[5])
                botonG=Button(frameIImg,image=img_list1[6])
                botonH=Button(frameIImg,image=img_list1[7])
                botonI_J=Button(frameIImg,image=img_list1[8])
                botonK=Button(frameIImg,image=img_list1[9])
                botonL=Button(frameIImg,image=img_list1[10])
                botonM=Button(frameIImg,image=img_list1[11])
                botonN=Button(frameIImg,image=img_list1[12])
                botonO=Button(frameIImg,image=img_list1[13])
                botonP=Button(frameIImg,image=img_list1[14])
                botonQ=Button(frameIImg,image=img_list1[15])
                botonR=Button(frameIImg,image=img_list1[16])
                botonS=Button(frameIImg,image=img_list1[17])
                botonT=Button(frameIImg,image=img_list1[18])
                botonU_V=Button(frameIImg,image=img_list1[19])
                botonW=Button(frameIImg,image=img_list1[20])
                botonX=Button(frameIImg,image=img_list1[21])
                botonY=Button(frameIImg,image=img_list1[22])
                botonZ=Button(frameIImg,image=img_list1[23])
        
        
                botonA.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,0,img_list1))
                botonB.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,1,img_list1))
                botonC.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,2,img_list1))
                botonD.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,3,img_list1))
                botonE.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,4,img_list1))
                botonF.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,5,img_list1))
                botonG.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,6,img_list1))
                botonH.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,7,img_list1))
                botonI_J.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,8,img_list1))
                botonK.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,9,img_list1))
                botonL.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,10,img_list1))
                botonM.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,11,img_list1))
                botonN.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,12,img_list1))
                botonO.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,13,img_list1))
                botonP.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,14,img_list1))
                botonQ.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,15,img_list1))
                botonR.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,16,img_list1))
                botonS.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,17,img_list1))
                botonT.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,18,img_list1))
                botonU_V.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,19,img_list1))
                botonW.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,20,img_list1))
                botonX.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,21,img_list1))
                botonY.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,22,img_list1))
                botonZ.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,23,img_list1))
        
                botonA.grid(row=0,column=0,padx=2,pady=2)
                botonB.grid(row=0,column=1,padx=2,pady=2)
                botonC.grid(row=0,column=2,padx=2,pady=2)
                botonD.grid(row=0,column=3,padx=2,pady=2)
                botonE.grid(row=0,column=4,padx=2,pady=2)
                botonF.grid(row=0,column=5,padx=2,pady=2)
                botonG.grid(row=1,column=0,padx=2,pady=2)
                botonH.grid(row=1,column=1,padx=2,pady=2)
                botonI_J.grid(row=1,column=2,padx=2,pady=2)
                botonK.grid(row=1,column=3,padx=2,pady=2)
                botonL.grid(row=1,column=4,padx=2,pady=2)
                botonM.grid(row=1,column=5,padx=2,pady=2)
                botonN.grid(row=2,column=0,padx=2,pady=2)
                botonO.grid(row=2,column=1,padx=2,pady=2)
                botonP.grid(row=2,column=2,padx=2,pady=2)
                botonQ.grid(row=2,column=3,padx=2,pady=2)
                botonR.grid(row=2,column=4,padx=2,pady=2)
                botonS.grid(row=2,column=5,padx=2,pady=2)
                botonT.grid(row=3,column=0,padx=2,pady=2)
                botonU_V.grid(row=3,column=1,padx=2,pady=2)
                botonW.grid(row=3,column=2,padx=2,pady=2)
                botonX.grid(row=3,column=3,padx=2,pady=2)
                botonY.grid(row=3,column=4,padx=2,pady=2)
                botonZ.grid(row=3,column=5,padx=2,pady=2)
                
            #-------------Teclado Rosicrucian------
            else:
                
                botonA=Button(frameIImg,image=img_list2[0])
                botonB=Button(frameIImg,image=img_list2[1])
                botonC=Button(frameIImg,image=img_list2[2])
                botonD=Button(frameIImg,image=img_list2[3])
                botonE=Button(frameIImg,image=img_list2[4])
                botonF=Button(frameIImg,image=img_list2[5])
                botonG=Button(frameIImg,image=img_list2[6])
                botonH=Button(frameIImg,image=img_list2[7])
                botonI=Button(frameIImg,image=img_list2[8])
                botonJ=Button(frameIImg,image=img_list2[9])
                botonK=Button(frameIImg,image=img_list2[10])
                botonL=Button(frameIImg,image=img_list2[11])
                botonM=Button(frameIImg,image=img_list2[12])
                botonN=Button(frameIImg,image=img_list2[13])
                botonO=Button(frameIImg,image=img_list2[14])
                botonP=Button(frameIImg,image=img_list2[15])
                botonQ=Button(frameIImg,image=img_list2[16])
                botonR=Button(frameIImg,image=img_list2[17])
                botonS=Button(frameIImg,image=img_list2[18])
                botonT=Button(frameIImg,image=img_list2[19])
                botonU=Button(frameIImg,image=img_list2[20])
                botonV=Button(frameIImg,image=img_list2[21])
                botonW=Button(frameIImg,image=img_list2[22])
                botonX=Button(frameIImg,image=img_list2[23])
                botonY=Button(frameIImg,image=img_list2[24])
                botonZ=Button(frameIImg,image=img_list2[25])
        
        
                botonA.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,0,img_list2))
                botonB.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,1,img_list2))
                botonC.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,2,img_list2))
                botonD.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,3,img_list2))
                botonE.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,4,img_list2))
                botonF.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,5,img_list2))
                botonG.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,6,img_list2))
                botonH.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,7,img_list2))
                botonI.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,8,img_list2))
                botonJ.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,9,img_list2))
                botonK.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,10,img_list2))
                botonL.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,11,img_list2))
                botonM.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,12,img_list2))
                botonN.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,13,img_list2))
                botonO.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,14,img_list2))
                botonP.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,15,img_list2))
                botonQ.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,16,img_list2))
                botonR.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,17,img_list2))
                botonS.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,18,img_list2))
                botonT.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,19,img_list2))
                botonU.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,20,img_list2))
                botonV.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,21,img_list2))
                botonW.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,22,img_list2))
                botonX.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,23,img_list2))
                botonY.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,24,img_list2))
                botonZ.config(cursor="hand2",command=lambda:CorD_Imgs
                                 (croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,25,img_list2))
        
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
                
           
            
        else:
            print("Cifrado con Imagenes")

        

#---------------Funciones adicionales para metodos de imagenes

#-----------------Funciones utilizadas en el método Braille-----------



def CorD_Imgs(croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,ve2,img_list):
        
    abc_braille_rosicrucian=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    abc_dorabella=["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","V","W","X","Y","Z"]
    
    if metodoElegido.get()==17 or metodoElegido.get()==19:
        abc=abc_braille_rosicrucian
    else: 
        abc=abc_dorabella    

    if ve1.get()==1:
        
        frameIImgC.destroy()
        frameIImgC=Frame(croot)
        frameIImgC.config(bg="red")
        
        mostrar=False;i=0;j=0;x=0;y=0
        men_cif=textoCom.get("1.0",'end-1c') #el -1c es para eliminar un \n extra que toma el .get()
        men_cif=men_cif.upper()

        #LabelImg.delete("1.0","end")
        while i<len(men_cif):
            while j<len(img_list):
                if men_cif[i]==abc[j]:
                    if x==5:
                        y+=1
                        x=0
                    Label(frameIImgC,image=img_list[j]).grid(row=y,column=x)
                    mostrar=True
                    j=26
                else:
                    j+=1
            x+=1
            j=0
            i+=1
        if mostrar:
            frameIImgC.grid(row=1,column=1)
            
    else:
        
        men_decif=textoCom.get("1.0",'end-1c')
        men_decif=men_decif.upper()
        textoCom.delete("1.0","end")
        textoCom.insert(1.0,men_decif+abc[ve2])
        #Text no tiene método .set por lo que se usará
        #.delete para borrar el contenido del cuadro
        #y luego se utilizará .insert para poner el mensaje
        #LabelImg.delete(1.0,"end")
        #LabelImg.insert(1.0,lista_met[metodoElegido.get()-1].descifrar(men_decif))
"""op_label=[]
label2=Label(root,image=Image1)
op_label.append(labelx)"""

def CorD_brailleInterface(frameIImgC,frameIImg,frameButton,ve1):
    if ve1.get()==1:
        frameIImgC.grid(row=1,column=1)
        #a=clone_(frameIImgC)
        #print(a.__class__)
        #print(frameIImgC.__class__)
        #a.grid(row=3,column=3)
        frameIImg.grid_forget()
        frameButton.grid(row=3,column=0)
        
    else:
        frameButton.grid_forget()
        frameIImg.grid(row=2,column=0)
        frameIImgC.grid_forget()

