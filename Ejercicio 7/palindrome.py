#Andreu Pomar Cabot
#Ejercicio 7.10 - Palíndrome

def Palindrome (entrada):
    if entrada == entrada[::-1]:
        salida = ("%s es palíndrome o capicúa" % (entrada))
    else:
        salida = ("%s no es nada" % (entrada))
    return salida

entrada = input ("Introduce una secuencia alfanumérica: \n")

print (Palindrome (entrada))

        
    
