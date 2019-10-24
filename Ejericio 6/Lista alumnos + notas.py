#Andreu Pomar Cabot
#Programa que almacena listas de listas con cantidades variables de elementos

listado = []
alumno = []

nombre = str(input("Introduzca el nombre del alumno: "))

while nombre != "":
    alumno.append(nombre)
    nota = int(input("Introduzca una nota para %s: " % (nombre)))
    int(nota)
    while nota >= 0 and nota <= 10:
        alumno.append(nota)
        nota = int(input("Introduzca una nota para %s: " % (nombre)))
    listado.append(alumno)
    alumno = []
    nombre = str(input("Introduzca el nombre del alumno: "))

for i in listado:
    print (i)
