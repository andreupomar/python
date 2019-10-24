#Andreu Pomar Cabot
#Ejercicio 6 - Hacer un programa que pide números incrementales y los guarda en una lista
print("Este programa pide números incrementales y los guarda en una lista")


entrada = int (input ("Escriba un numero: "))
ultimo = entrada-1
lista = []

while entrada > ultimo:
    lista.append (entrada)
    ultimo = entrada
    entrada =  int (input ("Escriba otro número, mayor que %d: " % (ultimo)))

print ("Los números son:",end=" ")
for i in lista:
    print (i,end=", ")

input()
