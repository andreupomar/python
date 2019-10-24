#Andreu Pomar Cabot
#Práctica 3: Hacer un programa para determinar la validez de una fecha
print ("Este programa determina si la fecha introducida es válida.\n")
dia = int(input("Por favor, introduzca el día \n"))
mes = int(input("Por favor, introduzca el mes (en números)\n"))
año = int(input("Por favor, introduzca el año \n"))

if (dia==0 or dia>31 or mes==0 or mes>12):
    print ("Esa fecha no es válida")

elif (mes==2 and dia>29):
    print ("Esa fecha no es válida")

elif (mes==4 or mes==6 or mes==9 or mes==11) and dia>30:
    print ("Esa fecha no es válida")

else:
    print ("\n El %d del %d de %d es una fecha válida" % (dia, mes, año))

input ("Pulse enter para cerrar el programa")
