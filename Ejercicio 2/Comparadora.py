#Andreu Pomar Cabot
#Práctica 2: Hacer un programa para determinar qué número es mayor
print ("Este programa te ayuda a saber cuál de los dos números es mayor.\n")
a, b = list(map(float, input ("Introduzca los dos números que desea comparar, separados por un espacio \n").split()))

if (a>b):
    print ("%f es mayor que %f \n" % (a, b))

elif (a<b):
    print ("%f es mayor que %f \n" % (b, a))

elif (a==b):
    print ("%f es igual que %f \n" % (a, b))

input ("Presione Enter para cerrar el programa")
