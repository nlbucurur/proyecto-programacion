def matriz(x,y,comienzo):
    return [[comienzo for i in range(x)] for j in range(y)]
    
ini_matriz=matriz(5,5,0)

def localizacion_indice(c): 
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(ini_matriz):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def cifrar(mensaje,llave='A'):
    mc = ''
    #llave=input("Por favor, introduce la llave con la que quieres cifrar el texto: ")
    llave=llave.replace(" ", "")
    llave=llave.upper()
    result=list()
    for c in llave: 
        if c not in result:
            if c=='J':
                result.append('I')
            else:
                result.append(c)
    flag=0
    for i in range(65,91): 
        if chr(i) not in result:
            if i==73 and chr(74) not in result:
                result.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                result.append(chr(i))
    k=0
    for i in range(0,5): 
        for j in range(0,5):
            ini_matriz[i][j]=result[k]
            k+=1
    mensaje=mensaje.upper()
    mensaje=mensaje.replace(" ", "")             
    i=0
    for s in range(0,len(mensaje)+1,2):
        if s<len(mensaje)-1:
            if mensaje[s]==mensaje[s+1]:
                mensaje=mensaje[:s+1]+'X'+mensaje[s+1:]
    if len(mensaje)%2!=0:
        mensaje=mensaje[:]+'X'
    while i<len(mensaje):
        loc=list()
        loc=localizacion_indice(mensaje[i])
        loc1=list()
        loc1=localizacion_indice(mensaje[i+1])
        if loc[1]==loc1[1]:
            mc = mc + ini_matriz[(loc[0]+1)%5][loc[1]]
            mc = mc + ini_matriz[(loc1[0]+1)%5][loc1[1]]
            mc = mc + ' '
            #print("{}{}".format(ini_matriz[(loc[0]+1)%5][loc[1]],ini_matriz[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            mc = mc + ini_matriz[loc[0]][(loc[1]+1)%5]
            mc = mc + ini_matriz[loc1[0]][(loc1[1]+1)%5]
            mc = mc + ' '
            #print("{}{}".format(ini_matriz[loc[0]][(loc[1]+1)%5],ini_matriz[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            mc = mc + ini_matriz[loc[0]][loc1[1]]
            mc = mc + ini_matriz[loc1[0]][loc[1]]
            mc = mc + ' '
            #print("{}{}".format(ini_matriz[loc[0]][loc1[1]],ini_matriz[loc1[0]][loc[1]]),end=' ')    
        i=i+2
    return mc      
                 
def descifrar(mensaje,llave='A'):
    md = ''
    #llave=input("Por favor, introduce la llave con la que se cifró el texto: ")
    llave=llave.replace(" ", "")
    llave=llave.upper()
    result=list()
    for c in llave: 
        if c not in result:
            if c=='J':
                result.append('I')
            else:
                result.append(c)
    flag=0
    for i in range(65,91): 
        if chr(i) not in result:
            if i==73 and chr(74) not in result:
                result.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                result.append(chr(i))
    k=0
    for i in range(0,5): 
        for j in range(0,5):
            ini_matriz[i][j]=result[k]
            k+=1
    mensaje=mensaje.upper()
    mensaje=mensaje.replace(" ", "")  
    i=0
    while i<len(mensaje):
        loc=list()
        loc=localizacion_indice(mensaje[i])
        loc1=list()
        loc1=localizacion_indice(mensaje[i+1])
        if loc[1]==loc1[1]:
            md = md + ini_matriz[(loc[0]-1)%5][loc[1]]
            md = md + ini_matriz[(loc1[0]-1)%5][loc1[1]]
            md = md + ' '           
        elif loc[0]==loc1[0]:
            md = md + ini_matriz[loc[0]][(loc[1]-1)%5]
            md = md + ini_matriz[loc1[0]][(loc1[1]-1)%5]
            md = md + ' '  
        else:
            md = md + ini_matriz[loc[0]][loc1[1]]
            md = md + ini_matriz[loc1[0]][loc[1]]
            md = md + ' '
        i=i+2        
    return md