#Andreu Pomar Cabot
#Ejercicio 6.7 - Programa que pide un limite y luego ints hasta llegar a sumar el limite

limit = int ( input ("Introduzca un número límite: "))

entrada = int ( input ("Introduzca un número a sumar: "))
total = entrada
valores = [entrada]

while total < limit:
    entrada = int ( input ("Introduzca un número a sumar: "))
    valores.append (entrada)
    total = total + entrada
    

print ("La suma de todos los valores introducidos es %d, que es superior al límite %d" % (total, limit))
print ("Los valores introducidos son:", valores)

input ("Pulse Enter para cerrar el programa")
