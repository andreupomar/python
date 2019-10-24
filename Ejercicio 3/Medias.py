#Andreu Pomar Cabot
#Práctica 3 - Programa que calcula la media
print ("Este programa calcula la media de tres notas \n")
n1, n2, n3 = list(map(float, input ("Introduzca las tres notas cuya media quiera calcular (separadas por un espacio) \n").split()))
media = (n1+n2+n3)/3
print ("La media de ",n1," ",n2," y ",n3," es", media)
input ("Presione enter para cerrar el programa")
