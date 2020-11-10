# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 14:17:08 2020

@author: Ronald
"""

lista=[['NG', 'OG', 'PG', 'QG', 'RG', 'SG', 'TG', 'UG', 'VG', 'WG', 'XG', 'YG', 'ZG', 'AG', 'BG', 'CG', 'DG', 'EG', 'FG', 'GG', 'HG', 'IG', 'JG', 'KG', 'LG', 'MG'], 
       ['NF', 'OF', 'PF', 'QF', 'RF', 'SF', 'TF', 'UF', 'VF', 'WF', 'XF', 'YF', 'ZF', 'AF', 'BF', 'CF', 'DF', 'EF', 'FF', 'GF', 'HF', 'IF', 'JF', 'KF', 'LF', 'MF'], 
       ['NE', 'OE', 'PE', 'QE', 'RE', 'SE', 'TE', 'UE', 'VE', 'WE', 'XE', 'YE', 'ZE', 'AE', 'BE', 'CE', 'DE', 'EE', 'FE', 'GE', 'HE', 'IE', 'JE', 'KE', 'LE', 'ME'], 
       ['ND', 'OD', 'PD', 'QD', 'RD', 'SD', 'TD', 'UD', 'VD', 'WD', 'XD', 'YD', 'ZD', 'AD', 'BD', 'CD', 'DD', 'ED', 'FD', 'GD', 'HD', 'ID', 'JD', 'KD', 'LD', 'MD'], 
       ['NC', 'OC', 'PC', 'QC', 'RC', 'SC', 'TC', 'UC', 'VC', 'WC', 'XC', 'YC', 'ZC', 'AC', 'BC', 'CC', 'DC', 'EC', 'FC', 'GC', 'HC', 'IC', 'JC', 'KC', 'LC', 'MC'], 
       ['NB', 'OB', 'PB', 'QB', 'RB', 'SB', 'TB', 'UB', 'VB', 'WB', 'XB', 'YB', 'ZB', 'AB', 'BB', 'CB', 'DB', 'EB', 'FB', 'GB', 'HB', 'IB', 'JB', 'KB', 'LB', 'MB'], 
       ['NA', 'OA', 'PA', 'QA', 'RA', 'SA', 'TA', 'UA', 'VA', 'WA', 'XA', 'YA', 'ZA', 'AA', 'BA', 'CA', 'DA', 'EA', 'FA', 'GA', 'HA', 'IA', 'JA', 'KA', 'LA', 'MA'], 
       ['NZ', 'OZ', 'PZ', 'QZ', 'RZ', 'SZ', 'TZ', 'UZ', 'VZ', 'WZ', 'XZ', 'YZ', 'ZZ', 'AZ', 'BZ', 'CZ', 'DZ', 'EZ', 'FZ', 'GZ', 'HZ', 'IZ', 'JZ', 'KZ', 'LZ', 'MZ'], 
       ['NY', 'OY', 'PY', 'QY', 'RY', 'SY', 'TY', 'UY', 'VY', 'WY', 'XY', 'YY', 'ZY', 'AY', 'BY', 'CY', 'DY', 'EY', 'FY', 'GY', 'HY', 'IY', 'JY', 'KY', 'LY', 'MY'], 
       ['NX', 'OX', 'PX', 'QX', 'RX', 'SX', 'TX', 'UX', 'VX', 'WX', 'XX', 'YX', 'ZX', 'AX', 'BX', 'CX', 'DX', 'EX', 'FX', 'GX', 'HX', 'IX', 'JX', 'KX', 'LX', 'MX'], 
       ['NW', 'OW', 'PW', 'QW', 'RW', 'SW', 'TW', 'UW', 'VW', 'WW', 'XW', 'YW', 'ZW', 'AW', 'BW', 'CW', 'DW', 'EW', 'FW', 'GW', 'HW', 'IW', 'JW', 'KW', 'LW', 'MW'], 
       ['NV', 'OV', 'PV', 'QV', 'RV', 'SV', 'TV', 'UV', 'VV', 'WV', 'XV', 'YV', 'ZV', 'AV', 'BV', 'CV', 'DV', 'EV', 'FV', 'GV', 'HV', 'IV', 'JV', 'KV', 'LV', 'MV'], 
       ['NU', 'OU', 'PU', 'QU', 'RU', 'SU', 'TU', 'UU', 'VU', 'WU', 'XU', 'YU', 'ZU', 'AU', 'BU', 'CU', 'DU', 'EU', 'FU', 'GU', 'HU', 'IU', 'JU', 'KU', 'LU', 'MU'], 
       ['NT', 'OT', 'PT', 'QT', 'RT', 'ST', 'TT', 'UT', 'VT', 'WT', 'XT', 'YT', 'ZT', 'AT', 'BT', 'CT', 'DT', 'ET', 'FT', 'GT', 'HT', 'IT', 'JT', 'KT', 'LT', 'MT'], 
       ['NS', 'OS', 'PS', 'QS', 'RS', 'SS', 'TS', 'US', 'VS', 'WS', 'XS', 'YS', 'ZS', 'AS', 'BS', 'CS', 'DS', 'ES', 'FS', 'GS', 'HS', 'IS', 'JS', 'KS', 'LS', 'MS'], 
       ['NR', 'OR', 'PR', 'QR', 'RR', 'SR', 'TR', 'UR', 'VR', 'WR', 'XR', 'YR', 'ZR', 'AR', 'BR', 'CR', 'DR', 'ER', 'FR', 'GR', 'HR', 'IR', 'JR', 'KR', 'LR', 'MR'], 
       ['NQ', 'OQ', 'PQ', 'QQ', 'RQ', 'SQ', 'TQ', 'UQ', 'VQ', 'WQ', 'XQ', 'YQ', 'ZQ', 'AQ', 'BQ', 'CQ', 'DQ', 'EQ', 'FQ', 'GQ', 'HQ', 'IQ', 'JQ', 'KQ', 'LQ', 'MQ'], 
       ['NP', 'OP', 'PP', 'QP', 'RP', 'SP', 'TP', 'UP', 'VP', 'WP', 'XP', 'YP', 'ZP', 'AP', 'BP', 'CP', 'DP', 'EP', 'FP', 'GP', 'HP', 'IP', 'JP', 'KP', 'LP', 'MP'], 
       ['NO', 'OO', 'PO', 'QO', 'RO', 'SO', 'TO', 'UO', 'VO', 'WO', 'XO', 'YO', 'ZO', 'AO', 'BO', 'CO', 'DO', 'EO', 'FO', 'GO', 'HO', 'IO', 'JO', 'KO', 'LO', 'MO'], 
       ['NN', 'ON', 'PN', 'QN', 'RN', 'SN', 'TN', 'UN', 'VN', 'WN', 'XN', 'YN', 'ZN', 'AN', 'BN', 'CN', 'DN', 'EN', 'FN', 'GN', 'HN', 'IN', 'JN', 'KN', 'LN', 'MN'], 
       ['NM', 'OM', 'PM', 'QM', 'RM', 'SM', 'TM', 'UM', 'VM', 'WM', 'XM', 'YM', 'ZM', 'AM', 'BM', 'CM', 'DM', 'EM', 'FM', 'GM', 'HM', 'IM', 'JM', 'KM', 'LM', 'MM'], 
       ['NL', 'OL', 'PL', 'QL', 'RL', 'SL', 'TL', 'UL', 'VL', 'WL', 'XL', 'YL', 'ZL', 'AL', 'BL', 'CL', 'DL', 'EL', 'FL', 'GL', 'HL', 'IL', 'JL', 'KL', 'LL', 'ML'], 
       ['NK', 'OK', 'PK', 'QK', 'RK', 'SK', 'TK', 'UK', 'VK', 'WK', 'XK', 'YK', 'ZK', 'AK', 'BK', 'CK', 'DK', 'EK', 'FK', 'GK', 'HK', 'IK', 'JK', 'KK', 'LK', 'MK'], 
       ['NJ', 'OJ', 'PJ', 'QJ', 'RJ', 'SJ', 'TJ', 'UJ', 'VJ', 'WJ', 'XJ', 'YJ', 'ZJ', 'AJ', 'BJ', 'CJ', 'DJ', 'EJ', 'FJ', 'GJ', 'HJ', 'IJ', 'JJ', 'KJ', 'LJ', 'MJ'], 
       ['NI', 'OI', 'PI', 'QI', 'RI', 'SI', 'TI', 'UI', 'VI', 'WI', 'XI', 'YI', 'ZI', 'AI', 'BI', 'CI', 'DI', 'EI', 'FI', 'GI', 'HI', 'II', 'JI', 'KI', 'LI', 'MI'], 
       ['NH', 'OH', 'PH', 'QH', 'RH', 'SH', 'TH', 'UH', 'VH', 'WH', 'XH', 'YH', 'ZH', 'AH', 'BH', 'CH', 'DH', 'EH', 'FH', 'GH', 'HH', 'IH', 'JH', 'KH', 'LH', 'MH']]




def cifrar(mensaje):
    i=0;j=0   #i es la palabra y j es la posicion de la letra en cada palabra
    mensaje=mensaje.upper()      #Convierte las letras del mensaje en mayusculas
    mensaje=mensaje.split()      #Organiza las palabras del mensaje en una lista, eliminando los espacios
    mensaje_cifrado=[]
    while i < len(mensaje):
        if (len(mensaje[i])%2)==0:
            Par=True
        else: Par=False
        while j<len(mensaje[i]):
            cord_x=ord(mensaje[i][j])-65        #-65 porque ord('A')=65, por lo que se "alinean" con la lista
            
            if (j+1)<len(mensaje[i]):
                    
                cord_y=ord(mensaje[i][j+1])-65
                mensaje_cifrado.append(lista[cord_y][cord_x])
                
            elif j==(len(mensaje[i])-1):
                if Par==False:
                    cord_y=23
                    mensaje_cifrado.append(lista[cord_y][cord_x])
                else: break
            j+=2
        j=0
        i+=1
    return ' '.join(mensaje_cifrado)

def descifrar(mensaje):
    
    mensaje=mensaje.upper()
    mensaje=mensaje.replace(' ','')   #"Elimina" todos los espacios blancos
    mensaje_descifrado = []
    i=0
    cord_x=0
    cord_y=0
    while i<len(mensaje):
        break1=False
        while cord_y< 26:
            while cord_x<26:
                if lista[cord_y][cord_x]==mensaje[i:i+2]:                       #Compara los datos de la lista con una pareja de caracteres de mensaje
                    mensaje_descifrado.append((chr(cord_x+65)+chr(cord_y+65)))  #+65 para que el numero coincida con la posicion en la tabla ASCII
                    break1=True                                                 
                    break                                                       #Agrega el par de letras a mensaje_descifrado y termina este ciclo while
                else: cord_x+=1
            if break1:break                                                     #Como ya se revisaron las letras mensaje[i:i+2] termina tambien este ciclo
            else:
                cord_x=0
                cord_y+=1
        cord_y=0
        i+=2
    return ' '.join(mensaje_descifrado)


def run():

    while True:

        opcion = str(input('''Bienvenido al cifrador. ¿Qué deseas hacer? Pulsa la tecla correspondiente:
            [c]ifrar
            [d]escifrar
            [s]alir
            '''))

        if opcion == 'c':
            mensaje = str(input('Ingresa el mensaje que deseas cifrar: '))
            mensaje_cifrado = cifrar(mensaje)
            print(mensaje_cifrado)

        elif opcion == 'd':
            mensaje = str(input('Ingresa la oracion que deseas descifrar: '))
            mensaje_descifrado = descifrar(mensaje)
            print(mensaje_descifrado)

        elif opcion == 's':
            print('¡Gracias por jugar, vuelve pronto!')
            break

        else:
            print('No has seleccionado ninguna opción valida. Ejecuta el programa nuevamente.')
            break

if __name__ == '__main__':
    run()
    
    
    
"""  
    
lista_x=['N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C'
         ,'D','E','F','G','H','I','J','K','L','M']
lista_y=['G','F','E','D','C','B','A','Z','Y','X','W','V','U','T','S'
         ,'R','Q','P','O','N','M','L','K','J','I','H']
diagrama=[]
i=0;j=0
while i<26:
    lista_temp=[]
    while j<26:
        lista_temp.append(lista_x[j]+lista_y[i])
        j+=1
    diagrama.append(lista_temp)
    j=0
    i+=1    
print(diagrama)
"""