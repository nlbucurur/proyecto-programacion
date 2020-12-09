# proyecto-programación - Encriptado y Desencripatado

## Planteamiento y Justificación del Problema

El cifrado o la encriptación de mensajes han sido de gran utilidad e importancia a lo largo de la historia, ya que juegan un papel fundamental en la seguridad, tanto de un país, como de un mensaje enviado a través de una aplicación de mensajería, pagos electrónicos, bases de datos de grandes y pequeñas empresas, información personal de los usuarios, etc. Esta es una ciencia que evoluciona constantemente debido a que debe proteger información delicada. Se han encontrado metodos de cifrado desde el Siglo I a.C, y se han desarrollado de tal forma que, con ayuda de las compuadoras, son cada vez más complejos y díficiles de desencriptar, además se presenta una visión bastante amplia en el fúturo, ya que puede ser desarrollada como una aplicación de la computación cuántica, pues, el comportamiento de esta física es netamente probabilistico, permitiendo así, la superposición de los estados cuánticos, además se ha notado que estos estados en un sistema, colapsan al ser observados. Imaginar este tipo de encriptación, en la que, por ejemplo, al intentar leer una tarjeta de crédito cuántica para clonarla, esta colapse a un solo estado y pierda toda la información, puede ser posible, muestra un gran camino por recorrer en la ciencia y en especial, en este tipo de aplicación, aunque por ahora solo puede estar en nuestra imaginación.

Debido a la importancia del encriptado y desencriptado en la sociedad, este proyecto del curso de "Programación e Introducción a los métodos númericos" de la Universidad Nacional de Colombia, pretende crear un programa que encripte y desencripte textos dados por el ususario con algunos métodos que van desde los más sencillos, hasta algunos más complicados a través de una interfaz gráfica sencilla que permitirá mayor comodidad para el ususario a la hora de usar el programa. Además, permitirá desarrollar a los estudiantes, habilidades en la programción y conocimientos básicos en el área de la seguridad informatica.

## Métodos de Cifrado y Descifrado

A continuación se presentará la lista de metodos de encriptado que se trabajarán en este proyecto, se explicará en que consiste cada uno:

### 1. A1Z26 
Este método consiste en remplazar las letras del alfabeto por números que van desde el 1 hasta el 26.

A B C D E F G H I J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z 
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

### 2. ASCII
Este metodo remplaza cada letra introducida por su valor numerico correspondiente a la tabla ASCII.


### 3. ATBASH
Este método invierte el orden del alfabeto y remplaza cada letra con su correspondiente en este alfabeto invertido. 

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
Z Y X W V U T S R Q P O N M L K J I H G F E D C B A

### 4. BINARIO
Este metodo realiza el cambio a representación binaria para cada letra



