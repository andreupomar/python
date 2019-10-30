#Andreu Pomar Cabot
#Escribir un programa que hace listas de listas de listas de listas de listas

listin = []
entrada = []

nombre = str(input("Introduzca un nombre: "))
telf = str(input("Introduzca el número de %s: " % (nombre)))

while nombre !="S":
    entrada.extend([nombre, telf])
    listin.extend([entrada])
    nombre = ""
    telf = ""
    entrada = []
    nombre = str(input("Introduzca un nombre: "))
    telf = str(input("Introduzca el número de %s: " % (nombre)))

for i in listin:
    print (i)
input ()


