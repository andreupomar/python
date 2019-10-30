#Andreu Pomar Cabot
#Práctica 6.13 - Determinadora de primos, pero mejorado

num = int (input ("Introduzca un número: "))
contador = 2

primo = True

while primo == True and contador < num:
    if num%contador == 0:
        primo = False
    else:
        contador+=1


if primo == True:
    print ("%d es un número primo" % (num))
else:
    print ("%d no es un número primo, se puede dividir entre %d" % (num, contador))

input()

#La ventaja de usar un while en vez de un for es que si le doy un número como 6*10^65 en cuanto haya dividido entre dos se parará y no realizará el resto
#de las 6*10^65 operaciones restantes que intentaría hacer con un for.
