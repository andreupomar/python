#Andreu Pomar Cabot
#Práctica 4: Hacer un programa para determinar si una cadena de números está en orden
print ("Este programa determina si una cadena de números está ordenada.\n")
a, b, c, d, e = list(map(int, input ("Introduzca una cadena de cinco números, separados por espacios \n").split()))

if a>b and b>c and c>d and d>e:
    print ("Los números están en orden descendiente")
elif a<b and b<c and c<d and d<e:
    print ("Los números están en orden ascendiente")
else:
    print ("Los números están desordenados")
