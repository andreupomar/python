#Andreu Pomar Cabot
#Ejercicio 6 - Hacer un programa que pide notas y las une en una lista

print ("Este programa pide notas hasta que reciba un input que no esté entre 0 y 10, y luego imprime la lista de palabras que haya recibido")

nota = int (input ("Escriba una nota: "))
lista = []

while nota >=0 and nota <=10:
    lista.append (nota)
    palabra=""
    palabra= input ("Escriba otra palabra, o pulse Enter: ")

print ("Las notas son", lista)
    
