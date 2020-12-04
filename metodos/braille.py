# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 14:48:23 2020

@author: Ronald
"""
from tkinter import *

def clone_2(widget):
    parent = widget.nametowidget(widget.winfo_parent())
    clase = widget.__class__
    config_list=[]
    clone = clase(parent)
    for key in widget.configure():
        config_list.append(widget.cget(key))
        clone.config()
    return clone

#-----------------Funciones utilizadas en el método Braille-----------

abc_braille=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

"""
def CorD_braille(croot,textoCom,frameIImg,frameIImgC,metodoElegido,ve1,ve2,lista_botones,img_list):
        
    if ve1.get()==1:
        
        frameIImgC.destroy()
        frameIImgC2=Frame(croot)
        frameIImgC2.config(bg="blue")
        
        mostrar=False;i=0;j=0;x=0
        men_cif=textoCom.get("1.0",'end-1c') #el -1c es para eliminar un \n extra que toma el .get()
        men_cif=men_cif.upper()

        #LabelImg.delete("1.0","end")
        while i<len(men_cif):
            while j<len(img_list):
                if men_cif[i]==abc_braille[j]:
                    Label(frameIImgC2,image=img_list[j]).grid(row=0,column=x)
                    mostrar=True
                    j=26
                else:
                    j+=1
            x+=1
            j=0
            i+=1
        if mostrar:
            frameIImgC2.grid(row=1,column=1)
            
    else:
        label_im=Label(frameIImg,image=img_list[0])
        men_decif=textoCom.get("1.0",'end-1c')
        men_decif=men_decif.upper()
        
        label_im.grid(row=0,column=0)
        #Text no tiene método .set por lo que se usará
        #.delete para borrar el contenido del cuadro
        #y luego se utilizará .insert para poner el mensaje
        #LabelImg.delete(1.0,"end")
        #LabelImg.insert(1.0,lista_met[metodoElegido.get()-1].descifrar(men_decif))

def CorD_brailleInterface(frameIImgC,frameIImg,ve1):
    if ve1.get()==1:
        frameIImgC.grid(row=1,column=1)
        #a=clone_(frameIImgC)
        #print(a.__class__)
        #print(frameIImgC.__class__)
        #a.grid(row=3,column=3)
        frameIImg.grid_forget()
        
    else:
        frameIImg.grid(row=2,column=0)
        frameIImgC.grid_forget()
        """

