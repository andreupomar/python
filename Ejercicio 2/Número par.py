#Andreu Pomar Cabot
#Práctica 2: Hacer un programa para determinar si un número es par o impar
print ("Este programa determina si un número es par o impar.\n")
C= int(input ("Introduzca el número que no sabe si es par o impar \n")) 
N= C%2
if (N==0):
    print ("Efectivamente, %d es un número par." % (C))

else:
    print ("Por si no lo sabías, %d es un número impar." %(C))

input ("Presione Enter para cerrar el programa")
