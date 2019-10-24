#Andreu Pomar Cabot
#Práctica 3 - Programa que cuenta cuántas cifras tiene un número
print ("Este programa determina si un número tiene más de tres cifras \n")
numero = int(input ("Introduzca el número \n "))

if numero>=0 and numero<=999:
    print (numero,"tiene tres o menos cifras")

else:
    print (numero,"tiene cuatro o más cifras")

input ("\n Presione enter para cerrar el programa")
