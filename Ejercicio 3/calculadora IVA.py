#Andreu Pomar Cabot
#Práctica 3 - Programa que calcula el precio de una compra con iva
print ("Este programa calcula el IVA de un producto \n")
producto = str(input("¿Qué producto ha adquirido? \n"))
IVA = int(input("¿Cuál es el tipo de IVA del producto? \n"))
bimponible = float(input ("¿Cuál es la base imponible del producto adquirido? \n"))
pvp = ((IVA/100)+1)*bimponible
print ("\n Su %s con tipo de IVA del %d y con base imponible %f tiene un precio de venta al público de %f €" % (producto,IVA,bimponible,pvp))
