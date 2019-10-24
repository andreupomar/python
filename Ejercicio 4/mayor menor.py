#Andreu Pomar Cabot
#Práctica 4: Hacer un programa para determinar qué numero es el mayor y qué numero es el menor
print ("Este programa determina cuál es el mayor y el menor de cinco números.\n")
a, b, c, d, e = list(map(int, input ("Introduzca los dos números que desea comparar, separados por un espacio \n").split()))
mayor=a
menor=a

if b>mayor:
    mayor=b
if c>mayor:
    mayor=c
if d>mayor:
    mayor=d
if e>mayor:
    mayor=e
print (mayor,"es el número mayor")

if b<menor:
    menor=b
if c<menor:
    menor=c
if d<menor:
    menor=d
if e<menor:
    menor=e
print (menor,"es el número menor")

input ("Presione enter para cerrar el programa")

