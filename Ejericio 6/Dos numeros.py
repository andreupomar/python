#Andreu Pomar Cabot
#Ejercicio 6 - Programa que pide dos inputs numéricos, el segundo mayor que el primero, y luego los imprime

num1 = int (input ("Introduce un número \n"))
num2 = int (input ("Introduce un número mayor que %d" % (num1)))

while num1 >= num2:
    print ("%d no es mayor que %d. \n" % (num2, num1))
    num2= int (input ("Vuelve a probar, anda. Mayor que %d:" % num1))

print ("\nLos números que has introducido son %d y %d. %d es el mayor." % (num1, num2, num2))
input ("Pulse Enter para continuar")
