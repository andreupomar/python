#Andreu Pomar Cabot
#Práctica 4: Hacer un programa para calcular áreas
print ("Este programa es capaz de calcular el área de un triángulo o un cuadrilatero regular.\n")
poligono= input ("¿Desea calcular el área de un triangulo o de un cuadrilatero? \n")
tri="triangulo"
cuadr="cuadrilatero"

if poligono==tri:
    base = float(input ("Introduzca la base del triángulo \n"))
    altura = float(input ("Introduzca la altura del triángulo \n"))
    A = (base*altura)/2
    print ("\n El área del triángulo con base %f y altura %f es %f" % (base, altura, A))

elif poligono==cuadr:
    base= float(input ("Introduzca la base del cuadrilátero \n"))
    altura= float(input ("Introduzca la altura del cuadrilátero \n"))
    A = (base*altura)
    print ("\n El área del triángulo con base %f y altura %f es %f" % (base, altura, A))

else:
    print ("Este programa no es capaz de calcular el área de un", poligono)

input ("Presione Enter para cerrar el programa")
    
