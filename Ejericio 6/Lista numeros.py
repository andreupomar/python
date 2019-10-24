#Andreu Pomar Cabot
#Ejercicio 6 - Hacer un programa que pide numeros y los une en una lista

print ("Este programa pide palabras hasta que reciba un input vacío, y luego imprime la lista de palabras que haya recibido")

palabra = input ("Escriba una palabra: ")
lista = []

while palabra != "Salir":
    lista.append (int(palabra))
    palabra=""
    palabra= input ("Escriba otra palabra, o pulse Enter: ")

print ("Las palabras son", lista)
    
