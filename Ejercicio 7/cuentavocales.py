#Andreu Pomar Cabot
#Ejercicio 7.7 - Contador de vocales

def TheCount():
    numa = frase.count("a")
    nume = frase.count("e")
    numi = frase.count("i")
    numo = frase.count("o")
    numu = frase.count("u")
    print ("La frase contiene: \n A: %d \n E: %d \n I: %d \n O: %d \n U: %d \n (Ah! Ah! Ah!)" % (numa,nume,numi,numo,numu))

frase = str(input("Introduce una frase, por favor: "))

TheCount()
input()
