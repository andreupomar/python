#Andreu Pomar Cabot
#Práctica 7.2 - Función que une tres strings

nombre = str(input("Introduzca el nombre: "))
apell1 = str(input("Introduzca el primer apellido: "))
apell2 = str(input("Introduzca el segundo apellido: "))

def combinar():
       final = " tu nombre es: %s %s %s" % (nombre,apell1,apell2) 
       return final

final = combinar()

print (final)
