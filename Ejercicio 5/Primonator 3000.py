#Andreu Pomar Cabot
#Práctica 5 - Determinadora de primos

num = int (input ("Introduzca un número: "))

primo = True

for i in range(2,num):
    if num%i==0:
        primo = False

if primo == True:
    print ("Es primo")
else:
    print ("No es primo")
