#Andreu Pomar Cabot
# Ejercicio 7.12b - Programa que cuente palabras

def CountVonCount (entrada):
    proceso = entrada.replace(","," ")
    proceso = proceso.replace(";"," ")
    proceso = proceso.replace("."," ")
    proceso = proceso.replace(":"," ")
    proceso = proceso.replace("-"," ")
    proceso = proceso.replace("_"," ")
    proceso = proceso.replace("*"," ")
    proceso = proceso.replace("/"," ")
    resultado = len(proceso.split())
    return resultado

entrada = input ("Introduce una secuencia de palabras: \n")

resultado = CountVonCount (entrada)
print ("%d! %d palabras! \nAh! Ah! Ah!" % (resultado, resultado))
input()
