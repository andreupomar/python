#Andreu Pomar Cabot
#Ejercicio 7.6 - Comprobar si un str contiene un caracter determinado

def sherlock():
    if frase.find(letra) > -1:
        return True
    else:
        return False

frase = str(input("Introduzca una frase: "))
letra = str(input("¿Qué letra hay que buscar? "))

if sherlock() == True:
    print ("Contiene la letra")
else:
    print ("No contiene la letra")

input ()
