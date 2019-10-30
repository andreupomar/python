#Andreu Pomar Cabot
#Ejercicio 7.5 - Cambiar vocales de un string

frase = str(input("Introduzca una frase: "))
vocal = str(input("¿Qué vocal?"))

def rintintin():
    final = frase.replace("a",vocal)
    final = final.replace("e",vocal)
    final = final.replace("i",vocal)
    final = final.replace("o",vocal)
    final = final.replace("u",vocal)
    return final

print (rintintin())


