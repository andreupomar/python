#Andreu Pomar Cabot
#Ejercicio 7.11 - Palíndroma, avanzado

def Palindrome (entrada):
    if entrada.replace(" ","") == entrada.replace(" ","")[::-1]:
        return True
    

entrada = input ("Introduce una secuencia alfanumérica: \n")

if Palindrome (entrada) == True:
    print ("%s es palíndroma" % (entrada))
else:
    print (entrada[::-1])
