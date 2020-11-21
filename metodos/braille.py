# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 14:48:23 2020

@author: Ronald
"""
#-----------------Funciones utilizadas en el método Braille-----------

abc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def CorD_braille(textoCom,frameIImg,metodoElegido,ve1,ve2,lista_botones):
        
    if ve1.get()==1:
        i=0
        j=0
        men_cif=textoCom.get("1.0",'end-1c') #el -1c es para eliminar un \n extra que toma el .get()
        men_cif=men_cif.upper()
        #LabelImg.delete("1.0","end")
        while i<len(men_cif):
            while j<26:
                if men_cif[i]==abc[j]:
                    lista_botones[j].grid(row=0,column=0)
                    j=26
                else:
                    j+=1
            j=0
            i+=1
            
    else:
        men_decif=textoCom.get("1.0",'end-1c')
            
        #Text no tiene método .set por lo que se usará
        #.delete para borrar el contenido del cuadro
        #y luego se utilizará .insert para poner el mensaje
        LabelImg.delete(1.0,"end")
        LabelImg.insert(1.0,lista_met[metodoElegido.get()-1].descifrar(men_decif))

def CorD_brailleInterface(frameIImgC,frameIImg,ve1):
    if ve1.get()==1:
        frameIImgC.grid(row=1,column=1)
        frameIImg.grid_forget()
        
    else:
        frameIImg.grid(row=2,column=0)
        frameIImgC.grid_forget()
