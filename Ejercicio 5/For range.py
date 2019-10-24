#Andreu Pomar
#Ejercicio 5 - Bucles for, determina todos los numeros entre dos ints si son pares o impares

num1= int(input("Introduzca un numero"))
num2= int(input("Introduzca otro número"))

for i in range(num1, num2+1):
    if i%2==0:
        print ( i, "Es par")
    else:
        print ( i, "Es impar")
