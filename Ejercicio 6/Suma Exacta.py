#Andreu Pomar Cabot
#Ejercicio 6.7 - Programa que pide un limite y luego ints hasta llegar a sumar el limite sin pasarse

limit = int ( input ("Introduzca un número límite: "))

entrada = int ( input ("Introduzca un número a sumar: "))
total = entrada
valores = [entrada]


while total < limit:
    entrada = int ( input ("Introduzca un número a sumar: "))
    if entrada+total<=limit:
        valores.append (entrada)
        total = total + entrada
    else:
        print ("El total es %d, que supera %d. Inténtalo de nuevo" % (total+entrada, limit))

print ("La suma de todos los valores introducidos es %d, que es igual al límite %d" % (total, limit))
print ("Los valores introducidos son:", valores)

input ("Pulse Enter para cerrar el programa")
