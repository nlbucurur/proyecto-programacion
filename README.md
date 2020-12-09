# proyecto-programación - Encriptado y Desencripatado

## Planteamiento y Justificación del Problema

El cifrado o la encriptación de mensajes han sido de gran utilidad e importancia a lo largo de la historia, ya que juegan un papel fundamental en la seguridad, tanto de un país, como de un mensaje enviado a través de una aplicación de mensajería, pagos electrónicos, bases de datos de grandes y pequeñas empresas, información personal de los usuarios, etc. Esta es una ciencia que evoluciona constantemente debido a que debe proteger información delicada. Se han encontrado metodos de cifrado desde el Siglo I a.C, y se han desarrollado de tal forma que, con ayuda de las compuadoras, son cada vez más complejos y díficiles de desencriptar, además se presenta una visión bastante amplia en el fúturo, ya que puede ser desarrollada como una aplicación de la computación cuántica, pues, el comportamiento de esta física es netamente probabilistico, permitiendo así, la superposición de los estados cuánticos, además se ha notado que estos estados en un sistema, colapsan al ser observados. Imaginar este tipo de encriptación, en la que, por ejemplo, al intentar leer una tarjeta de crédito cuántica para clonarla, esta colapse a un solo estado y pierda toda la información, puede ser posible, muestra un gran camino por recorrer en la ciencia y en especial, en este tipo de aplicación, aunque por ahora solo puede estar en nuestra imaginación.

Debido a la importancia del encriptado y desencriptado en la sociedad, este proyecto del curso de "Programación e Introducción a los métodos númericos" de la Universidad Nacional de Colombia, pretende crear un programa que encripte y desencripte textos dados por el ususario con algunos métodos que van desde los más sencillos, hasta algunos más complicados a través de una interfaz gráfica sencilla que permitirá mayor comodidad para el ususario a la hora de usar el programa. Además, permitirá desarrollar a los estudiantes, habilidades en la programción y conocimientos básicos en el área de la seguridad informatica.

## Métodos de Cifrado y Descifrado

A continuación se presentará la lista de metodos de encriptado que se trabajarán en este proyecto, se explicará en que consiste cada uno:

### 1. A1Z26 
Este método consiste en remplazar las letras del alfabeto por números que van desde el 1 hasta el 26.

|Entrada|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
|--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- |
|Salida |1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|

### 2. ASCII
Este metodo remplaza cada letra introducida por su valor numerico correspondiente a la tabla ASCII.


### 3. ATBASH
Este método invierte el orden del alfabeto y remplaza cada letra con su correspondiente en este alfabeto invertido. 

|Entrada|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
|--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- |
|Salida |Z|Y|X|W|V|U|T|S|R|Q|P|O|N|M|L|K|K|I|H|G|F|E|D|C|B|A|

### 4. BINARIO
Este metodo realiza el cambio a representación binaria para cada letra

### 5. DIGRAPH
Este metodo divide toda cadena de caracteres en pares de letras (si la cadena tiene una cantidad impar agrega una X al final), cada par de letras corresponde a una coordenada dentro de la tabla mostrada a continuación (la primera letra del par determina la columna y la segunda la fila).

|COORDENADAS|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
|--- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | ---|
|A|NG|OG|PG|QG|RG|SG|TG|UG|VG|WG|XG|YG|ZG|AG|BG|CG|DG|EG|FG|GG|HG|IG|JG|KG|LG|MG|
|B|NF|OF|PF|QF|RF|SF|TF|UF|VF|WF|XF|YF|ZF|AF|BF|CF|DF|EF|FF|GF|HF|IF|JF|KF|LF|MF|
|C|NE|OE|PE|QE|RE|SE|TE|UE|VE|WE|XE|YE|ZE|AE|BE|CE|DE|EE|FE|GE|HE|IE|JE|KE|LE|ME|
|D|ND|OD|PD|QD|RD|SD|TD|UD|VD|WD|XD|YD|ZD|AD|BD|CD|DD|ED|FD|GD|HD|ID|JD|KD|LD|MD|
|E|NC|OC|PC|QC|RC|SC|TC|UC|VC|WC|XC|YC|ZC|AC|BC|CC|DC|EC|FC|GC|HC|IC|JC|KC|LC|MC|
|F|NB|OB|PB|QB|RB|SB|TB|UB|VB|WB|XB|YB|ZB|AB|BB|CB|DB|EB|FB|GB|HB|IB|JB|KB|LB|MB|
|G|NA|OA|PA|QA|RA|SA|TA|UA|VA|WA|XA|YA|ZA|AA|BA|CA|DA|EA|FA|GA|HA|IA|JA|KA|LA|MA|
|H|NZ|OZ|PZ|QZ|RZ|SZ|TZ|UZ|VZ|WZ|XZ|YZ|ZZ|AZ|BZ|CZ|DZ|EZ|FZ|GZ|HZ|IZ|JZ|KZ|LZ|MZ|
|I|NY|OY|PY|QY|RY|SY|TY|UY|VY|WY|XY|YY|ZY|AY|BY|CY|DY|EY|FY|GY|HY|IY|JY|KY|LY|MY|
|J|NX|OX|PX|QX|RX|SX|TX|UX|VX|WX|XX|YX|ZX|AX|BX|CX|DX|EX|FX|GX|HX|IX|JX|KX|LX|MX|
|K|NW|OW|PW|QW|RW|SW|TW|UW|VW|WW|XW|YW|ZW|AW|BW|CW|DW|EW|FW|GW|HW|IW|JW|KW|LW|MW|
|L|NV|OV|PV|QV|RV|SV|TV|UV|VV|WV|XV|YV|ZV|AV|BV|CV|DV|EV|FV|GV|HV|IV|JV|KV|LV|MV|
|M|NU|OU|PU|QU|RU|SU|TU|UU|VU|WU|XU|YU|ZU|AU|BU|CU|DU|EU|FU|GU|HU|IU|JU|KU|LU|MU|
|N|NT|OT|PT|QT|RT|ST|TT|UT|VT|WT|XT|YT|ZT|AT|BT|CT|DT|ET|FT|GT|HT|IT|JT|KT|LT|MT|
|O|NS|OS|PS|QS|RS|SS|TS|US|VS|WS|XS|YS|ZS|AS|BS|CS|DS|ES|FS|GS|HS|IS|JS|KS|LS|MS|
|P|NR|OR|PR|QR|RR|SR|TR|UR|VR|WR|XR|YR|ZR|AR|BR|CR|DR|ER|FR|GR|HR|IR|JR|KR|LR|MR|
|Q|NQ|OQ|PQ|QQ|RQ|SQ|TQ|UQ|VQ|WQ|XQ|YQ|ZQ|AQ|BQ|CQ|DQ|EQ|FQ|GQ|HQ|IQ|JQ|KQ|LQ|MQ|
|R|NP|OP|PP|QP|RP|SP|TP|UP|VP|WP|XP|YP|ZP|AP|BP|CP|DP|EP|FP|GP|HP|IP|JP|KP|LP|MP|
|S|NO|OO|PO|QO|RO|SO|TO|UO|VO|WO|XO|YO|ZO|AO|BO|CO|DO|EO|FO|GO|HO|IO|JO|KO|LO|MO|
|T|NN|ON|PN|QN|RN|SN|TN|UN|VN|WN|XN|YN|ZN|AN|BN|CN|DN|EN|FN|GN|HN|IN|JN|KN|LN|MN|
|U|NM|OM|PM|QM|RM|SM|TM|UM|VM|WM|XM|YM|ZM|AM|BM|CM|DM|EM|FM|GM|HM|IM|JM|KM|LM|MM|
|V|NL|OL|PL|QL|RL|SL|TL|UL|VL|WL|XL|YL|ZL|AL|BL|CL|DL|EL|FL|GL|HL|IL|JL|KL|LL|ML|
|W|NK|OK|PK|QK|RK|SK|TK|UK|VK|WK|XK|YK|ZK|AK|BK|CK|DK|EK|FK|GK|HK|IK|JK|KK|LK|MK|
|X|NJ|OJ|PJ|QJ|RJ|SJ|TJ|UJ|VJ|WJ|XJ|YJ|ZJ|AJ|BJ|CJ|DJ|EJ|FJ|GJ|HJ|IJ|JJ|KJ|LJ|MJ|
|Y|NI|OI|PI|QI|RI|SI|TI|UI|VI|WI|XI|YI|ZI|AI|BI|CI|DI|EI|FI|GI|HI|II|JI|KI|LI|MI|
|Z|NH|OH|PH|QH|RH|SH|TH|UH|VH|WH|XH|YH|ZH|AH|BH|CH|DH|EH|FH|GH|HH|IH|JH|KH|LH|MH|

### 6. KEYBOARD
Este metodo reorganiza el alfabeto siguiendo el orden establecido en un tecaldo QWERTY y remplaza cada letra con su correspondiente en este nuevo alfabeto. 

|Entrada|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
|--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- |
|Salida |Q|W|E|R|T|Y|U|I|O|P|A|S|D|F|G|H|J|K|L|Ñ|Z|X|C|V|B|N|M|

### 7. BACON
Este metodo utiliza la clave de Bacon (Nombre del creador, utiliza combinaciones de A y B) para remplazar cada uno de los terminos de la cadena de caracteres.

|Entrada|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U/V|W|X|Y|Z|
|--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |
|Salida |AAAAA|AAAAB|AAABA|AAABB|AABAA|AABAB|AABBA|AABBB|ABAAA|ABAAA|ABAAB|ABABA|ABABB|ABBAA|ABBAB|ABBBA|ABBBB|BAAAA|BAAAB|BAABA|BAABB|BABAA|BABAB|BABBA|BABBB|

### 8. MORSE
Este metodo utiliza la clave de Morse (Nombre del creador, utiliza combinaciones de puntos y rayas) para remplazar cada uno de los terminos de la cadena de caracteres.

|Entrada|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
|--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- |--- | --- | ---|
|Salida |.-|-...|-.-.|-..|-|--.-|--.|....|..|.---|-.-|.-..|--|-.|---|.--.|--.-|.-.|...|-|..-|...-|.--|-..-|-.--|--..|

### 9. BASE 64
Este metodo transforma toda la cadena de caracteres en binario (cada caracter tiene una representación de 8 bits), luego dividide la cadena en binario en 6 bits y decodifica estas cadenas binarias de 6 bits nuevamente a su representacion original.

### 10. TAP (CUADRADO DE POLIBIO)
Este metodo toma cada caracter de la cadena y devuelve su coordenada dentro del cuadrado de Polibio (Primero fila luego columna).

|COORDENADAS|1|2|3|4|5|
|---|---|---|---|---|---|
|1|A|B|C|D|E|
|2|F|G|H|I/J|K|
|3|L|M|N/Ñ|O|P|
|4|Q|R|S|T|U|
|5|V|W|X|Y|Z|

### 12. ROT (CESAR)
Este metodo toma una clave (número), y translada cada letra ese mismo numero veces.

Ejemplo: se quiere codificar la palabra "MENSAJE" con un número de rotaciones de "3"

   |MENSAJE ORIGINAL|M|E|N|S|A|J|E|
   |---|---|---|---|---|---|---|---|
   |PRIMERA ROTACION|N|F|O|T|B|K|F|
   |SEGUNDA ROTACION|O|G|P|U|C|L|G|
   |TERCERA ROTACION|P|H|Q|V|D|M|H|
   
   Mensaje codificado: PHQVDMH

### 11. COLUMNAR
Este metodo toma una clave (letras), y organiza una matriz con la cadena de caractares a codificar para que tenga el mismo numero de columnas que letras en la clave (Esta matriz se completa con X). luego reorganiza las colunas resultantes debido al orden alfabetico de la clave.

Ejemplo: se quiere codificar la palabra "MENSAJE" con la clave "CLAVE"

Matriz original:

|C|L|A|V|E|
|---|---|---|---|---|
|M|E|N|S|A|
|J|E|X|X|X|

Reorganizando columnas:

|A|C|E|L|V|
|---|---|---|---|---|
|N|M|A|E|S|
|X|J|X|E|X|

Mensaje codificado: "NMAESXJXEX"



