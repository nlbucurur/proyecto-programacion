def cifrar(mensaje):
  
  def cifrar_bin(mensaje):
    MAYUSCULA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minuscula = "abcdefghijklmnopqrstuvwxyz"
    palabras = mensaje.split(" ")
    mensaje_cifrado = []
    

    for palabra in palabras:

        palabra_cifrada = " "
        for letra in palabra:

            if letra in MAYUSCULA:
                palabra_cifrada = "010" + bin(MAYUSCULA.index(letra)+1)[2:].zfill(5)
            elif letra in minuscula:
                palabra_cifrada = "011" + bin(minuscula.index(letra)+1)[2:].zfill(5)
            else:
                palabra_cifrada = "[caracter no definido]"
            mensaje_cifrado.append(palabra_cifrada) 
        
        if len(palabras) > 1:
           mensaje_cifrado.append("00100000")
           
    if mensaje_cifrado[-1] == "00100000":
        mensaje_cifrado.pop()

    return ' '.join(mensaje_cifrado)
  
  TABLA = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  binario = cifrar_bin(mensaje)
  cadena_1 = "".join(binario.split(" "))
  bits_6 = []
  mensaje_cifrado=[]
  
  
  for index in range(0,len(cadena_1), 6):    
     bits_6.append(cadena_1[index: index+6])
  
  
  for letra in bits_6:
    
     index = list(letra)
          
     while len(index) < 6:
        index.append("0")
     
     index_64 = int(str("".join(index)), 2)
     mensaje_cifrado.append(TABLA[index_64])      
        

        
  if   len(bits_6)%4 <= 0:
      a = ""
  elif len(bits_6)%4 <= 0.5:
      a = "=="  
      mensaje_cifrado.append(a) 
  elif len(bits_6)%4 >= 0.75:
      a = "="
      mensaje_cifrado.append(a)
        
        
        
  return "".join(mensaje_cifrado)



def descifrar(mensaje):
      
    def descifrar_bin(mensaje):
        MAYUSCULA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        minuscula = "abcdefghijklmnopqrstuvwxyz"
        letras = mensaje.split(" ")
        mensaje_desifrado=[]
        for letra in letras:
             if letra != "00100000":
                 sub_letra = list(letra)
                 if sub_letra[1] == "1":
                     
                      if sub_letra[2] == "0":
                          bin_index = sub_letra[3:len(letra)]
                          index = "".join(bin_index)
                          mensaje_desifrado.append(MAYUSCULA[int(str(index),2 )-1])
                      elif sub_letra[2] == "1":
                          bin_index = sub_letra[3:len(letra)]
                          index = "".join(bin_index)
                          mensaje_desifrado.append(minuscula[int(str(index),2 )-1])
    
    
             if letra == "00100000":
                 mensaje_desifrado.append(" ")

        return ''.join(mensaje_desifrado)
    
    TABLA = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    letras = list(mensaje)
    mensaje_desifrado=[]
    letras_1 = []
    bits6 = []
    bits8 = []
    
    for i in letras:
        if i != "=":
            letras_1.append(i)
    
    for i in letras_1:
      bits6.append(bin(TABLA.index(i))[2:].zfill(6))
    
    cadena =  "".join(bits6)
    
    for index in range(0,len(cadena), 8):    
       bits8.append(cadena[index: index+8])
    
    for i in bits8:
        i_sub = list(i)
        if len(i_sub ) != 8:
            bits8.remove(i)
    
        mensaje_desifrado.append(descifrar_bin(i))
        
    
    return ''.join(mensaje_desifrado)
