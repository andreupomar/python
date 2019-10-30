#Andreu Pomar Cabot
#Ejercicio 6 - Hacer un programa que pida números entre dos números

print ("Este programa toma dos números como inputs. \nLuego toma inputs numéricos entre ambas cifras")

minimo = int (input ("Introduzca un número \n"))
maximo = int (input ("Introduzca un número mayor que %d \n" % (minimo)))

while minimo > maximo:
    print ("%d no es mayor que %d \n" % (maximo,minimo))
    maximo = int (input ("Introduzca un número mayor que %d: " % (minimo)))
           
entrada = int (input ("Introduzca un número comprendido entre %d y %d \n" % (minimo, maximo)))
valores = []

while entrada > minimo and  entrada < maximo:
    valores.append (entrada)
    entrada = int (input ("Introduzca un número comprendido entre %d y %d \n" % (minimo, maximo)))

print ("Los valores comprendidos entre %d y %d son: \n")
print (valores)
print ("\n pulse Enter para cerrar el programa")
    
    
